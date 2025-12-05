# Exercice 05 - Recherche par clé ou par valeur

## 🎯 Objectif
Créer un script Python qui prend une string avec plusieurs expressions séparées par des virgules et identifie si chacune est une capitale, un état, ou aucun des deux.

## 📋 Fichier à créer
`all_in.py`

## ✅ Consignes

- ✅ Prendre une string en argument avec expressions séparées par des virgules
- ✅ Pour chaque expression, déterminer: capitale, état, ou aucun des deux
- ✅ Insensible à la casse (new jersey = New Jersey)
- ✅ Ignorer les espaces blancs en trop (` Trenton ` = Trenton)
- ✅ Si 0 ou trop d'arguments → ne rien faire
- ✅ Si deux virgules d'affilées (`, ,`) → ignorer cette expression (pas afficher la ligne)
- ✅ Utiliser `import sys`
- ✅ Aucun code dans le scope global
- ✅ Fonction appelée dans `if __name__ == '__main__':`

## 📤 Comportement attendu

```bash
$ python3 all_in.py "New jersey, Tren ton, NewJersey, Trenton, toto, , sAlem"
Trenton is the capital of New Jersey
Tren ton is neither a capital city nor a state
NewJersey is neither a capital city nor a state
Trenton is the capital of New Jersey
Toto is neither a capital city nor a state
Salem is the capital of Oregon
```

**Remarque**: La ligne vide (`, ,`) n'affiche rien - elle est ignorée.

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
2. Diviser la string par virgule
3. Pour chaque expression:
   - `.strip()` pour normaliser les espaces
   - Si chaîne vide → `continue` (ignorer)
   - Chercher dans les états (case-insensitive)
   - Chercher dans les capitales (case-insensitive)
   - Afficher le résultat formaté

## ✅ Format de sortie

- Si c'est une capitale: `{Capital} is the capital of {State}`
- Si c'est un état: `{State} is a state`
- Sinon: `{Expression} is neither a capital city nor a state`

## 🚀 Commandes Docker

### 1. Lancer le conteneur
```bash
cd Django_0_Starting
make ex05
```

### 2. Dans un autre terminal, exécuter le script
```bash
cd Django_0_Starting/ex05
docker compose exec app bash

# Tester
python3 all_in.py "New jersey, Trenton, Paris"
python3 all_in.py "New jersey, Trenton, New jersey,, Oregon"  # Deux virgules = rien
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

## 💡 Points clés

- ✅ `.split(',')` pour diviser par virgule
- ✅ `.strip()` pour enlever les espaces
- ✅ `.lower()` pour comparaison case-insensitive
- ✅ `continue` pour ignorer les lignes vides (pas `return`)
- ✅ Chercher dans les deux dictionnaires
- ✅ Format de sortie précis!

---

**Prêt?** Lance `make ex05` et commence! 🚀

