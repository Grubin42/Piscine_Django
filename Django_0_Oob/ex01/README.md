# Exercise 01 - Startup Intern

## 🎯 Objectif
Créer une classe `Intern` qui représente un stagiaire avec des méthodes pour faire du café et travailler.

## 📋 Fichier
- `intern.py` - Contient les classes `Intern` et `Coffee`

## 🚀 Utilisation

### Avec Docker
```bash
cd Django_0_Oob
make ex01
```

### En local
```bash
cd Django_0_Oob/ex01
python3 intern.py
```

## ✅ Classe Intern

### Attributs
- `name` (str): Nom du stagiaire
  - Valeur par défaut: `"My name? I'm nobody, an intern, I have no name."`

### Méthodes
- `__str__()`: Retourne le nom du stagiaire
- `work()`: Lève une exception `"I'm just an intern, I can't do that..."`
- `make_coffee()`: Retourne une instance de `Coffee`

## ✅ Classe Coffee

### Méthodes
- `__str__()`: Retourne `"This is the worst coffee you ever tasted."`

## 📤 Résultat attendu
```
Intern 1: My name? I'm nobody, an intern, I have no name.
Intern 2: Mark
Mark's coffee: This is the worst coffee you ever tasted.
Exception caught: I'm just an intern, I can't do that...
```

## 🎓 Concepts
- Classes et constructeurs
- Méthodes `__str__()`
- Exceptions
- Héritage (Coffee comme classe interne)
- Paramètres par défaut

