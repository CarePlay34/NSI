#Version1
def dico_ascii():
    return {chr(i): i for i in range(128)}

# Exemple d'utilisation
dico = dico_ascii()
print(dico["A"])  # Affiche 65

#Version2
def dico_ascii():
    ascii_chars = (
        "\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0A\x0B\x0C\x0D\x0E\x0F"
        "\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1A\x1B\x1C\x1D\x1E\x1F"
        " !\"#$%&'()*+,-./"      # Caractères 32 à 47
        "0123456789"            # Caractères 48 à 57
        ":;<=>?@"               # Caractères 58 à 64
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ"  # Caractères 65 à 90
        "[\\]^_`"               # Caractères 91 à 96
        "abcdefghijklmnopqrstuvwxyz"  # Caractères 97 à 122
        "{|}~"                  # Caractères 123 à 126
        "\x7F"                  # Caractère 127
    )
    
    d = {}
    for i in range(len(ascii_chars)):
        d[ascii_chars[i]] = i
    return d

d = dico_ascii()
print("Le code ASCII de 'A' est :", d["A"])  # Affiche 65