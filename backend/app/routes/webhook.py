from fastapi import APIRouter, Request
router = APIRouter(prefix="/v1/factori", tags=["factori"])
@router.post("/webhook")
async def webhook(req: Request):
    body = await req.json()
    return {"received": body, "ok": True}
