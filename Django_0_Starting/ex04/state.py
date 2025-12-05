import sys


def state():
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
    
    # Récupérer l'argument
    capital_name = sys.argv[1]
    
    # Chercher la capitale dans le dictionnaire
    # Trouver le code correspondant
    state_code = None
    for code, capital in capital_cities.items():
        if capital == capital_name:
            state_code = code
            break
    
    # Si capitale trouvée, afficher l'état
    if state_code:
        for state_name, code in states.items():
            if code == state_code:
                print(state_name)
    else:
        print("Unknown capital city")


if __name__ == '__main__':
    state()