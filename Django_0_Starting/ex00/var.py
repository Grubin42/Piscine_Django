def my_var():
    # 9 variables de types différents
    var_int = 42
    var_str1 = "42"
    var_str2 = "quarante-deux"
    var_float = 2.0
    var_bool = True
    var_list = [42]
    var_dict = {52: 42}
    var_tuple = (52,)
    var_set = set()
    
    # Afficher chaque variable avec son type
    print(f"{var_int} est de type {type(var_int)}")
    print(f"{var_str1} est de type {type(var_str1)}")
    print(f"{var_str2} est de type {type(var_str2)}")
    print(f"${var_float} est de type {type(var_float)}")
    print(f"{var_bool} est de type {type(var_bool)}")
    print(f"{var_list} est de type {type(var_list)}")
    print(f"{var_dict} est de type {type(var_dict)}")
    print(f"{var_tuple} est de type {type(var_tuple)}")
    print(f"{var_set} est de type {type(var_set)}")


if __name__ == '__main__':
    my_var()