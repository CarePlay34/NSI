def str_to_int(s):
    resultat = 0
    for char in s:
        # Conversion du caractère en chiffre : ord('0') vaut 48, ord('1') vaut 49, etc.
        chiffre = ord(char) - ord('0')
        resultat = resultat * 10 + chiffre
    return resultat

print(str_to_int("12345"))  