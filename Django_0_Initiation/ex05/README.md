# Exercice 05 - Validation W3C

## 🎯 Objectif
Corriger le fichier `index.html` pour passer la validation W3C (aucune erreur, aucun warning).

## 📋 Erreurs trouvées par W3C Validator

### Erreurs critiques

1. **Manque `<!DOCTYPE html>`** 
   - Ligne 1
   - Cause: Pas de déclaration du type de document
   - ✅ Correction: Ajout du DOCTYPE au début

2. **Caractère invalide pour charset**
   - Ligne 3: `charset="fr"`
   - Cause: Seul "UTF-8" est accepté
   - ✅ Correction: `charset="UTF-8"`

3. **Balise `</meta>` fermante invalide**
   - Ligne 3
   - Cause: `<meta>` est une balise auto-fermante
   - ✅ Correction: Suppression de `</meta>`

4. **`<script>` et `<link>` hors de `<head>`**
   - Ligne 1: `<script>` avant `<head>`
   - Ligne 6: `<link>` dans `<body>`
   - ✅ Correction: Déplacement dans `<head>`

5. **Élément `<title>` manquant**
   - Dans `<head>`
   - Cause: Obligatoire en HTML5
   - ✅ Correction: Ajout `<title>Art Gallery Blog</title>`

6. **Mismatch de balises fermantes**
   - Ligne 33: `<h2>...</h1>` (ouvre h2, ferme h1)
   - Ligne 59: Même erreur
   - Ligne 99: `<h1>` au lieu de `<h2>`
   - ✅ Correction: Fermer avec les bonnes balises

7. **Attribut `href` vide**
   - Ligne 33: `href=>`
   - Ligne 107: `href=>`
   - Cause: L'attribut n'a pas de valeur
   - ✅ Correction: `href="#"`

8. **Balises mal imbriquées**
   - Ligne 40: `<b class="article-lead"><p>...` (b contient p)
   - Cause: Structure invalide
   - ✅ Correction: `<p><b class="article-lead">...`

9. **Erreurs d'encodage HTML**
   - Ligne 87: `&&raquo;` (double ampersand)
   - Cause: Typo dans l'entité HTML
   - ✅ Correction: `&raquo;`

10. **Typo dans balise fermante**
    - Ligne 81: `</times>` 
    - Cause: La balise est `</time>` pas `</times>`
    - ✅ Correction: `</time>`

11. **Typo dans balise**
    - Ligne 128: `</asside>`
    - Cause: La balise est `</aside>` pas `</asside>`
    - ✅ Correction: `</aside>`

12. **Balise fermante manquante**
    - Ligne 136: `<a href="#">About</></li>`
    - Cause: Manque `</a>` avant `</li>`
    - ✅ Correction: `<a href="#">About</a>`

13. **Balise vide**
    - Ligne 52: `<p class="article-about"></p>` (vide)
    - Ligne 54: Contenu en dehors de la balise
    - ✅ Correction: Déplacement du contenu dans la balise

### Warnings

1. **`type="text/javascript"` inutile**
   - Ligne 1
   - Cause: C'est la valeur par défaut en HTML5
   - ✅ Correction: Suppression de l'attribut

2. **Trailing slash sur balises auto-fermantes**
   - `<meta ... />` et `<link ... />`
   - Cause: N'a aucun effet en HTML5
   - ✅ Correction: Peut rester, mais n'est pas nécessaire

---

## ✅ Validation

### Avant (Erreurs)
- ❌ 18+ Erreurs trouvées
- ⚠️ 2+ Warnings

### Après (Correct)
- ✅ 0 Erreurs
- ✅ 0 Warnings

---

## 🔗 Tester

1. Ouvrez [W3C Validator](https://validator.w3.org/)
2. Uploadez `index.html`
3. Vérifiez: "Document checking completed. No errors or warnings to show."

---

## 📝 Fichiers

- `index.html` - Fichier corrigé (valide W3C)
- `index_original.html` - Fichier original avec erreurs

---

**Exercice 05 - Terminé!** ✅