def init_divisible_par_7():
    divisible_7 = [False] * 1000  # 1000 booléens, tous à False au départ
    
    for i in range(1000):
        if i % 7 == 0:
            divisible_7[i] = True
    
    return divisible_7

tableau = init_divisible_par_7()
print(tableau[2])   
print(tableau[14])  

divisible_7 = init_divisible_par_7()

# Compter le nombre de True dans le tableau
nb_div_7 = sum(divisible_7)  # True compte pour 1, False pour 0
print("Nombre de multiples de 7 < 1000 :", nb_div_7)  

# Le plus grand indice < 1000 avec True
max_div_7 = max(i for i, val in enumerate(divisible_7) if val)
print("Plus grand multiple de 7 < 1000 :", max_div_7)  