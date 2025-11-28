.PHONY: up down clean logs

up:
	docker compose up -d
	@echo "✅ Exercice 03 lancé sur http://localhost:8003"
	@echo "📄 Ouvrez votre navigateur et allez à http://localhost:8003/copy.html"

down:
	docker compose down

clean:
	docker compose down

logs:
	docker compose logs -f

.DEFAULT_GOAL := up

