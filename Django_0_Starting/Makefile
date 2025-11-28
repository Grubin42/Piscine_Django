.PHONY: help ex00 ex01 ex02 ex03 ex04 ex05 ex06 ex07 clean clean-all

help:
	@echo "=========================================="
	@echo "Exercices Django_0_Starting"
	@echo "=========================================="
	@echo ""
	@echo "Usage: make ex00, make ex01, etc"
	@echo ""
	@echo "Ports d'accès:"
	@echo "  ex00: http://localhost:10000"
	@echo "  ex01: http://localhost:10001"
	@echo "  ex02: http://localhost:10002"
	@echo "  ex03: http://localhost:10003"
	@echo "  ex04: http://localhost:10004"
	@echo "  ex05: http://localhost:10005"
	@echo "  ex06: http://localhost:10006"
	@echo "  ex07: http://localhost:10007"
	@echo ""
	@echo "Commandes:"
	@echo "  make ex00-07     - Lance exercice XX"
	@echo "  make clean       - Arrête tous les conteneurs"
	@echo "  make clean-all   - Arrête et nettoie les images"

ex00:
	cd ex00 && docker compose up

ex01:
	cd ex01 && docker compose up

ex02:
	cd ex02 && docker compose up

ex03:
	cd ex03 && docker compose up

ex04:
	cd ex04 && docker compose up

ex05:
	cd ex05 && docker compose up

ex06:
	cd ex06 && docker compose up

ex07:
	cd ex07 && docker compose up

clean:
	cd ex00 && docker compose down || true
	cd ex01 && docker compose down || true
	cd ex02 && docker compose down || true
	cd ex03 && docker compose down || true
	cd ex04 && docker compose down || true
	cd ex05 && docker compose down || true
	cd ex06 && docker compose down || true
	cd ex07 && docker compose down || true

clean-all: clean
	docker system prune -f

.DEFAULT_GOAL := help

