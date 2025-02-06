import random  # On importe le module random pour pouvoir générer des nombres aléatoires

def genereListeEleve(n):
    eleves = {}  
    
    for i in range(1, n + 1):
        notes = []
        for _ in range(5):
            note = random.randint(5, 20) 
            notes.append(note)
        
        eleves["Eleve" + str(i)] = notes
    
    return eleves

print(genereListeEleve(3))