from io import BytesIO

from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import HRFlowable, Paragraph, SimpleDocTemplate, Spacer


def create_pdf(content):

    buffer = BytesIO()

    doc = SimpleDocTemplate(
        buffer,
        rightMargin=0.6 * inch,
        leftMargin=0.6 * inch,
        topMargin=0.6 * inch,
        bottomMargin=0.6 * inch,
    )

    styles = getSampleStyleSheet()

    # ---------- Custom Styles ---------- #

    title_style = ParagraphStyle(
        "Title",
        parent=styles["Heading1"],
        alignment=TA_CENTER,
        fontSize=22,
        leading=26,
        textColor=HexColor("#1F2937"),     
        spaceAfter=10,
    )

    heading_style = ParagraphStyle(
        "Heading",
        parent=styles["Heading2"],
        fontSize=13,
        textColor=HexColor("#0F4C81"),
        spaceBefore=12,
        spaceAfter=6,
    )

    body_style = ParagraphStyle(
        "Body",
        parent=styles["BodyText"],
        fontSize=10.5,
        leading=16,
        spaceAfter=4,
    )

    bullet_style = ParagraphStyle(
        "Bullet",
        parent=body_style,
        leftIndent=15,
    )

    story = []

    lines = content.split("\n")

    first_line = True

    for line in lines:

        line = line.strip()

        if not line:
            continue

        # Remove markdown symbols

        line = (
            line.replace("**", "")
            .replace("###", "")
            .replace("##", "")
            .replace("#", "")
        )

        # Skip markdown separators

        if line.startswith("---"):
            continue

        # Resume title

        if first_line:

            story.append(
                Paragraph(
                    f"<b>{line.upper()}</b>",
                    title_style,
                )
            )

            story.append(
                HRFlowable(
                    width="100%",
                    thickness=1.2,
                    color=HexColor("#0F4C81"),
                )
            )

            story.append(Spacer(1, 12))

            first_line = False
            continue

        # Section headings

        headings = [
            "Professional Summary",
            "Education",
            "Technical Skills",
            "Skills",
            "Experience",
            "Projects",
            "Certifications",
            "Contact Information",
        ]

        if line in headings:

            story.append(
                Paragraph(
                    f"<b>{line.upper()}</b>",
                    heading_style,
                )
            )

            story.append(
                HRFlowable(
                    width="100%",
                    thickness=0.6,
                    color=HexColor("#CCCCCC"),
                )
            )

            story.append(Spacer(1, 6))

            continue

        # Bullet points

        if line.startswith("*"):

            story.append(
                Paragraph(
                    f"• {line.replace('*', '').strip()}",
                    bullet_style,
                )
            )

            continue

        # Normal text

        story.append(
            Paragraph(
                line,
                body_style,
            )
        )

    doc.build(story)

    pdf = buffer.getvalue()

    buffer.close()

    return pdf