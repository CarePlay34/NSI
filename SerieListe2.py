taille = int(input("Entrez la taille des tableaux : "))

tableau1 = []
tableau2 = []
tableau_somme = []

print("Saisissez les éléments du premier tableau :")
for i in range(taille):
    element = float(input(f"Élément {i+1} : "))
    tableau1.append(element)

print("Saisissez les éléments du second tableau :")
for i in range(taille):
    element = float(input(f"Élément {i+1} : "))
    tableau2.append(element)

for i in range(taille):
    somme = tableau1[i] + tableau2[i]
    tableau_somme.append(somme)

print("Le nouveau tableau contenant la somme des éléments est :")
print(tableau1,tableau2,tableau_somme)