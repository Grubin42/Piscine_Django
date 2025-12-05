# Exercice 03 - Recherche par clé

## 🎯 Objectif
Créer un script Python qui prend le nom d'un état en argument et affiche sa capitale.

## 📋 Fichier à créer
`capital_city.py`

## ✅ Consignes

- ✅ Prendre un état en argument (ex: Oregon)
- ✅ Afficher sa capitale (ex: Salem)
- ✅ Si argument invalide → afficher "Unknown state"
- ✅ Si 0 ou trop d'arguments → ne rien faire et quitter
- ✅ Utiliser `import sys` pour accéder aux arguments
- ✅ Aucun code dans le scope global
- ✅ Fonction appelée dans `if __name__ == '__main__':`

## 📤 Comportement attendu

```bash
# Valide - affiche la capitale
$ python3 capital_city.py Oregon
Salem

# État invalide
$ python3 capital_city.py Ile-De-France
Unknown state

# Pas d'arguments - ne rien faire
$ python3 capital_city.py

# Trop d'arguments - ne rien faire
$ python3 capital_city.py Oregon Alabama
```

## 📝 Dictionnaires à utiliser

```python
states = {
    "Oregon": "OR",
    "Alabama": "AL",
    "New Jersey": "NJ",
    "Colorado": "CO"
}

capital_cities = {
    "OR": "Salem",
    "AL": "Montgomery",
    "NJ": "Trenton",
    "CO": "Denver"
}
```

## 🔍 Logique

1. Vérifier que le nombre d'arguments = exactement 1
2. Récupérer l'état en argument: `sys.argv[1]`
3. Chercher le code de l'état dans le dictionnaire `states`
4. Chercher la capitale avec ce code dans `capital_cities`
5. Afficher la capitale ou "Unknown state"

## 🚀 Commandes Docker

### 1. Lancer le conteneur
```bash
cd Django_0_Starting
make ex03
```

### 2. Dans un autre terminal, exécuter le script
```bash
cd Django_0_Starting/ex03
docker compose exec app bash

# Tester les cas
python3 capital_city.py Oregon
python3 capital_city.py Ile-De-France
python3 capital_city.py
```

### 3. Arrêter le conteneur
```bash
cd Django_0_Starting && make clean
```

## 💻 Commandes rapides
```bash
make up         # Lancer le conteneur
make down       # Arrêter
make shell      # Ouvrir un bash
make logs       # Voir les logs
```

## 📝 Structure du fichier

```python
import sys


def capital_city():
    # Vérifier le nombre d'arguments
    if len(sys.argv) != 2:
        return
    
    # Dictionnaires
    states = { ... }
    capital_cities = { ... }
    
    # Récupérer l'argument
    state_name = sys.argv[1]
    
    # Chercher dans les dictionnaires
    if state_name in states:
        state_code = states[state_name]
        if state_code in capital_cities:
            print(capital_cities[state_code])
    else:
        print("Unknown state")


if __name__ == '__main__':
    capital_city()
```

## 💡 Points clés

- `sys.argv[0]` = nom du script
- `sys.argv[1]` = premier argument
- `len(sys.argv)` = nombre total d'arguments (incluant le script)
- Chercher dans deux dictionnaires
- Imprimer seulement s'il y a exactement 1 argument

---

**Prêt?** Lance `make ex03` et commence! 🚀

