def var_to_dict():
    musicians = [
        ('Hendrix', '1942'),
        ('Allman', '1946'),
        ('King', '1925'),
        ('Clapton', '1945'),
        ('Johnson', '1911'),
        ('Berry', '1926'),
        ('Vaughan', '1954'),
        ('Cooder', '1947'),
        ('Page', '1944'),
        ('Richards', '1943'),
        ('Hammett', '1962'),
        ('Cobain', '1967'),
        ('Garcia', '1942'),
        ('Beck', '1944'),
        ('Santana', '1947'),
        ('Rasone', '1948'),
        ('White', '1975'),
        ('Frusciante', '1970'),
        ('Thompson', '1949'),
        ('Burton', '1939')
    ]
    
    # Créer le dictionnaire: année -> nom
    musicians_dict = {}
    for name, year in musicians:
        musicians_dict[year] = name
    
    # Trier par année décroissant et afficher formaté
    for year in sorted(musicians_dict.keys(), reverse=True):
        print(f"{year} : {musicians_dict[year]}")


if __name__ == '__main__':
    var_to_dict()