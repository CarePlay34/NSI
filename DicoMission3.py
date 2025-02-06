# Création du dictionnaire
d = {"nom": "Obama", "prenom": "Barak", "age": 58}

# 1. Corriger l'erreur dans le prénom
d["prenom"] = "Barack"

# 2. Afficher la liste des clés du dictionnaire
print("Clés :", d.keys())

# 3. Afficher la liste des valeurs du dictionnaire
print("Valeurs :", d.values())

# 4. Afficher la liste des paires clé/valeur du dictionnaire
print("Paires clé/valeur :", d.items())

# 5. Écrire la phrase "Barack Obama a 58 ans"
#    (en utilisant les informations du dictionnaire)
print(f"{d['prenom']} {d['nom']} a {d['age']} ans")