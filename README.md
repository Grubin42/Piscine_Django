# Piscine Django - Structure Docker

Ce projet utilise **Docker** pour isoler et faciliter l'exécution de chaque exercice Django.

## 🚀 Démarrage rapide

### Sur votre Mac M1 (local)

1. **Installez Docker Desktop** (si ce n'est pas déjà fait): [Docker Desktop](https://www.docker.com/products/docker-desktop)

2. **Accédez à un dossier d'exercices**:
```bash
cd Django_0_Initiation
```

3. **Lancez un exercice**:
```bash
make ex00    # Lance exercice 00
make ex01    # Lance exercice 01 sur http://localhost:8001
```

4. **Arrêtez tout**:
```bash
make clean
```

### À l'école (VirtualBox x86)

1. **Installez une VM VirtualBox** avec Ubuntu 22.04 x86_64
2. **Installez Docker** dans la VM:
```bash
sudo apt update && sudo apt install -y docker.io
sudo usermod -aG docker $USER
```

3. **Clonez votre repo**:
```bash
git clone <votre-repo>
cd Django_0_Initiation
```

4. **Lancez un exercice** (exactement pareil qu'à la maison!):
```bash
make ex00
make ex01
```

---

## 📁 Structure

```
Django_0_Initiation/
├── Makefile                 # Makefile principal
├── ex00/
│   ├── Dockerfile           # Image Docker
│   ├── docker-compose.yml   # Config services
│   ├── Makefile             # Commandes rapides
│   └── myawesomescript.sh   # Votre code
├── ex01/
│   ├── Dockerfile
│   ├── docker-compose.yml
│   ├── Makefile
│   └── cv.html              # Votre code
└── ... (ex02 à ex05)
```

---

## 🐳 Comment ça marche?

### Pour les exercices HTML/CSS/JS (ex01-ex05):

```bash
cd Django_0_Initiation/ex01
make up
# Ouvrez http://localhost:8001 dans votre navigateur
```

Un serveur Python HTTP tourne et sert vos fichiers. Changez votre code **sur votre Mac** avec Cursor, le navigateur verra les modifications en temps réel!

### Pour l'exercice shell (ex00):

```bash
cd Django_0_Initiation/ex00
make shell
# Vous êtes maintenant DANS le conteneur avec curl/grep/cut disponibles
```

---

## 📝 Commandes disponibles

### Au niveau racine du projet:
```bash
cd Django_0_Initiation
make help       # Affiche les ports et commandes
make ex00       # Lance ex00
make clean      # Arrête tous les conteneurs
```

### Au niveau de chaque exercice:
```bash
cd Django_0_Initiation/ex01
make up         # Lance le conteneur en arrière-plan
make down       # Arrête le conteneur
make clean      # Arrête et nettoie
make logs       # Voir les logs en temps réel
```

---

## 🎯 Ports utilisés

### Django_0_Initiation:
- ex00: Shell interactif
- ex01: http://localhost:8001
- ex02: http://localhost:8002
- ex03: http://localhost:8003
- ex04: http://localhost:8004
- ex05: http://localhost:8005

### Django_0_Oob:
- ex00-ex06: http://localhost:9000-9006

### Django_0_Starting:
- ex00-ex07: http://localhost:10000-10007

---

## 🔧 Troubleshooting

### Port déjà utilisé?
```bash
# Arrêtez tous les conteneurs
make clean

# Ou spécifiquement
cd ex01 && make down
```

### Voir les logs d'erreur?
```bash
cd ex01 && make logs
```

### Reconstruire l'image?
```bash
cd ex01 && docker-compose build --no-cache
```

---

## ✅ Prêt pour la soutenance?

1. ✅ Tous vos fichiers HTML/CSS/JS/Shell sont dans les bon dossiers
2. ✅ Les `Dockerfile` et `docker-compose.yml` sont versionés dans Git
3. ✅ Testez sur un ordi x86 (ou une VM VirtualBox) avant la soutenance
4. ✅ Commitez et poussez sur Git!

Bonne chance! 🚀

