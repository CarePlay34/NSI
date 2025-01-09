capitales = {
    "France": "Paris",
    "Espagne": "Madrid",
    "Italie": "Rome",
    "Allemagne": "Berlin",
    "Portugal": "Lisbonne"
}

def pays_de_la_capitale(ville):
    # On parcourt chaque (pays, capitale) du dictionnaire
    for pays, capitale in capitales.items():
        # Pour être plus robustes, on compare en minuscule
        if capitale.lower() == ville.lower():
            return pays
    # Si aucune correspondance trouvée, on renvoie None
    return None

# Exemples d'utilisation
print(pays_de_la_capitale("Rome"))      # Italie
print(pays_de_la_capitale("Berlin"))    # Allemagne
print(pays_de_la_capitale("Budapest"))  # None