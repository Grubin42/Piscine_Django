#!/usr/bin/env python3

import sys
import os
import re


def render_template(template_path):
    """Lit un fichier .template et génère un fichier .html"""
    
    # Vérifier l'extension du fichier
    if not template_path.endswith('.template'):
        print(f"Error: File must have .template extension", file=sys.stderr)
        return False
    
    # Vérifier que le fichier existe
    if not os.path.exists(template_path):
        print(f"Error: File '{template_path}' not found", file=sys.stderr)
        return False
    
    # Lire le fichier template
    try:
        with open(template_path, 'r') as f:
            content = f.read()
    except IOError as e:
        print(f"Error reading file: {e}", file=sys.stderr)
        return False
    
    # Importer les variables du settings.py
    try:
        import settings
        settings_vars = {k: v for k, v in vars(settings).items() if not k.startswith('_')}
    except ImportError:
        print("Error: settings.py not found", file=sys.stderr)
        return False
    
    # Remplacer les motifs {variable} par les valeurs de settings.py
    def replace_var(match):
        var_name = match.group(1)
        if var_name in settings_vars:
            return str(settings_vars[var_name])
        else:
            return match.group(0)  # Retourner le motif original si la variable n'existe pas
    
    # Utiliser regex pour remplacer les {variable}
    result = re.sub(r'\{(\w+)\}', replace_var, content)
    
    # Créer le nom du fichier de sortie
    output_path = template_path.replace('.template', '.html')
    
    # Écrire le résultat dans le fichier .html
    try:
        with open(output_path, 'w') as f:
            f.write(result)
        print(f"✅ {output_path} créé avec succès")
        return True
    except IOError as e:
        print(f"Error writing file: {e}", file=sys.stderr)
        return False


if __name__ == '__main__':
    # Vérifier le nombre d'arguments
    if len(sys.argv) != 2:
        print("Usage: python3 render.py <file.template>", file=sys.stderr)
        sys.exit(1)
    
    template_path = sys.argv[1]
    
    if not render_template(template_path):
        sys.exit(1)

