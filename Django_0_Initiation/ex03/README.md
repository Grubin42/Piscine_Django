# Exercice 03 - Reproduction de Page Web

## 🎯 Objectif
Reproduire une page web le plus fidèlement possible en utilisant un fichier CSS fourni (sans le modifier).

## 📋 Fichier à créer
`copy.html`

## ✅ Contraintes

**Fichier CSS:**
- ✅ Utiliser le fichier `style.css` fourni
- ✅ NE PAS modifier ce fichier
- ❌ Une version "fraiche" sera utilisée à la soutenance

**HTML:**
- ✅ Respecter la sémantique des balises
- ✅ Séparer fond et forme
- ✅ Reproduire le screenshot le plus fidèlement possible

## 📦 Fichiers fournis

Vous devez avoir:
- `style.css` - Fichier CSS (fourni, à ne pas modifier)
- `screenshot.png` ou image de référence (le design à reproduire)

## 🚀 Commandes

```bash
# 1. Lancer ex03
cd Django_0_Initiation
make ex03

# 2. Ouvrir navigateur
# http://localhost:8003/copy.html

# 3. Comparer avec le screenshot fourni
# Ajuster votre HTML pour correspondre

# 4. Arrêter
make clean
```

## 📝 Structure minimale

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Page Web</title>
    <link rel="stylesheet" href="style.css">
  </head>
  <body>
    <!-- Reproduire la structure HTML du screenshot -->
    <!-- Utiliser les bonnes classes/IDs du CSS fourni -->
  </body>
</html>
```

## 💡 Astuces

1. **Ouvrez le screenshot** et le navigateur côte à côte
2. **Inspirez-vous du CSS**: Les classes du fichier `style.css` vous indiquent la structure
3. **Comparez pixel par pixel** les couleurs, espacements, typographies
4. **Validez au fur et à mesure** avec le navigateur

## ✨ Résultat

Votre `copy.html` + `style.css` doit produire une page identique au screenshot! 🎯

---

**Prêt?** Lance `make ex03` et commence! 🚀

