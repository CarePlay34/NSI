def calculer_facture(prix_unitaire, quantite):
    montant_total = prix_unitaire * quantite
    if quantite >= 5:
        remise = montant_total * 0.05  
        montant_total -= remise        
    return montant_total

# Cas où le client achète moins de 5 articles
prix = 10.0    
quantite = 3   
facture = calculer_facture(prix, quantite)
print(f"Montant de la facture sans remise: {facture} €")  

# Cas où le client achète au plus 5 articles
prix = 10.0    
quantite = 6   
facture = calculer_facture(prix, quantite)
print(f"Montant de la facture avec remise: {facture} €") 