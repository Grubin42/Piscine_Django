.PHONY: help ex00 ex01 ex02 ex03 ex04 ex05 clean clean-all

help:
	@echo "=========================================="
	@echo "Exercices Django_0_Initiation"
	@echo "=========================================="
	@echo ""
	@echo "Usage: make ex00, make ex01, etc"
	@echo ""
	@echo "Ports d'accès:"
	@echo "  ex00: Shell interactif"
	@echo "  ex01: http://localhost:8001"
	@echo "  ex02: http://localhost:8002"
	@echo "  ex03: http://localhost:8003"
	@echo "  ex04: http://localhost:8004"
	@echo "  ex05: http://localhost:8005"
	@echo ""
	@echo "Commandes:"
	@echo "  make ex00        - Lance exercice 00"
	@echo "  make ex01        - Lance exercice 01"
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

clean:
	cd ex00 && docker compose down || true
	cd ex01 && docker compose down || true
	cd ex02 && docker compose down || true
	cd ex03 && docker compose down || true
	cd ex04 && docker compose down || true
	cd ex05 && docker compose down || true

clean-all: clean
	docker system prune -f

.DEFAULT_GOAL := help

