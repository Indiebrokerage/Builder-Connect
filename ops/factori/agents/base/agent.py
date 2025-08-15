import os, sys, json, requests
API = os.environ.get("API_BASE","http://backend:8000")

def http(method, path, **kw):
    r = requests.request(method, f"{API}{path}", timeout=60, **kw)
    r.raise_for_status()
    if "application/json" in r.headers.get("content-type",""):
        return r.json()
    return {"status": r.status_code, "text": r.text}

def handler_bidsheet_refresh(p): return http("POST", f"/v1/bid_sheet/{p.get('project_id','demo')}/rebuild")
def handler_theme_sync(p): return http("POST", "/v1/admin/theme/sync", json={"scope": "all"})

HANDLERS = {
  "agent.bidsheet_refresh": handler_bidsheet_refresh,
  "agent.theme_sync": handler_theme_sync,
}

if __name__ == "__main__":
    event = json.loads(sys.stdin.read() or "{}")
    node_id = event.get("node_id")
    payload = event.get("payload", {})
    fn = HANDLERS.get(node_id, lambda p: {"ok": True, "noop": node_id})
    try:
        out = fn(payload)
        print(json.dumps({"ok": True, "result": out}))
    except Exception as e:
        print(json.dumps({"ok": False, "error": str(e)}))
        sys.exit(2)
