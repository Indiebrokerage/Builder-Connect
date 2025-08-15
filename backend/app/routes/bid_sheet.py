from fastapi import APIRouter
router = APIRouter(prefix="/v1/bid_sheet", tags=["bidsheet"])
@router.post("/{project_id}/rebuild")
def rebuild(project_id: str):
    return {"ok": True, "project_id": project_id, "status": "rebuilt"}
