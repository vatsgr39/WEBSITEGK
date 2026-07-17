# SOURCE TWIN AI

Explainable supplier risk, should-cost and sourcing-scenario digital twin for manufacturing. This repository is an executable foundation and demonstration vertical slice—not a claim that every enterprise module is complete.

## Implemented

- Responsive dark/light executive Control Tower with spend, quality, risk, RFQ and action views
- Demonstration award workflow for `RFQ-2026-001`, including a 70/30 dual-source recommendation
- Deterministic, cited Copilot explanation that operates without an LLM key
- Decimal should-cost, normalized supplier-risk, disruption-cost, award-score and seeded Monte Carlo engines
- FastAPI health, readiness, metrics, dashboard, risk, scenario and recommendation endpoints
- PostgreSQL/pgvector schema covering core records, versioned methodologies and audit history
- Deterministic synthetic generator for 30 suppliers, 100 components, 8 commodities, 5 programs and 10 RFQs
- Docker Compose, non-root images, CI, fixed-value calculation tests and security configuration examples

## Architecture

`Next.js/Vinext UI → FastAPI REST → PostgreSQL 16 + pgvector`. Calculation services are pure, deterministic functions using `Decimal`; stored inputs and model versions make results reproducible. LLM providers are optional presentation adapters and cannot replace calculation services.

## Local start

```bash
cp .env.example .env
docker compose up --build
```

Open `http://localhost:3000`; API docs are at `http://localhost:8000/docs`.

Demo users use the local-only password `SourceTwinDemo!2026`: `admin`, `manager`, `buyer`, `analyst`, `executive`, or `supplier` followed by `@sourcetwin.demo`. Replace all demo credentials and `JWT_SECRET` outside development.

## Development and verification

```bash
pnpm install
pnpm build
cd backend && python -m pytest -q
docker compose build
docker compose exec backend python -m app.seed
```

The initial migration is mounted into PostgreSQL automatically. Reset local data with `docker compose down -v` (destructive to the local demo database only), then start again. Backup with `pg_dump`; restore with `psql` against the `source_twin` database.

## API summary

- `GET /health`, `/ready`, `/metrics`
- `GET /api/v1/dashboard`
- `POST /api/v1/risk/calculate`
- `POST /api/v1/scenarios/disruption`
- `GET /api/v1/rfqs/RFQ-2026-001/recommendation`

## Known limitations

The current repository is a strong runnable foundation and high-fidelity demonstration slice. Full CRUD for every normalized table, JWT rotation persistence, upload/import pipelines, PDF/XLSX exports, complete RBAC middleware, production LLM adapters, every requested route, and browser E2E coverage remain development milestones. The UI currently uses seeded presentation data while API integration is the next step.

See [architecture](docs/architecture.md), [methodologies](docs/risk-methodology.md), [security](SECURITY.md), and the [demo walkthrough](docs/demo-walkthrough.md).
