# Exercice 04 - Snippets JavaScript

## 🎯 Objectif
Créer `snippets.html` qui importe 4 fichiers JavaScript dans le bon ordre pour afficher une popup sans erreur.

## 📋 Fichier à créer
`snippets.html`

## ✅ Fichiers fournis

- `file1.js` - Fonction `unicorn()` 
- `file2.js` - Fonction `cat()` (appelée au chargement)
- `file3.js` - Fonction `whale()`
- `file4.js` - Fonction `puffin()` (affiche la popup)

## 🔗 Chaîne d'appels

```
file2.js: cat() → appelle whale()
file3.js: whale() → appelle unicorn()
file1.js: unicorn() → appelle puffin()
file4.js: puffin() → alert("Exercice réussi!")
```

**Important:** Les fonctions doivent être définies AVANT d'être appelées!

## 🚀 Commandes

```bash
# 1. Lancer ex04
cd Django_0_Initiation
make ex04

# 2. Ouvrir navigateur
# http://localhost:8004/snippets.html

# 3. Vérifier: Une popup "Exercice réussi!" s'affiche ✨

# 4. Arrêter
make clean
```

## 📝 Structure

```html
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>Snippets</title>
</head>
<body>
  <h1>Exercice 04 - Snippets JavaScript</h1>
  
  <!-- Importer DANS LE BON ORDRE -->
  <script src="file4.js"></script>
  <script src="file1.js"></script>
  <script src="file3.js"></script>
  <script src="file2.js"></script>
</body>
</html>
```

## ✨ Résultat

Popup affichant: **"Exercice réussi!"** 🎉

---

**Prêt?** Lance `make ex04`! 🚀

