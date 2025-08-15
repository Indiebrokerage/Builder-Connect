from fastapi import APIRouter
router = APIRouter(prefix="/v1/change_orders", tags=["change_orders"])
@router.post("/submit")
def submit_co(payload: dict):
    return {"ok": True, "co_id": "co_demo_001", "status": "submitted", "payload": payload}
@router.post("/{co_id}/approve")
def approve_co(co_id: str):
    return {"ok": True, "co_id": co_id, "status": "approved"}
