N = int(input("Donnez le nombre d'éléments du tableau : "))

T = []
for i in range(N):
    val = float(input(f"T[{i}] = "))
    T.append(val)

print("Tableau initial :", T)

element_a_ajouter = float(input("Donnez l'élément à ajouter à la fin : "))
T.append(element_a_ajouter)
print("Tableau après ajout :", T)

index_modif = int(input("Donnez l'indice de l'élément à modifier (0 à N) : "))
if 0 <= index_modif < len(T):
    nouvelle_valeur = float(input("Nouvelle valeur : "))
    T[index_modif] = nouvelle_valeur
    print("Tableau après modification :", T)
else:
    print("Indice invalide, aucune modification effectuée.")

index_suppr = int(input("Donnez l'indice de l'élément à supprimer (0 à N) : "))
if 0 <= index_suppr < len(T):
    del T[index_suppr]
    print("Tableau après suppression :", T)
else:
    print("Indice invalide, aucune suppression effectuée.")

if len(T) > 0:
    U = [0]*len(T)
    for i in range(len(T)):
        U[(i+1) % len(T)] = T[i]
    print("Nouveau tableau après décalage à droite :", U)
else:
    print("Tableau vide, impossible de décaler.")