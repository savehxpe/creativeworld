"""
Creative Direction Report PDF Generator.
Generates premium branded PDF reports for Creative Diagnosis deliveries.
"""
import os
from datetime import datetime
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from config.settings import (
    COMPANY_NAME, COMPANY_TAGLINE, COMPANY_CONTACT, COMPANY_WEBSITE,
    BRAND_PRIMARY_COLOR, BRAND_ACCENT_COLOR, BRAND_TEXT_COLOR, BRAND_LIGHT_BG,
    AUDITS_DIR
)


class CreativeDirectionPDFGenerator:
    """
    Generates premium Creative Direction Report PDFs.
    """
    
    def __init__(self):
        os.makedirs(AUDITS_DIR, exist_ok=True)
        self.styles = getSampleStyleSheet()
        self._custom_styles()
    
    def _custom_styles(self):
        """Define custom paragraph styles for creative direction reports."""
        
        # Title style — large, bold, premium
        self.styles.add(ParagraphStyle(
            name="ReportTitle",
            fontSize=28,
            leading=34,
            textColor=BRAND_PRIMARY_COLOR,
            spaceAfter=6,
            fontName="Helvetica-Bold",
            alignment=1  # center
        ))
        
        # Subtitle style
        self.styles.add(ParagraphStyle(
            name="ReportSubtitle",
            fontSize=14,
            leading=18,
            textColor=BRAND_ACCENT_COLOR,
            spaceAfter=24,
            fontName="Helvetica-Bold",
            alignment=1  # center
        ))
        
        # Section heading
        self.styles.add(ParagraphStyle(
            name="SectionHeading",
            fontSize=16,
            leading=20,
            textColor=BRAND_ACCENT_COLOR,
            spaceAfter=10,
            spaceBefore=20,
            fontName="Helvetica-Bold"
        ))
        
        # Sub-section heading
        self.styles.add(ParagraphStyle(
            name="SubHeading",
            fontSize=12,
            leading=16,
            textColor=BRAND_PRIMARY_COLOR,
            spaceAfter=6,
            spaceBefore=12,
            fontName="Helvetica-Bold"
        ))
        
        # Body text
        self.styles.add(ParagraphStyle(
            name="ReportBody",
            fontSize=10,
            leading=15,
            textColor=BRAND_TEXT_COLOR,
            spaceAfter=8,
            alignment=4  # justified
        ))
        
        # Emphasis text (for key insights)
        self.styles.add(ParagraphStyle(
            name="Emphasis",
            fontSize=11,
            leading=16,
            textColor=BRAND_ACCENT_COLOR,
            spaceAfter=10,
            fontName="Helvetica-Bold"
        ))
        
        # Revenue numbers (highlighted)
        self.styles.add(ParagraphStyle(
            name="RevenueNumber",
            fontSize=14,
            leading=18,
            textColor=BRAND_ACCENT_COLOR,
            spaceAfter=6,
            fontName="Helvetica-Bold",
            alignment=1  # center
        ))
        
        # Quote/callout style
        self.styles.add(ParagraphStyle(
            name="Callout",
            fontSize=11,
            leading=16,
            textColor=BRAND_PRIMARY_COLOR,
            spaceAfter=12,
            spaceBefore=12,
            leftIndent=20,
            rightIndent=20,
            fontName="Helvetica-Oblique",
            backColor=BRAND_LIGHT_BG
        ))
        
        # Footer style
        self.styles.add(ParagraphStyle(
            name="Footer",
            fontSize=8,
            leading=10,
            textColor=BRAND_TEXT_COLOR,
            alignment=1  # center
        ))
    
    def generate_creative_diagnosis_report(self, brand_name, niche, audit_content, 
                                          revenue_analysis, blueprint_summary, 
                                          spec_ad_summaries, output_filename=None):
        """
        Generate a complete Creative Diagnosis PDF report.
        
        Args:
            brand_name: Name of the brand
            niche: Brand niche
            audit_content: The creative audit text
            revenue_analysis: Revenue loss analysis text
            blueprint_summary: 200% blueprint summary
            spec_ad_summaries: List of spec ad concept summaries
            output_filename: Optional custom filename
            
        Returns:
            Path to generated PDF
        """
        if not output_filename:
            output_filename = f"{brand_name.lower().replace(' ', '_')}_creative_diagnosis_{datetime.now().strftime('%Y-%m-%d')}.pdf"
        output_path = os.path.join(AUDITS_DIR, output_filename)
        
        doc = SimpleDocTemplate(
            output_path, 
            pagesize=A4,
            rightMargin=60, 
            leftMargin=60,
            topMargin=60, 
            bottomMargin=60
        )
        
        story = []
        
        # === COVER PAGE ===
        story.append(Spacer(1, 80))
        story.append(Paragraph(f"{COMPANY_NAME}", self.styles["ReportTitle"]))
        story.append(Paragraph("Creative Direction Report", self.styles["ReportSubtitle"]))
        story.append(Spacer(1, 40))
        
        # Brand info box
        cover_data = [
            [Paragraph("Prepared For:", self.styles["Footer"]), 
             Paragraph(brand_name, self.styles["SubHeading"])],
            [Paragraph("Industry:", self.styles["Footer"]), 
             Paragraph(niche.replace('_', ' ').title(), self.styles["ReportBody"])],
            [Paragraph("Date:", self.styles["Footer"]), 
             Paragraph(datetime.now().strftime("%d %B %Y"), self.styles["ReportBody"])],
            [Paragraph("Prepared By:", self.styles["Footer"]), 
             Paragraph(f"{COMPANY_NAME} Creative Direction Team", self.styles["ReportBody"])],
        ]
        
        cover_table = Table(cover_data, colWidths=[120, 300])
        cover_table.setStyle(TableStyle([
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("LEFTPADDING", (0, 0), (-1, -1), 10),
            ("RIGHTPADDING", (0, 0), (-1, -1), 10),
            ("TOPPADDING", (0, 0), (-1, -1), 8),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
            ("BACKGROUND", (0, 0), (-1, -1), BRAND_LIGHT_BG),
            ("GRID", (0, 0), (-1, -1), 0.5, colors.lightgrey),
        ]))
        story.append(cover_table)
        story.append(Spacer(1, 60))
        
        # Confidentiality notice
        story.append(Paragraph(
            "This report contains strategic creative direction insights tailored specifically for your brand. "
            "The concepts, analyses, and recommendations herein are confidential and proprietary.",
            self.styles["Footer"]
        ))
        
        story.append(PageBreak())
        
        # === EXECUTIVE SUMMARY ===
        story.append(Paragraph("Executive Summary", self.styles["SectionHeading"]))
        story.append(HRFlowable(width="100%", thickness=1, color=BRAND_ACCENT_COLOR))
        story.append(Spacer(1, 12))
        
        story.append(Paragraph(
            f"This Creative Diagnosis examines {brand_name}'s current creative presence, "
            f"identifies critical revenue gaps, and outlines a strategic path to 200% growth through "
            f"premium creative direction.",
            self.styles["ReportBody"]
        ))
        
        story.append(Spacer(1, 12))
        story.append(Paragraph("Key Findings:", self.styles["SubHeading"]))
        
        # Parse key findings from audit content (first few lines)
        story.append(Paragraph(audit_content[:500] + "...", self.styles["ReportBody"]))
        
        story.append(PageBreak())
        
        # === CREATIVE AUDIT ===
        story.append(Paragraph("1. Creative Direction Audit", self.styles["SectionHeading"]))
        story.append(HRFlowable(width="100%", thickness=1, color=BRAND_ACCENT_COLOR))
        story.append(Spacer(1, 12))
        
        # Parse and format audit content
        self._format_markdown_content(story, audit_content)
        
        story.append(PageBreak())
        
        # === REVENUE LOSS ===
        story.append(Paragraph("2. Revenue Loss Analysis", self.styles["SectionHeading"]))
        story.append(HRFlowable(width="100%", thickness=1, color=BRAND_ACCENT_COLOR))
        story.append(Spacer(1, 12))
        
        story.append(Paragraph(
            "The following analysis quantifies the revenue your brand is currently losing due to creative gaps. "
            "These are conservative estimates based on industry benchmarks for the South African market.",
            self.styles["ReportBody"]
        ))
        
        story.append(Spacer(1, 12))
        self._format_markdown_content(story, revenue_analysis)
        
        story.append(PageBreak())
        
        # === 200% BLUEPRINT ===
        story.append(Paragraph("3. The 200% Revenue Blueprint", self.styles["SectionHeading"]))
        story.append(HRFlowable(width="100%", thickness=1, color=BRAND_ACCENT_COLOR))
        story.append(Spacer(1, 12))
        
        story.append(Paragraph(
            "This blueprint outlines the strategic creative transformation that will double your brand's revenue. "
            "Each lever is actionable, measurable, and designed for the South African market.",
            self.styles["ReportBody"]
        ))
        
        story.append(Spacer(1, 12))
        self._format_markdown_content(story, blueprint_summary)
        
        story.append(PageBreak())
        
        # === SPEC AD CONCEPTS ===
        story.append(Paragraph("4. Spec Ad Concepts", self.styles["SectionHeading"]))
        story.append(HRFlowable(width="100%", thickness=1, color=BRAND_ACCENT_COLOR))
        story.append(Spacer(1, 12))
        
        story.append(Paragraph(
            "The following spec ad concepts demonstrate what premium creative direction looks like for your brand. "
            "These are not templates — they are strategic previews tailored to your competitive landscape.",
            self.styles["ReportBody"]
        ))
        
        story.append(Spacer(1, 16))
        
        for i, spec_summary in enumerate(spec_ad_summaries, 1):
            story.append(Paragraph(f"Concept {i}", self.styles["SubHeading"]))
            self._format_markdown_content(story, spec_summary)
            story.append(Spacer(1, 12))
        
        story.append(PageBreak())
        
        # === NEXT STEPS ===
        story.append(Paragraph("5. Next Steps", self.styles["SectionHeading"]))
        story.append(HRFlowable(width="100%", thickness=1, color=BRAND_ACCENT_COLOR))
        story.append(Spacer(1, 12))
        
        story.append(Paragraph(
            "Based on this Creative Diagnosis, we recommend the following action plan:",
            self.styles["ReportBody"]
        ))
        
        next_steps = [
            ("Immediate (Week 1)", "Schedule a follow-up call to review this report and discuss priority fixes."),
            ("Short-term (Month 1)", "Implement the top 3 creative changes identified in the audit. Begin content system overhaul."),
            ("Medium-term (Month 2-3)", "Launch the first campaign using the spec ad concepts. Measure performance against baseline."),
            ("Long-term (Month 4-12)", "Build a consistent monthly creative direction system. Scale what works. Iterate what doesn't."),
        ]
        
        for step_title, step_desc in next_steps:
            story.append(Paragraph(step_title, self.styles["SubHeading"]))
            story.append(Paragraph(step_desc, self.styles["ReportBody"]))
            story.append(Spacer(1, 8))
        
        story.append(Spacer(1, 30))
        
        # === FOOTER ===
        story.append(HRFlowable(width="100%", thickness=0.5, color=colors.lightgrey))
        story.append(Spacer(1, 12))
        story.append(Paragraph(
            f"{COMPANY_NAME} | {COMPANY_TAGLINE}<br/>"
            f"{COMPANY_CONTACT} | {COMPANY_WEBSITE}<br/>"
            f"This report is confidential and proprietary. © {datetime.now().year} {COMPANY_NAME}.",
            self.styles["Footer"]
        ))
        
        # Build PDF
        doc.build(story)
        print(f"  [PDF] Creative Direction Report saved: {output_path}")
        return output_path
    
    def _format_markdown_content(self, story, content):
        """Parse markdown-style content and add to story."""
        if not content:
            story.append(Paragraph("[Content not available]", self.styles["ReportBody"]))
            return
        
        for line in content.split("\n"):
            line = line.strip()
            if not line:
                story.append(Spacer(1, 6))
                continue
            
            # Handle bold headings
            if line.startswith("**") and line.endswith("**"):
                clean = line.replace("**", "")
                story.append(Paragraph(clean, self.styles["SubHeading"]))
            
            # Handle bullet points
            elif line.startswith("-") or line.startswith("*"):
                clean = line[1:].strip()
                story.append(Paragraph(f"• {clean}", self.styles["ReportBody"]))
            
            # Handle numbered lists
            elif line[0].isdigit() and "." in line[:3]:
                story.append(Paragraph(line, self.styles["ReportBody"]))
            
            # Regular paragraph
            else:
                story.append(Paragraph(line, self.styles["ReportBody"]))
    
    def generate_simple_report(self, brand_name, niche, content, output_filename=None):
        """
        Generate a simple branded report (for quick turnarounds).
        """
        if not output_filename:
            output_filename = f"{brand_name.lower().replace(' ', '_')}_report_{datetime.now().strftime('%Y-%m-%d')}.pdf"
        output_path = os.path.join(AUDITS_DIR, output_filename)
        
        doc = SimpleDocTemplate(
            output_path, 
            pagesize=A4,
            rightMargin=50, 
            leftMargin=50,
            topMargin=50, 
            bottomMargin=50
        )
        
        story = []
        
        # Header
        story.append(Paragraph(f"{COMPANY_NAME}", self.styles["ReportTitle"]))
        story.append(Paragraph(f"Creative Direction Report for {brand_name}", self.styles["ReportSubtitle"]))
        story.append(Paragraph(
            f"Niche: {niche.replace('_', ' ').title()}  |  Date: {datetime.now().strftime('%d %B %Y')}",
            self.styles["ReportBody"]
        ))
        story.append(Spacer(1, 20))
        
        # Content
        self._format_markdown_content(story, content)
        
        story.append(Spacer(1, 30))
        story.append(Paragraph(f"— {COMPANY_TAGLINE}", self.styles["ReportBody"]))
        story.append(Paragraph(f"Contact: {COMPANY_CONTACT}", self.styles["ReportBody"]))
        
        doc.build(story)
        print(f"  [PDF] Simple report saved: {output_path}")
        return output_path
