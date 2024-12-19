N = int(input("Entrez le nombre d'éléments : "))

tableau = []

for i in range(N):
    element = float(input(f"Entrez l'élément {i+1} : "))
    tableau.append(element)

# Tri à bulles : On répète autant de fois qu'il y a d'éléments
for i in range(N):
    # A chaque passage, les plus grands éléments "remontent" en fin de tableau
    for j in range(0, N - i - 1):
        if tableau[j] > tableau[j+1]:
            # Échanger les éléments
            tableau[j], tableau[j+1] = tableau[j+1], tableau[j]

print("Le tableau trié est :", tableau)