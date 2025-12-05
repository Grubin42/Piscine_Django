# Exercise 06 - Tri d'un Dictionnaire

## 🎯 Objectif
Trier un dictionnaire de musiciens par année croissante, puis par ordre alphabétique du nom.

## 📋 Fichiers
- `my_sort.py` - Script Python pour le tri

## 📤 Résultat attendu
```
Johnson
King
Berry
Clapton
Hendrix
Garcia
Page
Beck
Richards
Hammett
Cobain
Rasone
Cooder
Santana
Thompson
Vaughan
Frusciante
White
```

## 🚀 Commandes Docker

### Lancer l'exercice
```bash
cd Django_0_Starting
make ex06
```

### Tester le script
```bash
cd Django_0_Starting/ex06
docker compose exec app python3 my_sort.py
```

### Mode interactif
```bash
cd Django_0_Starting/ex06
docker compose run --rm app bash
python3 my_sort.py
```

### Arrêter
```bash
cd Django_0_Starting
make clean
```

## ✅ Consignes
- ✅ Trier par année croissante (1911, 1925, 1926...)
- ✅ Trier alphabétiquement si même année
- ✅ Afficher UN nom par ligne (sans années)
- ✅ Aucun code en scope global
- ✅ Fonction dans `if __name__ == '__main__':`

