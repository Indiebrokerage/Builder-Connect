# Real Estate Conduit — Factory AI **1‑Click Deploy** Repository

This repo is ready for **Factory AI** and single‑VM **docker‑compose**. It includes:
- Factory graphs (full + demo), agent, and a one‑click script
- FastAPI backend (theme sync, SOW, Change Orders, Payments, Vendors, Exports CSV/XLSX/PDF)
- Next.js web app with multi‑brand + dark mode (token‑driven)
- Figma → tokens pipeline (works with or without Figma creds)
- Seed data + a smoke test script
- Prod helpers: Caddy HTTPS reverse proxy + optional Postgres

## One‑click (local/dev)
```bash
# (Optional) set env
export FACTORY_API=https://factory.yourdomain.com
export FACTORY_TOKEN=YOUR_FACTORY_TOKEN
export FIGMA_TOKEN=YOUR_FIGMA_TOKEN
export FIGMA_FILE_ID=YOUR_FIGMA_FILE_ID
export BRAND_LIST="default,acme,greenfield"

./bin/oneclick.sh           # registers full graph; add --demo or --no-docker
```

## Single‑VM deploy (compose + HTTPS)
```bash
# On the VM
curl -fsSL https://get.docker.com | sh
sudo usermod -aG docker $USER && newgrp docker

cp deploy/.env.prod.example .env   # fill values
docker compose -f docker-compose.yml -f deploy/docker-compose.prod.yml up -d --build

API_BASE=http://localhost:8000 ./scripts/smoke.sh
```

Built: 2025-08-14T23:51:44.349584Z
