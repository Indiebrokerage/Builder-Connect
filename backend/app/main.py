from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .logging import configure_logging

from .routes import admin_theme, bid_sheet, webhook, exports, sow, change_orders, payments, vendor_catalog, pdf_exports

logger = configure_logging()
app = FastAPI(title="REC API")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

app.include_router(admin_theme.router)
app.include_router(bid_sheet.router)
app.include_router(webhook.router)
app.include_router(exports.router)
app.include_router(sow.router)
app.include_router(change_orders.router)
app.include_router(payments.router)
app.include_router(vendor_catalog.router)
app.include_router(pdf_exports.router)

@app.get("/healthz")
def healthz(): return {"ok": True}
@app.get("/readyz")
def readyz(): return {"ready": True}
