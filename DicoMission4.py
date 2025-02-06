# Création du dictionnaire associant chaque lettre à son nombre de points
valeurs = {
    "A": 1, "B": 3, "C": 3, "D": 2, "E": 1, 
    "F": 4, "G": 2, "H": 4, "I": 1, "J": 8, 
    "K": 5
}

# Fonction qui calcule le score total d'un mot
def calculer_score(mot):
    total = 0
    for lettre in mot.upper():
        if lettre in valeurs:
            total += valeurs[lettre]
    return total

# Test avec le mot "KAKI"
mot_test = "KAKI"
score = calculer_score(mot_test)
print(f"Le score de '{mot_test}' est de {score} points.")