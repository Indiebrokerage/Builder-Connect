#!/usr/bin/env bash
set -euo pipefail
API_BASE="${API_BASE:-http://localhost:8000}"
OUT="${OUT:-./smoke_artifacts}"
mkdir -p "$OUT"
echo "==> healthz"; curl -fsS "$API_BASE/healthz" | tee "$OUT/healthz.json"
echo "==> vendors"; curl -fsS "$API_BASE/v1/vendors/search?q=lumber" -o "$OUT/vendors_lumber.json"
echo "==> CSV"; curl -fsS "$API_BASE/v1/exports/bidsheet/demo.csv" -o "$OUT/bidsheet_demo.csv"
echo "==> XLSX"; curl -fsS "$API_BASE/v1/exports/bidsheet/demo.xlsx" -o "$OUT/bidsheet_demo.xlsx"
echo "==> PDF"; curl -fsS "$API_BASE/v1/exports/bidsheet/demo.pdf" -o "$OUT/bidsheet_demo.pdf"
echo "==> SOW"; curl -fsS -X POST "$API_BASE/v1/pdf/sow" -H 'Content-Type: application/json' -d '{"project_id":"demo","scope":"Framing"}' -o "$OUT/sow.pdf"
echo "==> CO"; curl -fsS -X POST "$API_BASE/v1/pdf/change_order" -H 'Content-Type: application/json' -d '{"project_id":"demo","change":"Upgrade shingles"}' -o "$OUT/change_order.pdf"
echo "✅ Done -> $OUT"
