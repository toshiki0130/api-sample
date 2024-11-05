db_upgrade:
	alembic revision --autogenerate -m "Describe your changes here"
	alembic upgrade head

db_downgrade:
	alembic downgrade -1

re:
	docker compose -f docker-compose.yml down
	docker compose -f docker-compose.yml up --build
prd:
	docker compose -f docker-compose.yml up