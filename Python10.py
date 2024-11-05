def annonce(num, prov, dest):
    if dest != "0":
        msg = f"le train n° {num} en provenance de {prov} et à destination de {dest}, entre en gare."
    else:
        msg = f"le train n° {num} en provenance de {prov} entre en gare. Ce train est arrivé au terminus Tanger Ville."
    return msg

resultat1 = annonce("4557", "Casablanca", "Marrakech")
print(resultat1)

resultat2 = annonce("5768", "Casablanca", "0")
print(resultat2)