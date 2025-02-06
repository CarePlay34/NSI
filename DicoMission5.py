# Dictionnaire de correspondance héxa -> binaire (4 bits)
hex_to_bin = {
    '0': '0000', '1': '0001', '2': '0010', '3': '0011',
    '4': '0100', '5': '0101', '6': '0110', '7': '0111',
    '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
    'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'
}

def convertir_hex_en_binaire(hex_number):
    # On convertit le nombre en majuscules pour gérer indifféremment
    # les saisies en minuscule ou majuscule.
    hex_number = hex_number.upper()
    
    # On construit la chaîne binaire en concaténant
    # la valeur correspondant à chaque caractère hexa
    binaire = ""
    for char in hex_number:
        binaire += hex_to_bin[char]
    
    # Pour supprimer d’éventuels zéros initiaux tout en 
    # conservant au moins un '0' si le nombre vaut réellement zéro.
    binaire = binaire.lstrip('0')
    if binaire == "":
        binaire = "0"
    
    return binaire

# Exemple d'utilisation
hex_value = input("Entrez un nombre hexadécimal : ")
bin_value = convertir_hex_en_binaire(hex_value)
print(f"Le nombre hexadécimal {hex_value} vaut {bin_value} en binaire.")