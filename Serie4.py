def def_Echange(a, b):
    """
    Fonction qui échange le contenu de deux données numériques.
    """
    # Échange des valeurs
    temp = a
    a = b
    b = temp
    return a, b

def def_Echange1(a, b, c):
    """
    Fonction qui échange les contenus de trois entiers A, B, C.
    Si la somme est paire, effectue un échange circulaire.
    Sinon, met la somme dans A, le produit dans B, et 0 dans C.
    """
    somme = a + b + c

    if somme % 2 == 0:
        # Échange circulaire des valeurs
        temp = a
        a = b
        b = c
        c = temp
    else:
        # Affectations selon les instructions
        produit = a * b * c
        a = somme
        b = produit
        c = 0

    return a, b, c

# Exemple pour def_Echange
print("Exécution de def_Echange(a, b):")
a = float(input("Entrez la valeur de a : "))
b = float(input("Entrez la valeur de b : "))

print(f"Avant l'échange : a = {a}, b = {b}")
a, b = def_Echange(a, b)
print(f"Après l'échange : a = {a}, b = {b}")

print("\n-------------------------\n")

# Exemple pour def_Echange1
print("Exécution de def_Echange1(a, b, c):")
a = int(input("Entrez la valeur de A : "))
b = int(input("Entrez la valeur de B : "))
c = int(input("Entrez la valeur de C : "))

print(f"Avant traitement : A = {a}, B = {b}, C = {c}")
a, b, c = def_Echange1(a, b, c)
print(f"Après traitement : A = {a}, B = {b}, C = {c}")