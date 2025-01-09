def longueur_mots_no_split(phrase):
    longueurs = []
    in_word = False  # Indique si l’on est « dans » un mot
    count = 0        # Compteur de caractères pour le mot en cours
    
    for c in phrase:
        if c != ' ':
            # On est dans un caractère de mot
            if not in_word:
                # On vient de commencer un mot
                in_word = True
                count = 0
            count += 1
        else:
            # On est sur un espace
            if in_word:
                # On vient de finir un mot
                longueurs.append(count)
                in_word = False
    if in_word:
        longueurs.append(count)
    
    return longueurs


def longueur_mots_no_split_alternative(phrase):
    longueurs = []
    i = 0
    n = len(phrase)
    
    while i < n:
        # Passer les espaces (si on en a) pour trouver le début du mot.
        while i < n and phrase[i] == ' ':
            i += 1
        
        # Si on a atteint la fin de la chaîne, on s'arrête.
        if i >= n:
            break
        
        # Début du mot.
        debut = i
        
        # Avancer jusqu'au prochain espace ou la fin de la chaîne.
        while i < n and phrase[i] != ' ':
            i += 1
        
        # La fin du mot se situe à l'indice i (non inclus).
        fin = i
        
        # Calcul de la longueur du mot.
        longueur = fin - debut
        longueurs.append(longueur)
    
    return longueurs


phrase = "Le petit chat est mort"
print(longueur_mots_no_split_alternative(phrase))  # [2, 5, 4, 3, 4]

phrase = "Le petit chat est mort"
print(longueur_mots_no_split(phrase))  # [2, 5, 4, 3, 4]