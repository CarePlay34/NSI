def mot_de_passe_valide(mot_de_passe):
    # 1) Vérifier la longueur
    if len(mot_de_passe) < 8:
        return False

    # 2) Vérifier la présence d’au moins :
    #    - une majuscule
    #    - une minuscule
    #    - un chiffre
    #    - un caractère spécial (ni lettre, ni chiffre)
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    
    for c in mot_de_passe:
        if c.isupper():
            has_upper = True
        elif c.islower():
            has_lower = True
        elif c.isdigit():
            has_digit = True
        else:
            # Si ce n’est ni une lettre ni un chiffre, c’est un caractère spécial
            has_special = True

    # On retourne True si toutes les conditions sont remplies
    return has_upper and has_lower and has_digit and has_special

print(mot_de_passe_valide("Abc!1234"))   # True
print(mot_de_passe_valide("password"))  # False (pas de majuscule, pas de chiffre, pas de caractère spécial)