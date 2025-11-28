.PHONY: help ex00 ex01 ex02 ex03 ex04 ex05 ex06 clean clean-all

help:
	@echo "=========================================="
	@echo "Exercices Django_0_Oob"
	@echo "=========================================="
	@echo ""
	@echo "Usage: make ex00, make ex01, etc"
	@echo ""
	@echo "Ports d'accès:"
	@echo "  ex00: http://localhost:9000"
	@echo "  ex01: http://localhost:9001"
	@echo "  ex02: http://localhost:9002"
	@echo "  ex03: http://localhost:9003"
	@echo "  ex04: http://localhost:9004"
	@echo "  ex05: http://localhost:9005"
	@echo "  ex06: http://localhost:9006"
	@echo ""
	@echo "Commandes:"
	@echo "  make ex00-06     - Lance exercice XX"
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

clean:
	cd ex00 && docker compose down || true
	cd ex01 && docker compose down || true
	cd ex02 && docker compose down || true
	cd ex03 && docker compose down || true
	cd ex04 && docker compose down || true
	cd ex05 && docker compose down || true
	cd ex06 && docker compose down || true

clean-all: clean
	docker system prune -f

.DEFAULT_GOAL := help

