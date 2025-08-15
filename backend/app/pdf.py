from reportlab.lib.pagesizes import LETTER
from reportlab.pdfgen import canvas
import io
def make_simple_pdf(title: str, fields: dict) -> bytes:
    buf = io.BytesIO(); c = canvas.Canvas(buf, pagesize=LETTER); width, height = LETTER
    y = height - 72; c.setFont("Helvetica-Bold", 14); c.drawString(72, y, title); y -= 24
    c.setFont("Helvetica", 10)
    for k,v in fields.items():
        c.drawString(72, y, f"{k}: {v}"); y -= 14
        if y < 96: c.showPage(); y = height - 72
    c.showPage(); c.save(); return buf.getvalue()
