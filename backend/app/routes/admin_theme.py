from fastapi import APIRouter, HTTPException
import subprocess, os, time, shutil
router = APIRouter(prefix="/v1/admin/theme", tags=["admin:theme"])
@router.post("/sync")
def sync_theme(scope: str = "all"):
    env = os.environ.copy()
    try:
        env["FIGMA_TOKEN"] = env.get("FIGMA_TOKEN","")
        env["FIGMA_FILE_ID"] = env.get("FIGMA_FILE_ID","")
        env["BRAND_LIST"] = env.get("BRAND_LIST","default,acme,greenfield")
        subprocess.check_call(["node","scripts/sync-figma-tokens.js"], env=env, cwd="/app")
    except subprocess.CalledProcessError as e:
        raise HTTPException(500, f"Sync failed: {e}")
    ts = time.strftime("%Y%m%d-%H%M%S"); snap_dir = f"/app/packages/theme/snapshots/{ts}"
    os.makedirs(snap_dir, exist_ok=True)
    shutil.copy("/app/packages/theme/src/tokens.generated.ts", snap_dir)
    shutil.copy("/app/packages/theme/src/css-variables.css", snap_dir)
    return {"ok": True, "snapshot": ts}
