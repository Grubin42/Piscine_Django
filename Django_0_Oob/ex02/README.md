# Exercise 02 - 5 Classes 1 Cup

## 🎯 Objectif
Créer une hiérarchie de 5 classes pour représenter différentes boissons chaudes avec des descriptions.

## 📋 Fichier
- `beverages.py` - Contient toutes les classes de boissons

## 🚀 Utilisation

### Avec Docker
```bash
cd Django_0_Oob
make ex02
```

### En local
```bash
cd Django_0_Oob/ex02
python3 beverages.py
```

## ✅ Hiérarchie des classes

### HotBeverage (classe de base)
**Attributs:**
- `price = 0.30`
- `name = "hot beverage"`

**Méthodes:**
- `description()`: Retourne `"Just some hot water in a cup."`
- `__str__()`: Affiche le format:
  ```
  name : <name>
  price : <price (2 décimales)>
  description : <description>
  ```

### Coffee (hérite de HotBeverage)
**Attributs:**
- `name = "coffee"`
- `price = 0.40`

**Méthodes:**
- `description()`: Retourne `"A coffee, to stay awake."`

### Tea (hérite de HotBeverage)
**Attributs:**
- `name = "tea"`
- `price = 0.30`

**Méthodes:**
- `description()`: Retourne `"Just some hot water in a cup."`

### Chocolate (hérite de HotBeverage)
**Attributs:**
- `name = "chocolate"`
- `price = 0.50`

**Méthodes:**
- `description()`: Retourne `"Chocolate, sweet chocolate..."`

### Cappuccino (hérite de HotBeverage)
**Attributs:**
- `name = "cappuccino"`
- `price = 0.45`

**Méthodes:**
- `description()`: Retourne `"Un po' di Italia nella sua tazza!"`

## 📤 Résultat attendu
```
name : hot beverage
price : 0.30
description : Just some hot water in a cup.

name : coffee
price : 0.40
description : A coffee, to stay awake.

name : tea
price : 0.30
description : Just some hot water in a cup.

name : chocolate
price : 0.50
description : Chocolate, sweet chocolate...

name : cappuccino
price : 0.45
description : Un po' di Italia nella sua tazza!
```

## 🎓 Concepts
- **Héritage**: Les 4 classes dérivées héritent de HotBeverage
- **Surcharge de méthodes**: Chaque sous-classe redéfinit `description()`
- **DRY (Don't Repeat Yourself)**: Ne redéfinir que ce qui change
- **Polymorphisme**: Chaque classe a sa propre `description()`
- **Formatage**: `:.2f` pour limiter à 2 décimales
