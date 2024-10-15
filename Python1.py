nbr_copies=int(input("saisir le nombre de copies="))
if 0<nbr_copies<10:
    prix=nbr_copies*0.5
elif 10<nbr_copies and nbr_copies<=20:
    prix=nbr_copies*0.4
elif 20<nbr_copies :
    prix=nbr_copies*0.3
else:
    print("valeur invalide")

print("le prix total est=",prix,"Dh")