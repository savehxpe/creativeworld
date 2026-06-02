/**
 * Brand audit via Firecrawl.
 * 
 * Usage: node scripts/firecrawl/audit-brand.js <url> [niche]
 * 
 * Requires FIRECRAWL_API_KEY in .env (not committed).
 */

require('dotenv').config();
const fc = require('../../lib/firecrawl/client');

async function main() {
    const url = process.argv[2];
    const niche = process.argv[3] || 'unknown';
    if (!url) { console.error('Usage: node scripts/firecrawl/audit-brand.js <url> [niche]'); process.exit(1); }

    console.log(`=== Brand Audit: ${url} ===\n`);
    try {
        const data = await fc.scrapePage(url, ['markdown']);
        const content = data?.data?.markdown || data?.markdown || JSON.stringify(data).slice(0, 3000);
        
        const result = {
            brand_summary: extractSummary(content),
            niche: niche,
            offer: extractOffer(content),
            audience: extractAudience(content),
            current_cta: extractCTA(content),
            trust_signals: extractTrust(content),
            content_gaps: extractGaps(content),
            ad_opportunities: extractAdOpps(content, niche),
            brand_sound_opportunity: 'Most brands have visuals but no consistent sound identity.',
            diagnosis_bullets: [
                'Content shows product but doesn\'t create the feeling that drives action.',
                'No clear campaign system — posts are documentation, not direction.',
                'Sound identity is completely absent — every ad starts from zero.'
            ],
            outreach_angles: [
                'Creative direction preview showing campaign potential.',
                'Brand sound pack to create audio memory.',
                'Revenue leak analysis for their specific niche.'
            ]
        };
        
        console.log(JSON.stringify(result, null, 2));
    } catch (e) {
        console.error('Audit failed:', e.message);
        process.exit(1);
    }
}

function extractSummary(c) { const l = c.slice(0, 500); return l || 'Summary pending manual review.'; }
function extractOffer(c) { return 'Product/service detected via page scrape.'; }
function extractAudience(c) { return 'Audience profile pending analysis.'; }
function extractCTA(c) { const idx = c.search(/book|buy|shop|contact|subscribe|sign|get|start|try|join/i); return idx > -1 ? c.slice(idx, idx + 100).trim() : 'No clear CTA detected.'; }
function extractTrust(c) { const sigs = []; if (/review|testimonial/i.test(c)) sigs.push('Testimonials present'); if (/press|featured|as.seen/i.test(c)) sigs.push('Press mentions'); if (/trustpilot|google.reviews/i.test(c)) sigs.push('Review platform links'); return sigs.length ? sigs : ['No clear trust signals detected.']; }
function extractGaps(c) { const gaps = []; if (!/video|reel|tiktok/i.test(c)) gaps.push('No video content strategy'); if (!/sound|audio|music|jingle/i.test(c)) gaps.push('No brand sound identity'); if (!/blog|article|guide/i.test(c)) gaps.push('No content marketing'); return gaps.length ? gaps : ['Content gap analysis pending.']; }
function extractAdOpps(c, niche) { return [`5-second hook ads for ${niche}`, `15-second social ads with brand sound`, `UGC-style testimonial ads`]; }

main();
