from fastapi import APIRouter, Response
from ..pdf import make_simple_pdf
router = APIRouter(prefix="/v1/pdf", tags=["pdf"])
@router.post("/sow")
def sow_pdf(payload: dict):
    pdf = make_simple_pdf("Statement of Work", payload)
    return Response(content=pdf, media_type="application/pdf", headers={"Content-Disposition": "attachment; filename=sow.pdf"})
@router.post("/change_order")
def co_pdf(payload: dict):
    pdf = make_simple_pdf("Change Order", payload)
    return Response(content=pdf, media_type="application/pdf", headers={"Content-Disposition": "attachment; filename=change_order.pdf"})
