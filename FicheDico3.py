import random  

def genereListeEleve(n):
    eleves = {}  

    for i in range(1, n + 1):
        notes = [] 
        for _ in range(5):
            note = int(random.random() * 16) + 5
            notes.append(note)
        

        eleves["Eleve" + str(i)] = notes

    return eleves

def enregistrerCSV(nom_fichier, eleves):
    with open(nom_fichier, "w") as fichier:
        # Écriture de la ligne d'en-tête
        fichier.write("NOM;Note1;Note2;Note3;Note4;Note5;Moyenne\n")
        
        # Parcours du dictionnaire des élèves
        for nom, notes in eleves.items():
            # Calcul de la moyenne des 5 notes
            moyenne = sum(notes) / len(notes)
            # Transformation de la liste de notes en chaîne de caractères séparées par des points-virgules
            notes_str = ";".join(str(note) for note in notes)
            # Construction de la ligne à écrire, en arrondissant la moyenne à 2 décimales
            ligne = f"{nom};{notes_str};{moyenne:.2f}\n"
            fichier.write(ligne)


# 1. Générer un dictionnaire de 3 élèves avec leurs notes
eleves = genereListeEleve(3)
print(eleves)  # Affichage du dictionnaire dans la console

# 2. Enregistrer ces données dans un fichier CSV nommé "eleves.csv"
enregistrerCSV("eleves.csv", eleves)
print("Le fichier 'eleves.csv' a bien été créé.")