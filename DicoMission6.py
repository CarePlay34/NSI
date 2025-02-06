# On crée un petit dictionnaire Français-Anglais avec 5 mots
dico = {
    "chat": "cat",
    "maison": "house",
    "pomme": "apple",
    "voiture": "car",
    "école": "school"
}

# 1) Fonction "anglais" : affiche tous les mots en anglais (valeurs du dictionnaire)
def anglais(d):
    print("Mots en anglais :")
    for valeur in d.values():
        print(valeur)

# 2) Fonction "francais" : affiche tous les mots en français (clés du dictionnaire)
def francais(d):
    print("Mots en français :")
    for cle in d.keys():
        print(cle)

# 3) Fonction "ajoute" : ajoute un nouveau mot si la clé (mot français) n'existe pas encore
def ajoute(mot_francais, mot_anglais, d):
    if mot_francais not in d:
        d[mot_francais] = mot_anglais
        print(f"Ajouté : '{mot_francais}' -> '{mot_anglais}'")
    else:
        print(f"Le mot '{mot_francais}' existe déjà dans le dictionnaire.")

# 4) Fonction "supprime" : supprime toutes les clés qui commencent par "prefixe"
def supprime(prefixe, d):
    # On repère d’abord les clés à supprimer (pour ne pas modifier le dictionnaire en plein parcours)
    cles_a_supprimer = []
    for cle in d:
        if cle.startswith(prefixe):
            cles_a_supprimer.append(cle)
            
    # On supprime ensuite ces clés
    if cles_a_supprimer:
        for cle in cles_a_supprimer:
            del d[cle]
        print(f"Clés supprimées qui commençaient par '{prefixe}': {cles_a_supprimer}")
    else:
        print(f"Aucune clé ne commence par '{prefixe}'.")

# Programme principal avec un menu
while True:
    print("\n--- MENU ---")
    print("1. Afficher les mots en anglais")
    print("2. Afficher les mots en français")
    print("3. Ajouter un mot (français -> anglais)")
    print("4. Supprimer les mots dont la clé commence par un préfixe")
    print("0. Quitter")

    choix = input("Entrez votre choix : ")

    if choix == '1':
        anglais(dico)
    elif choix == '2':
        francais(dico)
    elif choix == '3':
        mot_fr = input("Entrez le mot en français : ")
        mot_en = input("Entrez la traduction en anglais : ")
        ajoute(mot_fr, mot_en, dico)
    elif choix == '4':
        prefix = input("Entrez le début du mot français à supprimer : ")
        supprime(prefix, dico)
    elif choix == '0':
        print("Fin du programme.")
        break
    else:
        print("Choix invalide. Réessayez.")