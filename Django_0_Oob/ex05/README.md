# Exercise 05 - Éléments HTML Dérivés

## 🎯 Objectif
Créer des classes dérivées d'`Elem` pour simplifier la création d'éléments HTML courants.

## 📋 Fichiers
- `elem.py` - Copie de la classe `Elem` et `Text` depuis ex04
- `elements.py` - Définitions de toutes les classes HTML

## ✅ Classes créées

### Structurels
- `Html`
- `Head`
- `Body`

### Titre et métadonnées
- `Title`
- `Meta`

### Images
- `Img`

### Tableaux
- `Table`
- `Tr`
- `Th`
- `Td`

### Listes
- `Ul` (liste non ordonnée)
- `Ol` (liste ordonnée)
- `Li` (élément de liste)

### En-têtes
- `H1`
- `H2`

### Paragraphes
- `P`
- `Div`
- `Span`

### Séparateurs
- `Hr` (ligne horizontale)
- `Br` (saut de ligne)

## 🚀 Utilisation

### Avec Docker
```bash
cd Django_0_Oob
make ex05
```

### En local
```bash
cd Django_0_Oob/ex05
python3 elements.py
```

## 📝 Exemple

### Avant (ex04 - avec Elem directement)
```python
elem = Elem('html', {}, [
    Elem('head', {}, [
        Elem('title', {}, Text('Hello ground!'))
    ]),
    Elem('body', {}, [
        Elem('h1', {}, Text('Oh no, not again!')),
        Elem('img', {'src': 'http://i.imgur.com/pfp3T.jpg'}, tag_type='simple')
    ])
])
```

### Après (ex05 - avec classes dérivées)
```python
page = Html([
    Head([
        Title(Text('Hello ground!'))
    ]),
    Body([
        H1(Text('Oh no, not again!')),
        Img({'src': 'http://i.imgur.com/pfp3T.jpg'}),
    ])
])
```

**Beaucoup plus simple et lisible!** ✨

## 🎓 Concepts
- Héritage de classe
- Réutilisation de code
- API simplifiée
- Composition d'objets

