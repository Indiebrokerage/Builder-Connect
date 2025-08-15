#!/usr/bin/env bash
set -euo pipefail
if ! command -v docker >/dev/null 2>&1; then curl -fsSL https://get.docker.com | sh; fi
docker compose -f docker-compose.yml -f deploy/docker-compose.prod.yml up -d --build
API_BASE=http://localhost:8000 ./scripts/smoke.sh || true
