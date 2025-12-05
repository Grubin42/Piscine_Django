#!/usr/bin/env python3


class HotBeverage:
    """Classe représentant une boisson chaude"""
    
    price = 0.30
    name = "hot beverage"
    
    def description(self):
        """Retourne une description de la boisson"""
        return "Just some hot water in a cup."
    
    def __str__(self):
        """Retourne le format d'affichage de la boisson"""
        return f"name : {self.name}\nprice : {self.price:.2f}\ndescription : {self.description()}"


class Coffee(HotBeverage):
    """Classe représentant un café"""
    
    name = "coffee"
    price = 0.40
    
    def description(self):
        """Retourne une description du café"""
        return "A coffee, to stay awake."


class Tea(HotBeverage):
    """Classe représentant un thé"""
    
    name = "tea"



class Chocolate(HotBeverage):
    """Classe représentant du chocolat chaud"""
    
    name = "chocolate"
    price = 0.50
    
    def description(self):
        """Retourne une description du chocolat"""
        return "Chocolate, sweet chocolate..."


class Cappuccino(HotBeverage):
    """Classe représentant un cappuccino"""
    
    name = "cappuccino"
    price = 0.45
    
    def description(self):
        """Retourne une description du cappuccino"""
        return "Un po' di Italia nella sua tazza!"


if __name__ == '__main__':
    # Tests des classes
    beverages = [
        HotBeverage(),
        Coffee(),
        Tea(),
        Chocolate(),
        Cappuccino()
    ]
    
    for beverage in beverages:
        print(beverage)
        print()  # Ligne vide entre les affichages
