# Exercise 06 - Validation de Pages HTML

## 🎯 Objectif
Créer une classe `Page` qui valide la structure d'une page HTML selon des règles strictes.

## 📋 Fichiers
- `elem.py` - Classe `Elem` et `Text` (copie depuis ex05)
- `elements.py` - Classes HTML dérivées (copie depuis ex05)
- `Page.py` - Classe de validation des pages HTML

## ✅ Règles de validation

### Éléments valides
`html`, `head`, `body`, `title`, `meta`, `img`, `table`, `tr`, `th`, `td`, `ul`, `ol`, `li`, `h1`, `h2`, `p`, `div`, `span`, `hr`, `br`, `Text`

### Règles spécifiques

- **Html**: Doit contenir exactement un Head, puis un Body (dans cet ordre)
- **Head**: Ne doit contenir qu'un unique Title et uniquement ce Title
- **Body** et **Div**: Doivent contenir uniquement: H1, H2, Div, Table, Ul, Ol, Span, ou Text
- **Title**, **H1**, **H2**, **Li**, **Th**, **Td**: Ne doivent contenir qu'un unique Text et uniquement ce Text
- **P**: Ne doit contenir que des Text
- **Span**: Ne doit contenir que des Text ou des P
- **Ul** et **Ol**: Doivent contenir au moins un Li et uniquement des Li
- **Tr**: Doit contenir au moins un Th ou Td et uniquement des Th ou des Td
  - Les Th et Td doivent être mutuellement exclusifs dans une ligne
- **Table**: Ne doit contenir que des Tr et uniquement des Tr

## 🚀 Utilisation

### Avec Docker
```bash
cd Django_0_Oob
make ex06
```

### En local
```bash
cd Django_0_Oob/ex06
python3 -c "from Page import Page; from elements import *; p = Page(Html([Head([Title(Text('Test'))]), Body([H1(Text('Hello'))])])); print('Valid!' if p.is_valid() else 'Invalid!')"
```

## 📝 Exemple

```python
from Page import Page
from elements import *
from elem import Text

# Créer une page valide
page = Page(Html([
    Head([
        Title(Text('Hello ground!'))
    ]),
    Body([
        H1(Text('Oh no, not again!')),
        Img({'src': 'http://i.imgur.com/pfp3T.jpg'}),
    ])
]))

# Vérifier la validité
if page.is_valid():
    print("✅ Page valide!")
    print(page)  # Affiche le HTML avec DOCTYPE
    page.write_to_file('output.html')  # Écrit dans un fichier
else:
    print("❌ Page invalide!")
```

## 🎓 Concepts
- Validation de structure
- Héritage et polymorphisme
- Récursion
- Règles métier complexes

