lint:
	pre-commit run --a

migrate:
	alembic upgrade head

run:
	uvicorn src.main:app --host 0.0.0.0 --port 8000 --log-level=info
