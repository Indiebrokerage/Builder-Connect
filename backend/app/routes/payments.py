from fastapi import APIRouter
router = APIRouter(prefix="/v1/payments", tags=["payments"])
@router.post("/negotiate")
def negotiate(payload: dict):
    return {"ok": True, "agreement_id": "agree_demo_001", "schedule": payload}
@router.post("/charge")
def charge(payload: dict):
    return {"ok": True, "charge_id": "ch_demo_001", "status": "succeeded"}
