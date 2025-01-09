#Methode A
def nb_mots_no_split_simple(phrase):
    # Hypothèses strictes : 
    # - pas d'espaces en trop en début/fin de phrase
    # - pas d'espaces multiples entre les mots
    if not phrase:
        return 0  # si la chaîne est vide, aucun mot
    return phrase.count(' ') + 1

#Methode B
def nb_mots_no_split(phrase):
    count = 0
    in_word = False
    
    for char in phrase:
        if char != ' ' and not in_word:
            # On vient de trouver le début d'un mot
            count += 1
            in_word = True
        elif char == ' ':
            # Dès qu'on rencontre un espace, on sait qu'on n'est plus dans un mot
            in_word = False
    
    return count

# Exemple de phrase "classique"
phrase = "Le petit chat est mort"
print(nb_mots_no_split_simple(phrase))  
print(nb_mots_no_split(phrase))        

# Avec d’éventuels espaces en trop
phrase2 = "   Le   petit  chat   "
print(nb_mots_no_split_simple(phrase2))  
print(nb_mots_no_split(phrase2))   