.PHONY: up down clean logs

up:
	docker compose up -d
	@echo "✅ Exercice 02 lancé sur http://localhost:8002"
	@echo "📄 Ouvrez votre navigateur et allez à http://localhost:8002/form.html"

down:
	docker compose down

clean:
	docker compose down

logs:
	docker compose logs -f

.DEFAULT_GOAL := up

