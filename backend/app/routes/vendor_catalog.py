from fastapi import APIRouter, Query
from typing import Dict, List
from .. import db
router = APIRouter(prefix="/v1/vendors", tags=["vendors"])
def _search(items: List[Dict], q: str):
    ql = q.lower(); return [it for it in items if ql in it["name"].lower()]
@router.get("/search")
def search_all(q: str = Query(..., description="Search term")):
    hd = _search(db.VENDORS.get("homedepot", []), q)
    lw = _search(db.VENDORS.get("lowes", []), q)
    mn = _search(db.VENDORS.get("menards", []), q)
    return {"homedepot": hd, "lowes": lw, "menards": mn}
