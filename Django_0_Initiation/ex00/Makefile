.PHONY: up down test shell clean

up:
	docker compose up -d
	@echo "✅ Conteneur lancé"

down:
	docker compose down

test:
	docker compose run --rm app bash -c "chmod +x /app/myawesomescript.sh && /app/myawesomescript.sh bit.ly/xyz123"

shell:
	docker compose run --rm app bash

clean:
	docker compose down

.DEFAULT_GOAL := up

