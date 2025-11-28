# Exercice 00 - Bit.ly Resolver

## 🎯 Objectif
Créer un script shell qui affiche l'adresse réelle d'une URL bit.ly.

## 📋 Fichier à créer
`myawesomescript.sh`

## 🚀 Commandes

### 1. Lancer le conteneur Docker
```bash
cd Django_0_Initiation
make ex00
```

### 2. Dans un autre terminal, entrer dans le conteneur
```bash
cd Django_0_Initiation/ex00
docker compose exec app bash
```

### 3. Tester le script
```bash
chmod +x myawesomescript.sh
./myawesomescript.sh https://bit.ly/1O72s3U
```

### 4. Arrêter le conteneur
```bash
# Dans le terminal où il tourne: Ctrl+C
# Ou dans un autre terminal:
cd Django_0_Initiation && make clean
```

## ✅ Code du script
```bash
#!/bin/sh

if [ -z "$1" ]; then
  echo "Usage: $0 <bit.ly_url>"
  exit 1
fi

curl -L -s -w "%{url_effective}\n" -o /dev/null "$1"
```

## 💻 Commandes rapides
```bash
make test           # Lancer le test automatique
make shell          # Ouvrir un bash dans le conteneur
make logs           # Voir les logs
```

---
