nbr_copies=int(input("saisir le nombre de copies="))
if nbr_copies<10:
    prix=nbr_copies*0.5
elif 10<nbr_copies and nbr_copies<=20:
    prix=nbr_copies*0.4
else:
    prix=nbr_copies*0.3

print("le prix total est=",prix,"Dh")