.PHONY: up down clean logs

up:
	docker compose up -d
	@echo "✅ Exercice 04 lancé sur http://localhost:8004"
	@echo "📄 Ouvrez votre navigateur et allez à http://localhost:8004/snippets.html"

down:
	docker compose down

clean:
	docker compose down

logs:
	docker compose logs -f

.DEFAULT_GOAL := up

