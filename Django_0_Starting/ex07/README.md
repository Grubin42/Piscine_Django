# Exercise 07 - Tableau Périodique Interactif

## 🎯 Objectif
Créer un script Python qui parse le fichier `periodic_table.txt` et génère une page HTML interactive affichant le tableau périodique avec design moderne et fonctionnalités interactives.

## 📋 Fichiers
- `periodic_table.py` - Script Python qui génère l'HTML
- `periodic_table.txt` - Données des 118 éléments (fourni)
- `index.html` - Généré automatiquement par le script

## 🎨 Fonctionnalités
✅ Parse le fichier `periodic_table.txt`
✅ Génère l'HTML dynamiquement en Python
✅ Tableau périodique complet (118 éléments)
✅ Couleurs par catégorie (métaux, non-métaux, gaz nobles, etc.)
✅ Légende interactive
✅ Infos détaillées au clic (numéro atomique, masse molaire, configuration électronique)
✅ Design moderne avec gradient et animations
✅ Responsive (adapté aux mobiles)

## 🚀 Commandes Docker

### Lancer l'exercice
```bash
cd Django_0_Starting
make ex07
```

Le script Python va:
1. Parser `periodic_table.txt`
2. Générer `index.html` avec tous les éléments
3. Lancer un serveur HTTP

### Accéder à la page
```
http://localhost:10007
```

### Tester en local
```bash
cd Django_0_Starting/ex07
python3 periodic_table.py  # Génère index.html
# Ouvrir index.html dans le navigateur
```

### Arrêter
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

## 💡 Utilisation
1. Lancez `make ex07`
2. Ouvrez `http://localhost:10007`
3. Cliquez sur un élément pour voir ses détails
4. Fermez la popup en cliquant le X ou ailleurs

## 🎓 Concepts
- **Parsing de fichiers** - Lire et analyser `periodic_table.txt`
- **String manipulation** - Extraire les données
- **Génération HTML** - Créer du HTML en Python
- **CSS en Python** - Intégrer le style dans l'HTML
- **JavaScript inline** - Injecter le JavaScript dans le HTML généré
- **Grille CSS** - Layout du tableau
- **Responsive design** - Adaptation mobile/desktop

