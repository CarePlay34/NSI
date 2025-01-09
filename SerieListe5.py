N = int(input("Combien d'éléments voulez-vous trier ? "))

tableau = []
for i in range(N):
    nombre = float(input("Entrez un nombre : "))
    tableau.append(nombre)

# Tri à bulles
for i in range(N - 1):
    for j in range(N - 1 - i):
        if tableau[j] > tableau[j + 1]:
            # On échange les deux nombres
            temp = tableau[j]
            tableau[j] = tableau[j + 1]
            tableau[j + 1] = temp

print("Le tableau trié est :", tableau)