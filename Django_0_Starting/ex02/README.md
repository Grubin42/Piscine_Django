# Exercice 02 - Mon premier dictionnaire

## 🎯 Objectif
Créer un script Python qui transforme une liste de tuples (nom, année) en un dictionnaire, puis affiche les musiciens triés par année décroissant.

## 📋 Fichier à créer
`var_to_dict.py`

## ✅ Consignes

- ✅ Utiliser la liste de musiciens fournie (couples nom, année)
- ✅ Transformer en dictionnaire: clé=année, valeur=nom
- ✅ Afficher formaté: `ANNÉE : NOM`
- ✅ Trier par année **décroissant** (1970, 1954, 1948...)
- ✅ Un musicien par ligne
- ✅ Aucun code dans le scope global
- ✅ Fonction appelée dans `if __name__ == '__main__':`

## 📤 Résultat attendu

```
1970 : Frusciante
1954 : Vaughan
1948 : Rasone
1944 : Page Beck
1911 : Johnson
...
```

## 📝 Liste à utiliser

```python
musicians = [
    ('Hendrix', '1942'),
    ('Allman', '1946'),
    ('King', '1925'),
    ('Clapton', '1945'),
    ('Johnson', '1911'),
    ('Berry', '1926'),
    ('Vaughan', '1954'),
    ('Cooder', '1947'),
    ('Page', '1944'),
    ('Richards', '1943'),
    ('Hammett', '1962'),
    ('Cobain', '1967'),
    ('Garcia', '1942'),
    ('Beck', '1944'),
    ('Santana', '1947'),
    ('Rasone', '1948'),
    ('White', '1975'),
    ('Frusciante', '1970'),
    ('Thompson', '1949'),
    ('Burton', '1939')
]
```

## 🚀 Commandes Docker

### 1. Lancer le conteneur
```bash
cd Django_0_Starting
make ex02
```

### 2. Dans un autre terminal, exécuter le script
```bash
cd Django_0_Starting/ex02
docker compose exec app bash
python3 var_to_dict.py
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
def var_to_dict():
    musicians = [
        # Liste de tuples (nom, année)
    ]
    
    # Créer le dictionnaire: année -> nom
    musicians_dict = {}
    for name, year in musicians:
        musicians_dict[year] = name
    
    # Trier par année décroissant et afficher formaté
    for year in sorted(musicians_dict.keys(), reverse=True):
        print(f"{year} : {musicians_dict[year]}")


if __name__ == '__main__':
    var_to_dict()
```

## 💡 Points clés

- `sorted(..., reverse=True)` pour trier décroissant
- Format f-string: `f"{year} : {name}"`
- Créer un dictionnaire avec boucle ou dict comprehension
- Afficher ligne par ligne avec print()

---

**Prêt?** Lance `make ex02` et commence! 🚀

