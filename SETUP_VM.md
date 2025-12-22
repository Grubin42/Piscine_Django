# 🖥️ Guide Complet - Configuration VM pour la Piscine Django

**Objectif**: Créer une machine virtuelle portable pour présenter les exercices Django à l'école.

---

## 📋 Table des matières

1. [Prérequis](#prérequis)
2. [Étape 1: Créer la VM VirtualBox](#étape-1-créer-la-vm-virtualbox)
3. [Étape 2: Installer Ubuntu](#étape-2-installer-ubuntu)
4. [Étape 3: Installer Docker](#étape-3-installer-docker)
5. [Étape 4: Installer Git](#étape-4-installer-git)
6. [Étape 5: Cloner le repo](#étape-5-cloner-le-repo)
7. [Étape 6: Tester les exercices](#étape-6-tester-les-exercices)
8. [Étape 7: Exporter la VM](#étape-7-exporter-la-vm)
9. [À l'école - Utiliser la VM](#à-lécole---utiliser-la-vm)
10. [Troubleshooting](#troubleshooting)

---

## 🔧 Prérequis

### Sur votre ordinateur actuel

- **VirtualBox** installé ([virtualbox.org](https://www.virtualbox.org/))
- **Espace disque**: 40 GB libres minimum
- **RAM disponible**: 8 GB (4 GB minimum)
- **Connexion Internet**: Pour télécharger Ubuntu et les images Docker

### Fichiers nécessaires

- Ubuntu 22.04 LTS ISO (téléchargeable gratuitement)
- Git pour cloner le repo
- Terminal/Bash

---

## Étape 1: Créer la VM VirtualBox

### A. Ouvrir VirtualBox

1. Lancer VirtualBox
2. Clic sur le bouton **"Nouvelle"** (ou Ctrl+N)

### B. Configuration de la machine

Remplir les champs avec:

| Champ | Valeur |
|-------|--------|
| **Nom** | `Piscine_Django` |
| **Dossier machine** | Laisser par défaut |
| **Type** | `Linux` |
| **Version** | `Ubuntu (64-bit)` |
| **Mémoire vive** | `4096 MB` (4 GB) ou plus |
| **Disque dur** | `Créer un disque dur virtuel maintenant` |

### C. Configuration du disque dur

- **Type de disque dur**: `VDI (VirtualBox Disk Image)`
- **Stockage**: `Dynamiquement alloué`
- **Taille**: `30 GB` minimum

### D. Démarrer la VM

1. Sélectionner la machine créée
2. Clic sur **"Démarrer"**
3. Une fenêtre s'ouvre

---

## Étape 2: Installer Ubuntu

### A. Sélectionner le fichier ISO

1. Ubuntu vous demande de sélectionner un fichier ISO
2. **Télécharger Ubuntu 22.04 LTS** depuis [ubuntu.com](https://ubuntu.com/download/desktop)
3. Clic sur le bouton dossier 📁
4. Sélectionner le fichier `ubuntu-22.04-desktop-amd64.iso`
5. Clic sur **"Démarrer"**

### B. Installation

1. **Bienvenue**: Clic sur **"Install Ubuntu"**
2. **Clavier**: Garder les paramètres par défaut
3. **Mises à jour et autres logiciels**: 
   - Cocher **"Download updates while installing"**
   - Garder le reste par défaut
4. **Type d'installation**: 
   - Sélectionner **"Erase disk and install Ubuntu"**
   - Clic sur **"Continue"**
5. **Localisation**: Sélectionner votre pays
6. **Compte utilisateur**:
   - **Nom d'ordinateur**: `piscine-django`
   - **Nom d'utilisateur**: `student` (ou votre nom)
   - **Mot de passe**: `piscine42` (ou un mot de passe fort)
   - ✅ Cocher **"Log in automatically"**
7. Clic sur **"Continue"**

L'installation prend **10-15 minutes**. ⏳

### C. Redémarrage

Une fois l'installation terminée, la VM redémarre automatiquement. 
Appuyer sur **Entrée** si demandé.

---

## Étape 3: Installer Docker

### A. Ouvrir un terminal

1. Dans Ubuntu, appuyer sur **Ctrl+Alt+T** pour ouvrir un terminal
2. Ou cliquer sur l'icône "Terminal" dans le menu

### B. Mettre à jour le système

```bash
sudo apt update
sudo apt upgrade -y
```

### C. Installer Docker

```bash
sudo apt install -y docker.io
```

### D. Configurer Docker (optionnel mais recommandé)

Pour utiliser Docker sans `sudo`:

```bash
sudo usermod -aG docker $USER
newgrp docker
```

### E. Vérifier l'installation

```bash
docker --version
docker run hello-world
```

✅ Vous devriez voir une message "Hello from Docker!"

---

## Étape 4: Installer Git

### A. Installer Git

```bash
sudo apt install -y git
```

### B. Configurer Git

```bash
git config --global user.name "Votre Nom"
git config --global user.email "votre.email@example.com"
```

### C. Vérifier

```bash
git --version
git config --global user.name
```

---

## Étape 5: Cloner le repo

### A. Naviguer au dossier home

```bash
cd ~
```

### B. Cloner le repository

Si le repo est sur GitHub:

```bash
git clone https://github.com/votre-username/Piscine_Django.git
cd Piscine_Django
```

Ou si vous avez un chemin local:

```bash
cp -r /chemin/vers/Piscine_Django ~/Piscine_Django
cd ~/Piscine_Django
```

### C. Vérifier la structure

```bash
ls -la
```

Vous devriez voir:
```
Django_0_Initiation/
Django_0_Oob/
Django_0_Starting/
Makefile (racine)
```

---

## Étape 6: Tester les exercices

### A. Django_0_Initiation

```bash
cd Django_0_Initiation
make help
```

Pour lancer un exercice:

```bash
make ex01
# Ouvrir http://localhost:8001 dans le navigateur
```

### B. Django_0_Starting

```bash
cd ../Django_0_Starting
make help
```

Pour lancer:

```bash
make ex00
# Test dans le même terminal
```

### C. Django_0_Oob

```bash
cd ../Django_0_Oob
make help
```

Pour lancer:

```bash
make ex01
# Test dans le même terminal
```

### D. Arrêter tous les conteneurs

```bash
make clean
```

---

## Étape 7: Exporter la VM

### ⚠️ IMPORTANT pour l'école!

Pour transférer votre VM à l'école facilement:

### A. Arrêter la VM

1. Dans Ubuntu: Clic sur le menu Power → Shutdown
2. Attendez que la VM s'arrête complètement

### B. Exporter en format OVA

1. Dans VirtualBox, clic droit sur la machine
2. Sélectionner **"Export Appliance"**
3. **Format**: `Open Virtualization Format (.ova)`
4. **Fichier**: `Piscine_Django.ova`
5. Clic sur **"Next"** puis **"Export"**

⏳ L'export prend **5-10 minutes** (crée un fichier de ~10 GB)

### C. Sauvegarder le fichier

Copier `Piscine_Django.ova` sur:
- Une clé USB
- Un disque dur externe
- Cloud (Google Drive, Dropbox, etc.)

### D. Snapshot (optionnel mais recommandé)

1. Clic droit sur la machine
2. **"Snapshots"** → **"Prendre un snapshot"**
3. Nommer: `Initial Setup - Working`

---

## À l'école - Utiliser la VM

### A. Importer la VM

1. Sur le PC de l'école, ouvrir VirtualBox
2. Clic sur **"File"** → **"Import Appliance"**
3. Sélectionner `Piscine_Django.ova`
4. Clic sur **"Import"**

⏳ Import: **5-10 minutes**

### B. Démarrer la VM

1. Sélectionner la machine
2. Clic sur **"Start"**

### C. Mettre à jour le code

```bash
cd ~/Piscine_Django
git pull origin main
```

### D. Lancer les exercices

```bash
cd Django_0_Starting
make ex00

# Ou dans un autre terminal:
cd Django_0_Initiation
make ex01
# Ouvrir http://localhost:8001
```

### E. Présenter aux autres élèves

```bash
# Montrer l'interface
make ex01
# http://localhost:8001 dans Firefox/Chrome

# Ou montrer le code:
cat ex01/README.md

# Ou lancer les tests:
cd Django_0_Oob/ex04
python3 tests.py
```

---

## 🔧 Troubleshooting

### Problème 1: "No space left on device"

**Cause**: Disque virtuel trop petit

**Solution**:
```bash
# Vérifier l'espace
df -h

# Ou créer une VM plus grande
```

### Problème 2: Docker not found

**Cause**: Docker pas bien installé

**Solution**:
```bash
sudo apt install -y docker.io
sudo systemctl start docker
docker --version
```

### Problème 3: Permission denied sur docker

**Cause**: Utilisateur pas dans le groupe docker

**Solution**:
```bash
sudo usermod -aG docker $USER
# Redémarrer la VM
sudo reboot
```

### Problème 4: Port already in use

**Cause**: Un service utilise déjà le port

**Solution**:
```bash
# Voir qui utilise le port 8001
sudo lsof -i :8001

# Ou fermer tous les conteneurs
docker stop $(docker ps -a -q)
```

### Problème 5: Cannot connect to Docker daemon

**Cause**: Docker n'est pas démarré

**Solution**:
```bash
sudo systemctl start docker
sudo systemctl enable docker  # Pour démarrer automatiquement
```

### Problème 6: Git: Permission denied

**Cause**: Pas d'accès en lecture/écriture

**Solution**:
```bash
sudo chown -R $USER:$USER ~/Piscine_Django
chmod -R u+w ~/Piscine_Django
```

---

## ✅ Checklist finale

Avant de partir à l'école:

- [ ] VM créée et fonctionnelle
- [ ] Docker installé et testé (`docker run hello-world`)
- [ ] Git configuré et repo cloné
- [ ] Au moins 1 exercice de chaque module testé
  - [ ] Django_0_Initiation/ex01
  - [ ] Django_0_Starting/ex00
  - [ ] Django_0_Oob/ex01
- [ ] VM exportée en `.ova`
- [ ] Fichier `.ova` sauvegardé sur clé USB / cloud
- [ ] README.md mis à jour
- [ ] Snapshot pris

---

## 📚 Ressources utiles

| Ressource | Lien |
|-----------|------|
| VirtualBox | [virtualbox.org](https://www.virtualbox.org/) |
| Ubuntu | [ubuntu.com](https://ubuntu.com) |
| Docker | [docker.com](https://www.docker.com/) |
| Git | [git-scm.com](https://git-scm.com/) |
| Make | `man make` |

---

## 🎯 Résumé workflow

```
┌─────────────────────────────────────────┐
│ 1. Créer VM VirtualBox                  │
└─────────────┬───────────────────────────┘
              │
              ▼
┌─────────────────────────────────────────┐
│ 2. Installer Ubuntu 22.04               │
└─────────────┬───────────────────────────┘
              │
              ▼
┌─────────────────────────────────────────┐
│ 3. Installer Docker + Git               │
└─────────────┬───────────────────────────┘
              │
              ▼
┌─────────────────────────────────────────┐
│ 4. Cloner repo Piscine_Django           │
└─────────────┬───────────────────────────┘
              │
              ▼
┌─────────────────────────────────────────┐
│ 5. Tester les exercices                 │
└─────────────┬───────────────────────────┘
              │
              ▼
┌─────────────────────────────────────────┐
│ 6. Exporter en .ova                     │
└─────────────┬───────────────────────────┘
              │
              ▼
┌─────────────────────────────────────────┐
│ 7. À l'école: Importer + Utiliser       │
└─────────────────────────────────────────┘
```

---

## 🎉 Bravo!

Vous avez maintenant une VM complète pour présenter votre Piscine Django à l'école!

**Questions?** Consultez la section [Troubleshooting](#troubleshooting) ou relancez le guide.

**Bonne présentation!** 🚀

