.PHONY: up down test lint build seed
up:
	docker compose up --build
down:
	docker compose down
test:
	cd backend && pytest -q
	pnpm test
lint:
	pnpm lint
build:
	pnpm build
seed:
	docker compose exec backend python -m app.seed
