# Exercise 04 - Classe Elem pour HTML

## 🎯 Objectif
Créer une classe `Elem` capable de représenter n'importe quel élément HTML avec ses attributs et son contenu.

## 📋 Fichiers
- `elem.py` - Contient les classes `Text` et `Elem`
- `tests.py` - Tests fournis pour vérifier les fonctionnalités

## 🚀 Utilisation

### Avec Docker
```bash
cd Django_0_Oob
make ex04
```

### En local
```bash
cd Django_0_Oob/ex04
python3 elem.py      # Voir un exemple
python3 tests.py     # Lancer les tests
```

## ✅ Classe Text

Hérite de `str` et ajoute:
- Échappement des caractères HTML: `<`, `>`, `"`, `&`
- Remplacement des `\n` par `\n<br />\n`

## ✅ Classe Elem

### Constructeur
```python
Elem(tag='div', attr={}, content=None, tag_type='double')
```

**Paramètres:**
- `tag` (str): Nom de la balise HTML
- `attr` (dict): Attributs HTML
- `content`: Contenu (Text, Elem, liste, ou None)
- `tag_type` (str): `'double'` (balises ouvrantes/fermantes) ou `'simple'` (balises auto-fermantes)

### Méthodes
- `__str__()`: Retourne le code HTML complet
- `add_content(content)`: Ajoute du contenu (Text, Elem, ou liste)
- `check_type(content)`: Vérifie que le contenu est valide (statique)

### Exception
- `Elem.ValidationError`: Levée si le contenu n'est pas valide

## 📝 Exemple

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

print(elem)
```

### Résultat
```html
<html>
  <head>
    <title>
      Hello ground!
    </title>
  </head>
  <body>
    <h1>
      Oh no, not again!
    </h1>
    <img src="http://i.imgur.com/pfp3T.jpg" />
  </body>
</html>
```

## 🎓 Concepts
- Classes et héritage
- Représentation HTML en Python
- Validation de contenu
- Indentation automatique
- Échappement HTML

