FROM ubuntu:22.04

# Installer les outils requis pour l'exercice
RUN apt-get update && apt-get install -y \
    curl \
    grep \
    coreutils \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Shell par défaut
CMD ["/bin/bash"]

