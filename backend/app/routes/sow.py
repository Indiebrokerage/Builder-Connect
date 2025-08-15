from fastapi import APIRouter
router = APIRouter(prefix="/v1/sow", tags=["sow"])
@router.post("/draft")
def create_sow(payload: dict):
    return {"ok": True, "sow_id": "sow_demo_001", "content": payload}
@router.post("/{sow_id}/sign")
def sign_sow(sow_id: str):
    return {"ok": True, "sow_id": sow_id, "status": "signed"}
