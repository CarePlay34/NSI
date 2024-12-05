# Variables
# Quantité : Entier
# Prix_unit, TVA, Prix_total : Réel

# Lecture des données
Quantité = int(input("Saisir Quantité : "))
Prix_unit = float(input("Saisir Prix_unit : "))
TVA = float(input("Saisir le taux de TVA (exemple : pour 20% entrer 0.20) : "))

# Calcul
Prix_total = Quantité * Prix_unit * (1 + TVA)

# Affichage du résultat
print("Prix_total =", Prix_total)



import math

# Variables
# X, Y, Z, Pi : Réel

# Définition de Pi
Pi = 3.1416  # Ou utiliser math.pi pour plus de précision

# Lecture des données
X = float(input("Saisir X : "))
Y = float(input("Saisir Y : "))

# Calculs
Z = X + Y
X = Z * Pi

# Affichage des résultats
print("X =", X, "Z =", Z)

def calculate_final_price(initial_price, tva_percentage):
    """
    Calculates and displays the final price including TVA.
    """
    # Calculate the final price
    final_price = initial_price * (1 + tva_percentage / 100)
    # Format and display the final price with two decimal places
    print(f"The final price including TVA is: {final_price:.2f}€")

# Main code
# Prompt the user for input values
initial_price = float(input("Enter the initial price: "))
tva_percentage = float(input("Enter the TVA percentage: "))

# Call the function with the input values
calculate_final_price(initial_price, tva_percentage)


def calcul_prix_total(quantité, prix_unit, tva):
    """
    Calcule le prix total en fonction de la quantité, du prix unitaire et du taux de TVA.
    """
    prix_total = quantité * prix_unit * (1 + tva)
    return prix_total

# Lecture des données
quantité = int(input("Saisir la Quantité : "))
prix_unit = float(input("Saisir le Prix unitaire : "))
tva = float(input("Saisir le taux de TVA (exemple : pour 20% entrer 0.20) : "))

# Appel de la fonction
prix_total = calcul_prix_total(quantité, prix_unit, tva)

# Affichage du résultat
print("Prix_total =", prix_total)


#Fonction 

def calcul_prix_total(quantité, prix_unit, tva):
    """
    Calcule le prix total en fonction de la quantité, du prix unitaire et du taux de TVA.
    """
    prix_total = quantité * prix_unit * (1 + tva)
    return prix_total

# Lecture des données
quantité = int(input("Saisir la Quantité : "))
prix_unit = float(input("Saisir le Prix unitaire : "))
tva = float(input("Saisir le taux de TVA (exemple : pour 20% entrer 0.20) : "))

# Appel de la fonction
prix_total = calcul_prix_total(quantité, prix_unit, tva)

# Affichage du résultat
print("Prix_total =", prix_total)





def calcul_x_et_z(x, y):
    """
    Calcule les nouvelles valeurs de X et Z en fonction des valeurs initiales de X et Y.
    """
    Pi = 3.1416  # Vous pouvez utiliser math.pi pour plus de précision
    z = x + y
    x = z * Pi
    return x, z

# Lecture des données
x = float(input("Saisir X : "))
y = float(input("Saisir Y : "))

# Appel de la fonction
nouveau_x, z = calcul_x_et_z(x, y)

# Affichage des résultats
print("X =", nouveau_x, "Z =", z)