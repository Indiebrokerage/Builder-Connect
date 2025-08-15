#!/usr/bin/env bash
set -euo pipefail

GRAPH="full"
DOCKER=1
DEMO=0

while [[ $# -gt 0 ]]; do
  case "$1" in
    --demo) DEMO=1; shift ;;
    --graph) GRAPH="$2"; shift 2 ;;
    --no-docker) DOCKER=0; shift ;;
    *) echo "Unknown arg: $1"; exit 1 ;;
  esac
done

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

echo "==> Installing Node deps for token sync (if any)"
if command -v pnpm >/dev/null 2>&1; then pnpm i || true; else npm i || true; fi

echo "==> Generating tokens (brands: ${BRAND_LIST:-default})"
export BRAND_LIST="${BRAND_LIST:-default}"
# Use Node directly; script tolerates missing Figma creds and emits defaults
node scripts/sync-figma-tokens.js || true

if [[ $DOCKER -eq 1 ]]; then
  echo "==> Starting Docker stack (backend, web, agent)"
  docker compose up -d --build
fi

if [[ -z "${FACTORY_API:-}" || -z "${FACTORY_TOKEN:-}" ]]; then
  echo "==> FACTORY_API or FACTORY_TOKEN missing; skipping Factory registration."
  exit 0
fi

GRAPH_FILE="ops/factori/taskgraph.json"
if [[ "$GRAPH" == "demo" || $DEMO -eq 1 ]]; then
  GRAPH_FILE="ops/factori/taskgraph.demo.json"
fi

echo "==> Registering taskgraph ($GRAPH_FILE)"
curl -sS -X POST "$FACTORY_API/v1/taskgraphs"  -H "Authorization: Bearer $FACTORY_TOKEN"  -H "Content-Type: application/json"  --data-binary @"$GRAPH_FILE" | sed -e 's/.*/[FACTORY]/'

echo "✅ One‑click complete."
