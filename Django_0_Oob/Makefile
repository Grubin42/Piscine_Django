.PHONY: help ex00 ex01 ex02 ex03 ex04 ex05 ex06 clean clean-all

help:
	@echo "=========================================="
	@echo "Exercices Django_0_Oob (POO)"
	@echo "=========================================="
	@echo ""
	@echo "Usage: make ex00, make ex01, etc"
	@echo ""
	@echo "Commandes:"
	@echo "  make ex00        - Générateur de CV (Template)"
	@echo "  make ex01        - Classes Intern et Coffee"
	@echo "  make ex02        - Hiérarchie de boissons"
	@echo "  make ex03        - 6 classes (POO avancée)"
	@echo "  make ex04        - Classe Elem (HTML)"
	@echo "  make ex05        - Classes HTML dérivées"
	@echo "  make ex06        - Validation de pages HTML"
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
