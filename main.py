"""
Outworld Lead Engine — Main CLI Orchestrator.

Usage:
    python main.py --batch data/batches/today.txt
    python main.py --batch data/batches/today.txt --send-dms
    python main.py --follow-ups

Workflow:
    1. Load handles from batch file
    2. For each handle:
        a. Scrape Instagram bio → find website
        b. Capture website screenshot + Lighthouse audit
        c. AI analysis (OpenRouter)
        d. Generate PDF audit report
        e. Generate 3 DM variants
        f. Save to database
    3. Optionally launch Instagram bot to send DMs (human-in-the-loop)
    4. Follow-up reminders
"""
import argparse
import os
import sys

# Ensure project root is on path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from core.database import LeadDatabase
from core.scraper import WebScraper
from core.lighthouse import LighthouseAuditor
from core.ai_analyzer import AIAnalyzer
from core.pdf_generator import PDFGenerator
from core.copywriter import DMCopywriter
from core.instagram_bot import InstagramBot
from config.niches import detect_niche
from config.services import get_recommended_services, get_primary_pitch
from prompts.audit_prompts import build_audit_prompt, build_no_website_prompt
from config.settings import BATCHES_DIR, OUTREACH_DIR


def process_lead(handle, db, scraper, lighthouse, ai, pdf_gen, copywriter, send_dms=False, bot=None):
    """Process a single lead end-to-end."""
    print(f"\n{'='*60}")
    print(f"Processing lead: @{handle}")
    print(f"{'='*60}")

    # Step 1: Scrape Instagram bio
    ig_data = scraper.scrape_instagram_bio(handle)
    website_url = ig_data.get("website_url")
    bio_text = ig_data.get("bio_text", "")

    # Step 2: Detect niche
    niche = detect_niche(handle, bio_text, "")
    print(f"  Detected niche: {niche}")

    # Step 3: Website research + Lighthouse
    screenshot_path = None
    lighthouse_result = {"scores": {}, "flags": []}
    page_text = ""

    if website_url:
        print(f"  Found website: {website_url}")
        site_data = scraper.capture_website(website_url, handle)
        screenshot_path = site_data.get("screenshot_path")
        page_text = site_data.get("text_content", "")
        lighthouse_result = lighthouse.run(website_url)
    else:
        print(f"  [!] No website found for @{handle}")
        lighthouse_result["flags"].append("no_website")

    # Step 4: AI Analysis
    if website_url:
        audit_prompt = build_audit_prompt(
            screenshot_description="See attached screenshot and Lighthouse scores.",
            lighthouse_json=lighthouse_result,
            niche=niche,
            handle=handle
        )
    else:
        audit_prompt = build_no_website_prompt(handle, niche, bio_text)

    try:
        ai_summary = ai.analyze_website(audit_prompt)
    except Exception as e:
        print(f"  [!] AI analysis failed: {e}")
        ai_summary = "AI analysis unavailable. Manual review recommended."

    # Step 5: Generate PDF
    try:
        pdf_path = pdf_gen.generate(
            handle=handle,
            niche=niche,
            lighthouse_scores=lighthouse_result.get("scores", {}),
            ai_summary=ai_summary,
            screenshot_path=screenshot_path
        )
    except Exception as e:
        print(f"  [!] PDF generation failed: {e}")
        pdf_path = None

    # Step 6: Generate DM variants
    has_website = bool(website_url)
    audit_flags = lighthouse_result.get("flags", [])
    if not has_website:
        audit_flags.append("no_website")

    service_pitch = get_primary_pitch(audit_flags)

    try:
        outreach_path, dm_variants = copywriter.generate(
            handle=handle,
            niche_key=niche,
            audit_summary=ai_summary,
            website_found=has_website,
            service_pitch=service_pitch
        )
    except Exception as e:
        print(f"  [!] DM generation failed: {e}")
        outreach_path = None
        dm_variants = {"soft": "", "value": "", "direct": ""}

    # Step 7: Save to database
    lead_id = db.add_lead(
        handle=handle,
        niche=niche,
        website_found=website_url,
        has_website=has_website,
        audit_pdf_path=pdf_path,
        outreach_dir=outreach_path
    )

    # Step 8: Send DM (human-in-the-loop)
    sent = False
    if send_dms and bot and outreach_path and dm_variants:
        # Use the "soft" variant as default for sending
        message = dm_variants.get("soft", "")
        if message:
            sent = bot.send_dm(handle, message)
            if sent:
                db.update_lead_status(handle, "contacted", notes="DM sent via bot")
                db.schedule_follow_ups(handle)
            else:
                db.update_lead_status(handle, "discovered", notes="User skipped DM send")
        else:
            db.update_lead_status(handle, "discovered", notes="No DM variant generated")
    else:
        db.update_lead_status(handle, "discovered", notes="Ready for manual outreach")

    print(f"\n  Lead @{handle} complete.")
    print(f"  PDF: {pdf_path or 'N/A'}")
    print(f"  DMs: {outreach_path or 'N/A'}")
    if sent:
        print(f"  Status: DM sent")
    elif send_dms:
        print(f"  Status: Skipped or failed")
    else:
        print(f"  Status: Drafted (run with --send-dms to send)")

    return {
        "handle": handle,
        "niche": niche,
        "website": website_url,
        "pdf": pdf_path,
        "outreach": outreach_path,
        "sent": sent
    }


def main():
    parser = argparse.ArgumentParser(description="Outworld Lead Engine")
    parser.add_argument("--batch", type=str, help="Path to .txt file with Instagram handles (one per line)")
    parser.add_argument("--send-dms", action="store_true", help="Launch Instagram bot to send DMs (human-in-the-loop)")
    parser.add_argument("--follow-ups", action="store_true", help="Show pending follow-ups")
    parser.add_argument("--handle", type=str, help="Process a single handle")
    args = parser.parse_args()

    # Init database
    db = LeadDatabase()

    # Show follow-ups mode
    if args.follow_ups:
        print("\nPending Follow-Ups:")
        rows = db.get_pending_follow_ups()
        if not rows:
            print("  No follow-ups due today.")
        for row in rows:
            handle, niche, status, f1, f2 = row
            print(f"  @{handle} ({niche}) | Status: {status} | F1: {f1} | F2: {f2}")
        return

    # Determine handles to process
    handles = []
    if args.handle:
        handles = [args.handle.strip().lstrip("@")]
    elif args.batch:
        if not os.path.exists(args.batch):
            print(f"[!] Batch file not found: {args.batch}")
            return
        with open(args.batch, "r", encoding="utf-8") as f:
            handles = [line.strip().lstrip("@") for line in f if line.strip() and not line.startswith("#")]
    else:
        print("[!] Provide --batch, --handle, or --follow-ups")
        parser.print_help()
        return

    if not handles:
        print("[!] No handles found to process.")
        return

    print(f"\n[Outworld] Processing {len(handles)} lead(s)...")
    print(f"  Send DMs: {'Yes (human-in-the-loop)' if args.send_dms else 'No'}")

    # Initialize core components
    scraper = WebScraper()
    lighthouse = LighthouseAuditor()
    ai = AIAnalyzer()
    pdf_gen = PDFGenerator()
    copywriter = DMCopywriter()

    bot = None
    if args.send_dms:
        bot = InstagramBot()
        bot.start()

    results = []
    try:
        for handle in handles:
            try:
                result = process_lead(
                    handle=handle,
                    db=db,
                    scraper=scraper,
                    lighthouse=lighthouse,
                    ai=ai,
                    pdf_gen=pdf_gen,
                    copywriter=copywriter,
                    send_dms=args.send_dms,
                    bot=bot
                )
                results.append(result)
            except Exception as e:
                print(f"[!] Fatal error processing @{handle}: {e}")
                continue
    finally:
        if bot:
            bot.close()

    # Summary
    print(f"\n{'='*60}")
    print("BATCH COMPLETE")
    print(f"{'='*60}")
    print(f"Processed: {len(results)}")
    print(f"PDFs generated: {sum(1 for r in results if r['pdf'])}")
    print(f"DMs drafted: {sum(1 for r in results if r['outreach'])}")
    if args.send_dms:
        print(f"DMs sent: {sum(1 for r in results if r['sent'])}")
    print(f"\nOutput folders:")
    print(f"  Audits: {os.path.abspath('output/audits')}")
    print(f"  Outreach: {os.path.abspath(OUTREACH_DIR)}")


if __name__ == "__main__":
    main()
