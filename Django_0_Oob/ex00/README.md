# Exercise 00 - Générateur de CV avec Template

## 🎯 Objectif
Créer un générateur de CV qui remplace les variables `{variable}` d'un fichier `.template` par des valeurs définies dans `settings.py`.

## 📋 Fichiers
- `render.py` - Script Python qui génère le fichier HTML
- `settings.py` - Fichier de configuration avec les variables
- `myCV.template` - Template du CV avec variables
- `myCV.html` - Généré automatiquement

## 🚀 Utilisation

### Avec Docker
```bash
cd Django_0_Oob
make ex00
```

### En local
```bash
cd Django_0_Oob/ex00

# 1. Générer le CV HTML
python3 render.py myCV.template

# 2. Ouvrir le fichier
cat myCV.html
```

## ✅ Fonctionnalités
- ✅ Parse les variables `{name}`, `{firstname}`, `{age}`, `{profession}` du template
- ✅ Remplace par les valeurs du settings.py
- ✅ Gère les erreurs (fichier manquant, mauvaise extension, etc.)
- ✅ Génère un fichier `.html` correspondant

## 📝 Exemple

### settings.py
```python
name = "duoquadragintian"
```

### file.template
```html
<p>-Who are you?
-& {name}!*</p>
```

### Commande
```bash
python3 render.py file.template
```

### file.html (résultat)
```html
<p>-Who are you?
-& duoquadragintian!*</p>
```

## 🎓 Concepts
- Regex pour trouver les variables
- Lecture/écriture de fichiers
- Gestion d'erreurs
- Import dynamique (settings.py)

