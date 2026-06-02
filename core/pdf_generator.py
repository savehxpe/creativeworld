"""
PDF Audit Report generator using ReportLab.
"""
import os
from datetime import datetime
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle, PageBreak
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from config.settings import (
    COMPANY_NAME, COMPANY_TAGLINE, COMPANY_CONTACT,
    BRAND_PRIMARY_COLOR, BRAND_ACCENT_COLOR, BRAND_TEXT_COLOR, BRAND_LIGHT_BG,
    AUDITS_DIR
)


class PDFGenerator:
    def __init__(self):
        os.makedirs(AUDITS_DIR, exist_ok=True)
        self.styles = getSampleStyleSheet()
        self._custom_styles()

    def _custom_styles(self):
        self.styles.add(ParagraphStyle(
            name="Title",
            fontSize=24,
            leading=30,
            textColor=BRAND_PRIMARY_COLOR,
            spaceAfter=12,
            fontName="Helvetica-Bold"
        ))
        self.styles.add(ParagraphStyle(
            name="Heading",
            fontSize=14,
            leading=18,
            textColor=BRAND_ACCENT_COLOR,
            spaceAfter=8,
            spaceBefore=12,
            fontName="Helvetica-Bold"
        ))
        self.styles.add(ParagraphStyle(
            name="Body",
            fontSize=10,
            leading=14,
            textColor=BRAND_TEXT_COLOR,
            spaceAfter=8
        ))
        self.styles.add(ParagraphStyle(
            name="ScoreLabel",
            fontSize=10,
            leading=12,
            textColor=BRAND_TEXT_COLOR,
            alignment=1  # center
        ))
        self.styles.add(ParagraphStyle(
            name="ScoreValue",
            fontSize=16,
            leading=20,
            textColor=BRAND_PRIMARY_COLOR,
            alignment=1,
            fontName="Helvetica-Bold"
        ))

    def generate(self, handle, niche, lighthouse_scores, ai_summary, screenshot_path, output_filename=None):
        """
        Generate a professional PDF audit report.
        Returns the file path.
        """
        if not output_filename:
            output_filename = f"{handle}_audit_{datetime.now().strftime('%Y-%m-%d')}.pdf"
        output_path = os.path.join(AUDITS_DIR, output_filename)

        doc = SimpleDocTemplate(output_path, pagesize=A4,
                                rightMargin=50, leftMargin=50,
                                topMargin=50, bottomMargin=50)
        story = []

        # Header
        story.append(Paragraph(f"{COMPANY_NAME}", self.styles["Title"]))
        story.append(Paragraph(f"Website Audit for @{handle}", self.styles["Heading"]))
        story.append(Paragraph(f"Niche: {niche.replace('_', ' ').title()}  |  Date: {datetime.now().strftime('%d %B %Y')}", self.styles["Body"]))
        story.append(Spacer(1, 20))

        # Lighthouse Score Card
        story.append(Paragraph("Lighthouse Scores", self.styles["Heading"]))
        score_data = []
        for key, val in lighthouse_scores.items():
            label = key.replace("-", " ").title()
            color = self._score_color(val)
            score_data.append([
                Paragraph(f"<font color='{color}'><b>{val}</b></font>", self.styles["ScoreValue"]),
                Paragraph(label, self.styles["ScoreLabel"])
            ])

        if score_data:
            score_table = Table(score_data, colWidths=[doc.width / len(score_data)] * len(score_data))
            score_table.setStyle(TableStyle([
                ("ALIGN", (0, 0), (-1, -1), "CENTER"),
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                ("TOPPADDING", (0, 0), (-1, -1), 10),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
                ("BACKGROUND", (0, 0), (-1, -1), BRAND_LIGHT_BG),
                ("GRID", (0, 0), (-1, -1), 0.5, colors.lightgrey),
            ]))
            story.append(score_table)
            story.append(Spacer(1, 20))

        # Screenshot
        if screenshot_path and os.path.exists(screenshot_path):
            story.append(Paragraph("Website Screenshot", self.styles["Heading"]))
            try:
                img = Image(screenshot_path, width=6 * inch, height=3.5 * inch)
                img.hAlign = "CENTER"
                story.append(img)
                story.append(Spacer(1, 20))
            except Exception:
                story.append(Paragraph("[Screenshot unavailable]", self.styles["Body"]))

        # AI Analysis
        story.append(PageBreak())
        story.append(Paragraph("Expert Analysis", self.styles["Heading"]))

        # Parse markdown-style headers in AI summary
        for line in ai_summary.split("\n"):
            line = line.strip()
            if not line:
                story.append(Spacer(1, 6))
                continue
            if line.startswith("**") and line.endswith("**"):
                story.append(Paragraph(line.replace("**", ""), self.styles["Heading"]))
            elif line.startswith("-"):
                story.append(Paragraph(f"• {line[1:].strip()}", self.styles["Body"]))
            else:
                story.append(Paragraph(line, self.styles["Body"]))

        story.append(Spacer(1, 30))
        story.append(Paragraph(f"— {COMPANY_TAGLINE}", self.styles["Body"]))
        story.append(Paragraph(f"Contact: {COMPANY_CONTACT}", self.styles["Body"]))

        doc.build(story)
        print(f"  [PDF] Saved: {output_path}")
        return output_path

    def _score_color(self, score):
        if score >= 90:
            return "#2e7d32"  # green
        elif score >= 70:
            return "#f9a825"  # yellow
        else:
            return "#c62828"  # red
