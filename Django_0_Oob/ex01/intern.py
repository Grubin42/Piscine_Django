#!/usr/bin/env python3


class Coffee:
    """Classe représentant un café"""
    
    def __str__(self):
        return "This is the worst coffee you ever tasted."


class Intern:
    """Classe représentant un stagiaire"""
    
    def __init__(self, name="My name? I'm nobody, an intern, I have no name."):
        """Constructeur de la classe Intern
        
        Args:
            name (str): Le nom du stagiaire
        """
        self.name = name
    
    def __str__(self):
        """Retourne le nom du stagiaire"""
        return self.name
    
    def work(self):
        """Méthode qui lève une exception"""
        raise Exception("I'm just an intern, I can't do that...")
    
    def make_coffee(self):
        """Retourne une instance de Coffee"""
        return Coffee()


if __name__ == '__main__':
    # Instancier deux fois la classe Intern
    intern_anonymous = Intern()
    intern_mark = Intern('Mark')
    
    # Afficher les noms
    print(f"Intern 1: {intern_anonymous}")
    print(f"Intern 2: {intern_mark}")
    
    # Mark fait un café
    coffee = intern_mark.make_coffee()
    print(f"Mark's coffee: {coffee}")
    
    # L'autre stagiaire essaie de travailler (gérer l'exception)
    try:
        intern_anonymous.work()
    except Exception as e:
        print(f"Exception caught: {e}")

