# Exercice 04 - Recherche par valeur

## 🎯 Objectif
Créer un script Python qui prend le nom d'une capitale en argument et affiche son état.

## 📋 Fichier à créer
`state.py`

## ✅ Consignes

- ✅ Prendre une capitale en argument (ex: Salem)
- ✅ Afficher son état (ex: Oregon)
- ✅ Si argument invalide → afficher "Unknown capital city"
- ✅ Si 0 ou trop d'arguments → ne rien faire et quitter
- ✅ Utiliser `import sys` pour accéder aux arguments
- ✅ Aucun code dans le scope global
- ✅ Fonction appelée dans `if __name__ == '__main__':`

## 📤 Comportement attendu

```bash
# Valide - affiche l'état
$ python3 state.py Salem
Oregon

# Capitale invalide
$ python3 state.py Paris
Unknown capital city

# Pas d'arguments - ne rien faire
$ python3 state.py

# Trop d'arguments - ne rien faire
$ python3 state.py Salem Colorado
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

## 🔍 Logique (INVERSE d'ex03)

1. Vérifier que le nombre d'arguments = exactement 1
2. Récupérer la capitale en argument
3. **Chercher la capitale dans `capital_cities.values()`**
4. **Trouver l'état correspondant via `states`**
5. Afficher l'état ou "Unknown capital city"

## 🚀 Commandes Docker

### 1. Lancer le conteneur
```bash
cd Django_0_Starting
make ex04
```

### 2. Dans un autre terminal, exécuter le script
```bash
cd Django_0_Starting/ex04
docker compose exec app bash

# Tester les cas
python3 state.py Salem
python3 state.py Paris
python3 state.py
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


def state():
    # Vérifier le nombre d'arguments
    if len(sys.argv) != 2:
        return
    
    # Dictionnaires
    states = { ... }
    capital_cities = { ... }
    
    # Récupérer l'argument
    capital_name = sys.argv[1]
    
    # Chercher la capitale dans capital_cities
    # Boucler pour trouver le code correspondant
    state_code = None
    for code, capital in capital_cities.items():
        if capital == capital_name:
            state_code = code
            break
    
    # Si capitale trouvée, chercher l'état
    if state_code:
        for state_name, code in states.items():
            if code == state_code:
                print(state_name)
    else:
        print("Unknown capital city")


if __name__ == '__main__':
    state()
```

## 💡 Points clés

- **C'est l'inverse d'ex03** (chercher par valeur au lieu de par clé)
- Utiliser `.items()` pour parcourir le dictionnaire
- Chercher la capitale dans les **valeurs** du dictionnaire `capital_cities`
- Le fichier s'appelle `state.py` (pas `capital_city.py`)
- Message d'erreur: "Unknown capital city" (pas "Unknown state")
- Important: boucler deux fois si nécessaire (une fois pour trouver le code, une fois pour trouver l'état)

---

**Prêt?** Lance `make ex04` et commence! 🚀

