# Exercice 01 - Nombres

## 🎯 Objectif
Créer un script Python qui lit les nombres d'un fichier et les affiche un par ligne sans virgules.

## 📋 Fichier à créer
`numbers.py`

## ✅ Consignes

- ✅ Ouvrir et lire le fichier `numbers.txt`
- ✅ Les nombres sont séparés par des virgules (1,2,3,...,100)
- ✅ Afficher chaque nombre sur une ligne
- ✅ Sans virgules
- ✅ Aucun code dans le scope global
- ✅ Fonction appelée dans `if __name__ == '__main__':`

## 📤 Résultat attendu

```
1
2
3
4
...
100
```

## 🚀 Commandes Docker

### 1. Lancer le conteneur
```bash
cd Django_0_Starting
make ex01
```

### 2. Dans un autre terminal, exécuter le script
```bash
cd Django_0_Starting/ex01
docker compose exec app bash
python3 numbers.py
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
def read_numbers():
    # Ouvrir numbers.txt
    # Lire les nombres séparés par virgules
    # Afficher chaque nombre sur une ligne
    pass


if __name__ == '__main__':
    read_numbers()
```

## 💡 Tips

- Utilisez `open()` pour ouvrir le fichier
- `.read()` pour lire tout le contenu
- `.split(',')` pour diviser par virgule
- `.strip()` pour enlever les espaces
- Vérifiez que ce n'est pas vide avant d'afficher

---

**Prêt?** Lance `make ex01` et commence! 🚀

