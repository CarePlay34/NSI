notes = []
for i in range(10):
    note = float(input(f"Saisir la note numéro {i+1}: "))
    notes.append(note)

# Calcul de la moyenne des notes
moyenne = sum(notes) / len(notes)
print(f"La moyenne des notes est: {moyenne}")

# Trouver la position de la meilleure note
meilleure_note = max(notes)
position_meilleure_note = notes.index(meilleure_note) + 1  # +1 pour une position humaine (non indexée à 0)
print(f"La meilleure note est à la position: {position_meilleure_note}")

# Augmentation des notes de 20%
notes_augmentees =[round(note * 1.2,2) for note in notes]
print("Les notes augmentées de 20% sont:")
print(notes_augmentees)