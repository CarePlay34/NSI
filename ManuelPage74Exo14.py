personnes = {
    "Jean Aymar": {"taille": 178, "pays": "USA", "age": 31},
    "Clio Patre": {"pays": "Portugal", "age": 32, "taille": 179},
}

# a) Fonction qui retourne l'âge d'une personne ou None si elle n'est pas dans le dictionnaire
def get_age(nom_personne):
    if nom_personne in personnes:
        return personnes[nom_personne].get("age")  # .get("age") renverra None s'il n'y a pas de champ 'age'
    return None

# b) Fonction qui calcule la taille moyenne des personnes dans le dictionnaire
def taille_moyenne():
    if not personnes:
        return 0  # ou None, selon la convention voulue

    total_taille = 0
    nb_personnes = 0

    for infos in personnes.values():
        if "taille" in infos:
            total_taille += infos["taille"]
            nb_personnes += 1

    if nb_personnes == 0:
        return 0  # ou None, s'il n'y a personne avec une taille définie

    return total_taille / nb_personnes


print(get_age("Jean Aymar"))  # 31
print(get_age("Clio Patre"))  # 32
print(get_age("Inconnu"))     # None

print(taille_moyenne())       # (178 + 179) / 2 = 178.5