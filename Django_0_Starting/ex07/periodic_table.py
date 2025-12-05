#!/usr/bin/env python3

import os
import re


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
    <title>Tableau Périodique</title>
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
            max-width: 1400px;
            margin: 0 auto;
        }

        h1 {
            text-align: center;
            color: white;
            margin-bottom: 30px;
            font-size: 2.5em;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        }

        .legend {
            display: flex;
            justify-content: center;
            gap: 30px;
            margin-bottom: 30px;
            flex-wrap: wrap;
        }

        .legend-item {
            display: flex;
            align-items: center;
            gap: 10px;
            background: rgba(255, 255, 255, 0.1);
            padding: 10px 20px;
            border-radius: 8px;
            color: white;
            backdrop-filter: blur(10px);
        }

        .legend-color {
            width: 30px;
            height: 30px;
            border-radius: 4px;
            border: 2px solid rgba(0,0,0,0.2);
        }

        .legend-color.metal { background: #ff6b6b; }
        .legend-color.nonmetal { background: #4ecdc4; }
        .legend-color.noble { background: #95e1d3; }
        .legend-color.halogen { background: #ffd93d; }
        .legend-color.transition { background: #a8e6cf; }

        .periodic-table {
            display: grid;
            grid-template-columns: repeat(18, 1fr);
            gap: 8px;
            margin-bottom: 30px;
            background: rgba(255, 255, 255, 0.05);
            padding: 20px;
            border-radius: 12px;
            backdrop-filter: blur(10px);
        }

        .element {
            aspect-ratio: 0.75;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            border-radius: 8px;
            cursor: pointer;
            transition: all 0.3s ease;
            border: 2px solid rgba(0,0,0,0.2);
            font-weight: bold;
            position: relative;
            overflow: hidden;
            padding: 4px;
        }

        .element:hover {
            transform: translateY(-4px);
            box-shadow: 0 10px 25px rgba(0,0,0,0.3);
        }

        .element-number {
            font-size: 0.7em;
            position: absolute;
            top: 2px;
            left: 2px;
            opacity: 0.8;
        }

        .element-symbol {
            font-size: 1.8em;
            font-weight: bold;
        }

        .element-name {
            font-size: 0.55em;
            text-align: center;
            margin-top: 1px;
            opacity: 0.9;
            line-height: 1.1;
        }

        .element-molar {
            font-size: 0.5em;
            position: absolute;
            bottom: 1px;
            left: 1px;
            right: 1px;
            opacity: 0.7;
            text-align: center;
        }

        /* Catégories d'éléments */
        .element.metal {
            background: #ff6b6b;
            color: white;
        }

        .element.nonmetal {
            background: #4ecdc4;
            color: white;
        }

        .element.noble {
            background: #95e1d3;
            color: #333;
        }

        .element.halogen {
            background: #ffd93d;
            color: #333;
        }

        .element.transition {
            background: #a8e6cf;
            color: #333;
        }

        .element.lanthanide {
            background: #c7b3ff;
            color: #333;
        }

        .element.actinide {
            background: #ff8fb1;
            color: white;
        }

        /* Info Box */
        .info-box {
            position: fixed;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            background: white;
            border-radius: 12px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            padding: 30px;
            max-width: 500px;
            width: 90%;
            z-index: 1000;
            animation: slideIn 0.3s ease;
            display: none;
        }

        .info-box.active {
            display: block;
        }

        @keyframes slideIn {
            from {
                transform: translate(-50%, -50%) scale(0.8);
                opacity: 0;
            }
            to {
                transform: translate(-50%, -50%) scale(1);
                opacity: 1;
            }
        }

        .close-btn {
            position: absolute;
            top: 10px;
            right: 10px;
            background: none;
            border: none;
            font-size: 24px;
            cursor: pointer;
            color: #999;
            padding: 5px;
        }

        .close-btn:hover {
            color: #333;
        }

        .info-content h2 {
            color: #333;
            margin-bottom: 15px;
            border-bottom: 2px solid #667eea;
            padding-bottom: 10px;
        }

        .info-content p {
            margin: 8px 0;
            color: #555;
            line-height: 1.6;
        }

        .info-label {
            font-weight: bold;
            color: #333;
        }

        .info-value {
            color: #667eea;
        }

        /* Responsive */
        @media (max-width: 1200px) {
            .periodic-table {
                gap: 6px;
            }
            
            h1 {
                font-size: 2em;
            }
        }

        @media (max-width: 768px) {
            .periodic-table {
                grid-template-columns: repeat(12, 1fr);
                gap: 4px;
                padding: 10px;
            }
            
            h1 {
                font-size: 1.5em;
            }
            
            .legend {
                gap: 10px;
            }
            
            .legend-item {
                padding: 8px 12px;
                font-size: 0.9em;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Tableau Périodique des Éléments</h1>
        
        <div class="legend">
            <div class="legend-item">
                <div class="legend-color metal"></div>
                <span>Métaux</span>
            </div>
            <div class="legend-item">
                <div class="legend-color nonmetal"></div>
                <span>Non-métaux</span>
            </div>
            <div class="legend-item">
                <div class="legend-color noble"></div>
                <span>Gaz nobles</span>
            </div>
            <div class="legend-item">
                <div class="legend-color halogen"></div>
                <span>Halogènes</span>
            </div>
            <div class="legend-item">
                <div class="legend-color transition"></div>
                <span>Métaux de transition</span>
            </div>
        </div>

        <div class="periodic-table" id="periodicTable">
'''
    
    # Ajouter chaque élément
    for element in elements:
        row = calculate_row(element['number'])
        col = element['position'] + 1
        
        html += f'''            <div class="element {element['category']}" 
                 style="grid-row: {row}; grid-column: {col};"
                 onclick="showInfo('{element['name']}', {element['number']}, '{element['symbol']}', {element['molar']}, '{element['electron']}', '{element['category']}')">
                <div class="element-number">{element['number']}</div>
                <div class="element-symbol">{element['symbol']}</div>
                <div class="element-name">{element['name']}</div>
                <div class="element-molar">{element['molar']}</div>
            </div>
'''
    
    html += '''        </div>

        <div class="info-box" id="infoBox">
            <button class="close-btn" onclick="closeInfo()">✕</button>
            <div class="info-content" id="infoContent"></div>
        </div>
    </div>

    <script>
        function showInfo(name, number, symbol, molar, electron, category) {
            const infoBox = document.getElementById('infoBox');
            const infoContent = document.getElementById('infoContent');
            
            infoContent.innerHTML = `
                <h2>${name} (${symbol})</h2>
                <p><span class="info-label">Numéro atomique:</span> <span class="info-value">${number}</span></p>
                <p><span class="info-label">Symbole:</span> <span class="info-value">${symbol}</span></p>
                <p><span class="info-label">Masse molaire:</span> <span class="info-value">${molar} g/mol</span></p>
                <p><span class="info-label">Configuration électronique:</span> <span class="info-value">${electron}</span></p>
                <p><span class="info-label">Catégorie:</span> <span class="info-value">${category}</span></p>
            `;
            
            infoBox.classList.add('active');
        }

        function closeInfo() {
            document.getElementById('infoBox').classList.remove('active');
        }

        // Fermer en cliquant en dehors
        document.addEventListener('click', (e) => {
            const infoBox = document.getElementById('infoBox');
            const closeBtn = e.target.closest('.close-btn');
            
            if (infoBox.classList.contains('active')) {
                // Fermer si on clique le bouton X
                if (closeBtn) {
                    closeInfo();
                    return;
                }
                
                // Fermer si on clique en dehors de la popup
                if (!infoBox.contains(e.target) && !e.target.classList.contains('element')) {
                    closeInfo();
                }
            }
        });
    </script>
</body>
</html>
'''
    
    return html


def main():
    """Fonction principale"""
    # Obtenir le chemin du fichier périodique_table.txt
    script_dir = os.path.dirname(os.path.abspath(__file__))
    periodic_file = os.path.join(script_dir, 'periodic_table.txt')
    
    # Parser les données
    elements = parse_periodic_table(periodic_file)
    
    # Générer l'HTML
    html = generate_html(elements)
    
    # Écrire dans index.html
    output_file = os.path.join(script_dir, 'index.html')
    with open(output_file, 'w') as f:
        f.write(html)
    
    print(f"✅ Tableau périodique généré: {output_file}")
    print(f"📊 {len(elements)} éléments trouvés")


if __name__ == '__main__':
    main()

