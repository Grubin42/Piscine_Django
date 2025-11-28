# Exercice 01 - CV en HTML/CSS

## 🎯 Objectif
Créer un CV en HTML/CSS respectant des contraintes spécifiques de sémantique et de mise en forme.

## 📋 Fichier à créer
`cv.html`

## ✅ Contraintes obligatoires

**Contenu:**
- ✅ Titre `<title>` et titre `<h1>`
- ✅ Nom, prénom, compétences, parcours
- ✅ Au moins 1 tableau avec `<table>`, `<th>`, `<tr>`, `<td>`
- ✅ Au moins 1 liste `<ul>` et 1 liste `<ol>` avec `<li>`

**Mise en forme:**
- ✅ Bordures tableaux: visibles (solid) + fusionnées (collapse)
- ✅ Cellule bas-droit de chaque tableau: couleur bordure `#424242`
- ✅ Bordures tableaux dans balise `<style>` du `<head>`
- ✅ Couleur cellule bas-droit dans attribut `style` inline

**Général:**
- ✅ Sémantique HTML respectée
- ✅ Séparation fond (HTML) et forme (CSS)

## 🚀 Commandes

### 1. Lancer le conteneur
```bash
cd Django_0_Initiation
make ex01
```

### 2. Dans un autre terminal
```bash
cd Django_0_Initiation/ex01
```

### 3. Ouvrir dans le navigateur
```
http://localhost:8001/cv.html
```

### 4. Éditer et voir les changements en live
Les modifications à `cv.html` s'affichent automatiquement au rafraîchissement!

### 5. Arrêter
```bash
cd Django_0_Initiation && make clean
```

## 📝 Structure minimale

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Mon CV</title>
    <style>
      /* Bordures tableaux ici */
      table {
        border-collapse: collapse;
      }
      table th, table td {
        border: 1px solid black;
      }
    </style>
  </head>
  <body>
    <h1>Mon Nom</h1>
    
    <!-- Tableau 1 -->
    <table>
      <tr>
        <th>Col1</th>
        <th>Col2</th>
        <th>Col3</th>
      </tr>
      <tr>
        <td>Data</td>
        <td>Data</td>
        <td style="border-color: #424242;">Data</td>
      </tr>
    </table>
    
    <!-- Liste ul -->
    <ul>
      <li>Item 1</li>
    </ul>
    
    <!-- Liste ol -->
    <ol>
      <li>Item 1</li>
    </ol>
  </body>
</html>
```

## 💻 Commandes rapides
```bash
make up      # Lancer le conteneur
make down    # Arrêter
make logs    # Voir les logs
```

---

**Prêt?** Lance `make ex01` et commence! 🚀

