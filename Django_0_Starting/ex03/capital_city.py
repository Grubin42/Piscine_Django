import sys


def capital_city():
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
    state_name = sys.argv[1]
    
    # Chercher le code de l'état
    if state_name in states:
        state_code = states[state_name]
        # Chercher la capitale
        if state_code in capital_cities:
            print(capital_cities[state_code])
    else:
        print("Unknown state")


if __name__ == '__main__':
    capital_city()