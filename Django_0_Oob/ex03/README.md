# Exercise 03 - Glorious Coffee Machine!

## 🎯 Objectif
Créer une machine à café qui sert des boissons aléatoirement, tombe en panne après 10 boissons et doit être réparée.

## 📋 Fichiers
- `machine.py` - Classe `CoffeeMachine` avec exception et classe interne
- `beverages.py` - Copie des classes de boissons depuis ex02

## 🚀 Utilisation

### Avec Docker
```bash
cd Django_0_Oob
make ex03
```

### En local
```bash
cd Django_0_Oob/ex03
python3 machine.py
```

## ✅ Classe CoffeeMachine

### Constructeur
```python
def __init__(self):
    # Initialise la machine
```

### Classe Interne: EmptyCup
Hérite de `HotBeverage`
- `name = "empty cup"`
- `price = 0.90`
- `description()` → `"An empty cup?! Gimme my money back!"`

### Exception Interne: BrokenMachineException
Hérite de `Exception`
- Message: `"This coffee machine has to be repaired."`
- Défini dans le constructeur de l'exception

### Méthode repair()
- Répare la machine
- Réinitialise le compteur de boissons à 0

### Méthode serve(beverage_class)
**Paramètres:**
- `beverage_class`: Une classe dérivée de `HotBeverage`

**Retour:**
- 50% du temps: Instance de la classe passée
- 50% du temps: Instance de `EmptyCup`

**Fonctionnement:**
1. Lève `BrokenMachineException` si machine en panne
2. Incrémente le compteur de boissons
3. Après 10 boissons (11ème appel): marque machine comme cassée
4. Prochaine tentative lève exception
5. Après `repair()`: recommence un nouveau cycle de 10

## 📤 Résultat attendu

```
🔄 Premier cycle - 10 boissons max:
  Boisson 1: coffee
  Boisson 2: cappuccino
  ...
  Boisson 10: chocolate
  ❌ PANNE! This coffee machine has to be repaired.

🔧 Réparation de la machine...
✅ Machine réparée!

🔄 Deuxième cycle - 10 boissons max:
  Boisson 1: cappuccino
  ...
  ❌ PANNE! This coffee machine has to be repaired.
```

## 🎓 Concepts POO

- ✅ **Classes internes** (`EmptyCup`, `BrokenMachineException`)
- ✅ **Héritage** (`EmptyCup` hérite de `HotBeverage`)
- ✅ **Exceptions personnalisées**
- ✅ **État de l'objet** (broken, servings_count)
- ✅ **Aléatoire** avec `random.choice()`
- ✅ **Gestion d'exceptions** en client

## 💡 Points clés

1. **Aléatoire 50/50**: `random.choice([True, False])`
2. **Compteur persistant**: Pas réinitialisé après panne, seulement après `repair()`
3. **Exception au-delà de 10**: La 11ème boisson lève l'exception
4. **Classes internes**: Accessible via `CoffeeMachine.EmptyCup` et `CoffeeMachine.BrokenMachineException`
