# Exercise 07 - Tableau Périodique des Éléments

## 🎯 Objectif
Créer un script Python qui parse le fichier `periodic_table.txt` et génère une page HTML affichant le tableau périodique des éléments avec le layout correct de Mendeleïev.

## 📋 Fichiers
- `periodic_table.py` - Script Python qui génère l'HTML
- `periodic_table.txt` - Données des 118 éléments (fourni)
- `periodic_table.html` - Généré automatiquement par le script

## ✅ Conformité aux consignes
✅ Seul `import sys` autorisé
✅ Parse le fichier `periodic_table.txt`
✅ Génère l'HTML dynamiquement en Python
✅ Chaque élément dans une case (div avec grid)
✅ Nom en balise `<h4>`
✅ Attributs en liste `<ul><li>` (numéro atomique, symbole, masse molaire)
✅ Layout de Mendeleïev respecté (positions et retours à la ligne)
✅ CSS inline pour le style
✅ HTML valide W3C
✅ Aucun code dans le scope global
✅ Fonction appelée dans `if __name__ == '__main__':`

## 🚀 Commandes

### Avec Docker
```bash
cd Django_0_Starting
make ex07
# Ouvrir http://localhost:10007
```

### En local
```bash
cd Django_0_Starting/ex07

# 1. Générer periodic_table.html
python3 periodic_table.py

# 2. Lancer le serveur
python3 -m http.server 8000

# 3. Ouvrir dans le navigateur
# http://localhost:8000/periodic_table.html
```

### Arrêter (Docker)
```bash
cd Django_0_Starting
make clean
```

## 📊 Catégories d'éléments
- 🔴 **Métaux** - Éléments conducteurs (rouge)
- 🔵 **Non-métaux** - Éléments gazeux/solides (bleu)
- 🟢 **Gaz nobles** - Éléments inertes (vert pâle)
- 🟡 **Halogènes** - Réactifs (jaune)
- 🟠 **Métaux de transition** - Métaux complexes (vert menthe)

## 🎓 Concepts
- **Parsing de fichiers** - Lire et analyser `periodic_table.txt`
- **String manipulation** - Extraire les données sans regex
- **Génération HTML** - Créer du HTML valide en Python
- **CSS inline** - Intégrer le style directement
- **Grid CSS** - Layout du tableau périodique
- **Minimal imports** - Utiliser SEULEMENT `sys`

