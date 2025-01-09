def est_ordonne(tableau):
    for i in range(len(tableau) - 1):
        if tableau[i] > tableau[i + 1]:
            return False
    return True

valeurs1 = [1, 2, 3, 4]
valeurs2 = [1, 3, 2, 4]

print(est_ordonne(valeurs1))  
print(est_ordonne(valeurs2))  