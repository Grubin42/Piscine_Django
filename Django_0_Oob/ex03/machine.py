#!/usr/bin/env python3

import random
from beverages import HotBeverage


class CoffeeMachine:
    """Classe représentant une machine à café"""
    
    class BrokenMachineException(Exception):
        """Exception levée quand la machine est en panne"""
        def __init__(self):
            super().__init__("This coffee machine has to be repaired.")
    
    class EmptyCup(HotBeverage):
        """Classe représentant une tasse vide"""
        name = "empty cup"
        price = 0.90
        
        def description(self):
            """Retourne une description de la tasse vide"""
            return "An empty cup?! Gimme my money back!"
    
    def __init__(self):
        """Constructeur de la machine à café"""
        self.broken = False
        self.servings_count = 0
    
    def repair(self):
        """Répare la machine"""
        self.broken = False
        self.servings_count = 0
        print("✅ Machine réparée!")
    
    def serve(self, beverage_class):
        """Sert une boisson
        
        Args:
            beverage_class: Une classe dérivée de HotBeverage
        
        Returns:
            Une instance de beverage_class ou EmptyCup aléatoirement
        
        Raises:
            CoffeeMachine.BrokenMachineException: Si la machine est en panne
        """
        # Vérifier si la machine est en panne
        if self.broken:
            raise CoffeeMachine.BrokenMachineException()
        
        # Incrémenter le compteur de boissons servies
        self.servings_count += 1
        
        # Vérifier si la machine tombe en panne après 10 boissons
        if self.servings_count > 10:
            self.broken = True
            raise CoffeeMachine.BrokenMachineException()
        
        # 50% du temps: retourner une instance de la classe passée
        # 50% du temps: retourner une instance de EmptyCup
        if random.choice([True, False]):
            return beverage_class()
        else:
            return self.EmptyCup()


if __name__ == '__main__':
    from beverages import Coffee, Tea, Chocolate, Cappuccino
    
    print("=" * 60)
    print("MACHINE À CAFÉ - Test")
    print("=" * 60)
    
    machine = CoffeeMachine()
    beverages_to_try = [Coffee, Tea, Chocolate, Cappuccino]
    
    # Premier cycle - jusqu'à la panne
    print("\n🔄 Premier cycle - 10 boissons max:")
    try:
        for i in range(15):
            beverage_class = random.choice(beverages_to_try)
            drink = machine.serve(beverage_class)
            print(f"  Boisson {machine.servings_count}: {drink.name}")
    except CoffeeMachine.BrokenMachineException as e:
        print(f"  ❌ PANNE! {e}")
    
    # Réparer la machine
    print("\n🔧 Réparation de la machine...")
    machine.repair()
    
    # Deuxième cycle - après réparation
    print("\n🔄 Deuxième cycle - 10 boissons max:")
    try:
        for i in range(15):
            beverage_class = random.choice(beverages_to_try)
            drink = machine.serve(beverage_class)
            print(f"  Boisson {machine.servings_count}: {drink.name}")
    except CoffeeMachine.BrokenMachineException as e:
        print(f"  ❌ PANNE! {e}")
    
    print("\n✅ Test terminé!")

