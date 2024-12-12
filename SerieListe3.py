n = int(input("Donnez le nombre d'éléments du tableau : "))

T = []
for i in range(n):
    val = float(input(f"T[{i+1}] = "))  # i+1 pour afficher la "position" humaine
    T.append(val)

U = []

for i in range(n):
    # i est l'indice Python, i+1 est la position
    # position paire => (i+1) mod 2 = 0 => i est impair
    if (i + 1) % 2 == 0:
        U.append(T[i])

for i in range(n):
    # position impaire => (i+1) mod 2 = 1 => i est pair
    if (i + 1) % 2 == 1:
        U.append(T[i])

print("Le tableau U réorganisé est :")
for elem in U:
    print(elem)