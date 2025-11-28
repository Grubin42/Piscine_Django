.PHONY: up down clean logs

up:
	docker compose up -d
	@echo "✅ Exercice 03 lancé sur http://localhost:9003"

down:
	docker compose down

clean:
	docker compose down

logs:
	docker compose logs -f

.DEFAULT_GOAL := up

