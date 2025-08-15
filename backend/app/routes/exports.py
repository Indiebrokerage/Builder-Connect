from fastapi import APIRouter, Response, HTTPException
from .. import db
import csv, io
router = APIRouter(prefix="/v1/exports", tags=["exports"])
@router.get("/bidsheet/{project_id}.csv")
def bidsheet_csv(project_id: str):
    data = [["Line Item","Vendor","Projected Cost","Committed Cost","Status"]]
    proj = db.PROJECTS.get(project_id)
    if proj:
        vendor_map = db.VENDORS
        for ln in proj.get("lines", []):
            pref = ln.get("vendor_pref"); items = vendor_map.get(pref, [])
            price = items[0]["price"] if items else 0.0
            projected = round(price * ln.get("qty", 1), 2)
            data.append([ln["desc"], pref, projected, "", "pending"])
    buf = io.StringIO(); csv.writer(buf).writerows(data)
    return Response(content=buf.getvalue(), media_type="text/csv",
                    headers={"Content-Disposition": f"attachment; filename=bidsheet_{project_id}.csv"})
@router.get("/bidsheet/{project_id}.xlsx")
def bidsheet_xlsx(project_id: str):
    try:
        from openpyxl import Workbook
    except Exception as e:
        raise HTTPException(500, f"openpyxl not installed: {e}")
    proj = db.PROJECTS.get(project_id)
    if not proj: raise HTTPException(404, f"Project {project_id} not found")
    wb = Workbook(); ws = wb.active; ws.title = "Bid Sheet"
    ws.append(["Line Item","Vendor","Projected Cost","Committed Cost","Status"])
    vendor_map = db.VENDORS
    for ln in proj.get("lines", []):
        pref = ln.get("vendor_pref"); items = vendor_map.get(pref, [])
        price = items[0]["price"] if items else 0.0
        projected = round(price * ln.get("qty", 1), 2)
        ws.append([ln["desc"], pref, projected, "", "pending"])
    bio = io.BytesIO(); wb.save(bio); bio.seek(0)
    return Response(content=bio.getvalue(),
        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        headers={"Content-Disposition": f"attachment; filename=bidsheet_{project_id}.xlsx"})
@router.get("/bidsheet/{project_id}.pdf")
def bidsheet_pdf(project_id: str):
    try:
        from reportlab.lib.pagesizes import LETTER
        from reportlab.pdfgen import canvas
    except Exception as e:
        raise HTTPException(500, f"reportlab not installed: {e}")
    proj = db.PROJECTS.get(project_id)
    if not proj: raise HTTPException(404, f"Project {project_id} not found")
    import io; buf = io.BytesIO(); c = canvas.Canvas(buf, pagesize=LETTER); width, height = LETTER
    y = height - 72; c.setFont("Helvetica-Bold", 14); c.drawString(72, y, f"Bid Sheet — {proj['name']}"); y -= 24
    c.setFont("Helvetica", 10); c.drawString(72, y, f"Project ID: {project_id}"); y -= 16
    c.drawString(72, y, f"Address: {proj.get('address','')}"); y -= 24
    c.setFont("Helvetica-Bold", 11); c.drawString(72, y, "Line Item"); c.drawString(250, y, "Vendor"); c.drawString(360, y, "Projected"); y -= 16
    c.setFont("Helvetica", 10)
    vendor_map = db.VENDORS
    for ln in proj.get("lines", []):
        pref = ln.get("vendor_pref"); items = vendor_map.get(pref, [])
        price = items[0]["price"] if items else 0.0
        projected = round(price * ln.get("qty", 1), 2)
        c.drawString(72, y, ln["desc"][:28]); c.drawString(250, y, (pref or "-")); c.drawRightString(430, y, f"${projected:,.2f}"); y -= 14
        if y < 96: c.showPage(); y = height - 72
    c.showPage(); c.save(); pdf = buf.getvalue()
    return Response(content=pdf, media_type="application/pdf",
                    headers={"Content-Disposition": f"attachment; filename=bidsheet_{project_id}.pdf"})
