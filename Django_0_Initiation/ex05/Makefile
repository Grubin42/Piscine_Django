.PHONY: up down clean logs

up:
	docker compose up -d
	@echo "✅ Exercice 05 lancé sur http://localhost:8005"
	@echo "📄 Ouvrez votre navigateur et allez à http://localhost:8005/index.html"

down:
	docker compose down

clean:
	docker compose down

logs:
	docker compose logs -f

.DEFAULT_GOAL := up

