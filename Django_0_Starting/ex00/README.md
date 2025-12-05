# Exercice 00 - Mes premières variables

## 🎯 Objectif
Créer un script Python qui définit 9 variables de types différents et affiche chaque variable avec son type.

## 📋 Fichier à créer
`var.py`

## ✅ Consignes importantes

- ✅ Fonction `my_var()` - Aucun code dans le scope global
- ✅ 9 variables de types différents (int, str, float, bool, list, dict, tuple, set)
- ✅ Afficher chaque variable avec son type
- ✅ Appeler la fonction dans: `if __name__ == '__main__':`
- ✅ Python3 uniquement

## 🚀 Commandes Docker

### 1. Lancer le conteneur
```bash
cd Django_0_Starting
make ex00
```

### 2. Dans un autre terminal, exécuter le script
```bash
cd Django_0_Starting/ex00
docker compose exec app bash
python3 var.py
```

### 3. Résultat attendu
```
40 est de type <class 'int'>
40 est de type <class 'str'>
quarante-deux est de type <class 'str'>
$2.0 est de type <class 'float'>
true est de type <class 'bool'>
[42] est de type <class 'list'>
{52: 42} est de type <class 'dict'>
(52,) est de type <class 'tuple'>
set() est de type <class 'set'>
```

### 4. Arrêter le conteneur
```bash
cd Django_0_Starting && make clean
```

## 💻 Commandes rapides
```bash
make up         # Lancer le conteneur
make down       # Arrêter
make shell      # Ouvrir un bash dans le conteneur
make logs       # Voir les logs
```

## 📝 Structure du fichier

```python
def my_var():
    # Définir 9 variables de types différents
    # Afficher chaque variable avec son type
    pass


if __name__ == '__main__':
    my_var()
```

---

**Prêt?** Lance `make ex00` et commence! 🚀

