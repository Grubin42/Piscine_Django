import sys


def all_in():
    # Vérifier le nombre d'arguments
    if len(sys.argv) != 2:
        return
    
    # Dictionnaires
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
    
    # Récupérer l'argument et diviser par virgule
    input_string = sys.argv[1]
    expressions = input_string.split(',')
    
    # Traiter chaque expression
    for expression in expressions:
        # Normaliser: strip et capitaliser correctement
        normalized = expression.strip()
        
        # Ignorer les chaînes vides (deux virgules d'affilées)
        if not normalized:
            continue
        
        # Chercher dans les états (case-insensitive)
        is_state = False
        state_code = None
        for state_name, code in states.items():
            if state_name.lower() == normalized.lower():
                is_state = True
                state_code = code
                break
        
        # Chercher dans les capitales (case-insensitive)
        is_capital = False
        capital_state = None
        for code, capital_name in capital_cities.items():
            if capital_name.lower() == normalized.lower():
                is_capital = True
                # Trouver l'état correspondant
                for state_name, state_code in states.items():
                    if state_code == code:
                        capital_state = state_name
                        break
                break
        
        # Afficher le résultat
        if is_capital:
            print(f"{normalized} is the capital of {capital_state}")
        elif is_state:
            print(f"{normalized} is a state")
        else:
            print(f"{normalized} is neither a capital city nor a state")


if __name__ == '__main__':
    all_in()

