def Facture(quantite,prix_unitaire_ht,taux_tva):
    if taux_tva==10:
        taux_tva=0.1
    elif taux_tva==20:
        taux_tva=0.2
    else:
        print("taux tva invalide")
        taux_tva=0.2
    montant_ht=quantite*prix_unitaire_ht
    montant_ttc=montant_ht*(1+taux_tva)
    print("Le montant HT (en DHS):",montant_ht)
    print("Le montant TTC (en DHS):",montant_ttc)

quantite=int(input("Entrer la quantité de l'article:"))     
taux_tva=int(input("Entrer le taux de TVA applicable (10 ou 20):"))
prix_unitaire_ht=int(input("Entrer le prix unitaire hors taxe (HT) de l'article:"))

Facture(quantite, prix_unitaire_ht, taux_tva)


