def read_numbers():
    with open('numbers.txt', 'r') as f:
        content = f.read()
    
    # Diviser par virgule et afficher chaque nombre
    numbers = content.split(',')
    
    for number in numbers:
        # Enlever les espaces et afficher
        number = number.strip()
        if number:  # Vérifier que ce n'est pas vide
            print(number)


if __name__ == '__main__':
    read_numbers()