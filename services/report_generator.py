from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
)

from reportlab.lib.units import inch


class PDFReport:

    @staticmethod
    def create(
        filename,
        title,
        content
    ):

        doc = SimpleDocTemplate(filename)

        styles = getSampleStyleSheet()

        story = []

        story.append(
            Paragraph(
                "<b>Market X</b>",
                styles["Title"]
            )
        )

        story.append(
            Spacer(
                1,
                0.3*inch
            )
        )

        story.append(
            Paragraph(
                title,
                styles["Heading1"]
            )
        )

        story.append(
            Spacer(
                1,
                0.2*inch
            )
        )

        for line in content.split("\n"):

            story.append(
                Paragraph(
                    line,
                    styles["BodyText"]
                )
            )

        doc.build(story)
