def my_sort():
    d = {
        'Hendrix': '1942',
        'Allman': '1946',
        'King': '1925',
        'Clapton': '1945',
        'Johnson': '1911',
        'Berry': '1926',
        'Vaughan': '1954',
        'Cooder': '1947',
        'Page': '1944',
        'Richards': '1943',
        'Hammett': '1962',
        'Cobain': '1967',
        'Garcia': '1942',
        'Beck': '1944',
        'Santana': '1947',
        'Rasone': '1948',
        'White': '1975',
        'Frusciante': '1970',
        'Thompson': '1949',
        'Burton': '1939'
    }
    
    # Inverser le dictionnaire: année -> liste de noms
    year_to_names = {}
    for name, year in d.items():
        if year not in year_to_names:
            year_to_names[year] = []
        year_to_names[year].append(name)
    
    # Trier par année croissante, puis par nom alphabétique
    for year in sorted(year_to_names.keys()):
        for name in sorted(year_to_names[year]):
            print(name)


if __name__ == '__main__':
    my_sort()

