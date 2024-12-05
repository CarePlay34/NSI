# Afficher les nombres impairs inférieurs à 120

for i in range(1, 120, 2):
    print(i)

# Afficher les multiples de 3 entre 6 et 150

for i in range(6, 151, 3):
    print(i)


print([i for i in range(6,151) if i %3 ==0])
