#!/usr/bin/env python3

import sys


def parse_periodic_table(filename):
    """Parse le fichier periodic_table.txt et retourne une liste d'éléments"""
    elements = []
    
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            
            # Parser la ligne: "Hydrogen = position:0, number:1, small: H, molar:1.00794, electron:1"
            if ' = ' in line:
                name_part, data_part = line.split(' = ', 1)
                name = name_part.strip()
                
                # Extraire les données
                data = {}
                data['name'] = name
                
                # Parser les key:value séparés par des virgules
                pairs = data_part.split(', ')
                for pair in pairs:
                    if ':' in pair:
                        key, value = pair.split(':', 1)
                        key = key.strip()
                        value = value.strip()
                        
                        if key == 'small':
                            data['symbol'] = value
                        elif key == 'position':
                            data['position'] = int(value)
                        elif key == 'number':
                            data['number'] = int(value)
                        elif key == 'molar':
                            data['molar'] = float(value)
                        elif key == 'electron':
                            data['electron'] = value
                
                # Déterminer la catégorie
                data['category'] = get_category(data['number'])
                elements.append(data)
    
    return elements


def get_category(atomic_number):
    """Détermine la catégorie d'un élément selon son numéro atomique"""
    # Halogènes (F, Cl, Br, I, At, Uus)
    halogens = [9, 17, 35, 53, 85, 117]
    if atomic_number in halogens:
        return 'halogen'
    
    # Gaz nobles
    noble_gases = [2, 10, 18, 36, 54, 86, 118]
    if atomic_number in noble_gases:
        return 'noble'
    
    # Métaux de transition
    if (21 <= atomic_number <= 30) or \
       (39 <= atomic_number <= 48) or \
       (72 <= atomic_number <= 80) or \
       (104 <= atomic_number <= 112):
        return 'transition'
    
    # Lanthanides
    if 57 <= atomic_number <= 71:
        return 'lanthanide'
    
    # Actinides
    if 89 <= atomic_number <= 103:
        return 'actinide'
    
    # Non-métaux
    nonmetals = [1, 6, 7, 8, 16, 34, 52, 83]
    if atomic_number in nonmetals:
        return 'nonmetal'
    
    # Métaux par défaut
    return 'metal'


def get_color(category):
    """Retourne la couleur selon la catégorie"""
    colors = {
        'metal': '#ff6b6b',
        'nonmetal': '#4ecdc4',
        'noble': '#95e1d3',
        'halogen': '#ffd93d',
        'transition': '#a8e6cf',
        'lanthanide': '#c7b3ff',
        'actinide': '#ff8fb1'
    }
    return colors.get(category, '#ffffff')


def get_text_color(category):
    """Retourne la couleur du texte selon la catégorie"""
    dark_text = ['noble', 'halogen', 'transition', 'lanthanide']
    if category in dark_text:
        return '#333'
    return 'white'


def calculate_row(atomic_number):
    """Calcule la ligne du tableau périodique"""
    if atomic_number <= 2:
        return 1
    elif atomic_number <= 10:
        return 2
    elif atomic_number <= 18:
        return 3
    elif atomic_number <= 36:
        return 4
    elif atomic_number <= 54:
        return 5
    elif atomic_number <= 86:
        return 6
    elif atomic_number <= 118:
        return 7
    return 1


def generate_html(elements):
    """Génère le HTML du tableau périodique"""
    html = '''<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tableau Périodique des Éléments</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
        }

        .container {
            max-width: 1600px;
            margin: 0 auto;
        }

        h1 {
            text-align: center;
            color: white;
            margin-bottom: 30px;
            font-size: 2.5em;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        }

        .periodic-table {
            display: grid;
            grid-template-columns: repeat(18, 1fr);
            gap: 4px;
            margin-bottom: 30px;
            background: rgba(255, 255, 255, 0.05);
            padding: 10px;
            border-radius: 12px;
            backdrop-filter: blur(10px);
            max-width: 100%;
            overflow-x: auto;
        }

        .element {
            border: 1px solid rgba(0,0,0,0.3);
            border-radius: 4px;
            padding: 6px;
            cursor: pointer;
            transition: all 0.3s ease;
            text-align: center;
            min-height: 70px;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            font-size: 0.8em;
        }

        .element:hover {
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(0,0,0,0.2);
        }

        .element h4 {
            font-size: 0.85em;
            margin-bottom: 3px;
            font-weight: bold;
            margin: 0;
        }

        .element ul {
            list-style: none;
            font-size: 0.65em;
            text-align: center;
            margin: 0;
            padding: 0;
        }

        .element li {
            margin: 1px 0;
            line-height: 1.2;
        }

        .element.metal { background: #ff6b6b; color: white; }
        .element.nonmetal { background: #4ecdc4; color: white; }
        .element.noble { background: #95e1d3; color: #333; }
        .element.halogen { background: #ffd93d; color: #333; }
        .element.transition { background: #a8e6cf; color: #333; }
        .element.lanthanide { background: #c7b3ff; color: #333; }
        .element.actinide { background: #ff8fb1; color: white; }

        @media (max-width: 1024px) {
            .element {
                min-height: 60px;
                padding: 4px;
                font-size: 0.7em;
            }
            
            .element h4 {
                font-size: 0.75em;
                margin-bottom: 2px;
            }
            
            .element ul {
                font-size: 0.6em;
            }
        }

        @media (max-width: 768px) {
            .periodic-table {
                gap: 2px;
                padding: 5px;
            }
            
            .element {
                min-height: 50px;
                padding: 3px;
                font-size: 0.6em;
            }
            
            .element h4 {
                font-size: 0.65em;
                margin-bottom: 1px;
            }
            
            .element ul {
                font-size: 0.55em;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Tableau Périodique des Éléments</h1>
        <div class="periodic-table">
'''
    
    # Ajouter chaque élément
    for element in elements:
        row = calculate_row(element['number'])
        col = element['position'] + 1
        
        html += f'''            <div class="element {element['category']}" 
                 style="grid-row: {row}; grid-column: {col};">
                <h4>{element['name']}</h4>
                <ul>
                    <li>No {element['number']}</li>
                    <li>{element['symbol']}</li>
                    <li>{element['molar']}</li>
                </ul>
            </div>
'''
    
    html += '''        </div>
    </div>
</body>
</html>
'''
    
    return html


def main():
    """Fonction principale"""
    # Parser les données
    elements = parse_periodic_table('periodic_table.txt')
    
    # Générer l'HTML
    html = generate_html(elements)
    
    # Écrire dans periodic_table.html
    with open('periodic_table.html', 'w') as f:
        f.write(html)
    
    print("✅ Tableau périodique généré: periodic_table.html")
    print(f"📊 {len(elements)} éléments trouvés")


if __name__ == '__main__':
    main()
