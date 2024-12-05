d=int(input("saisir la valeur de d="))
if d<50:
    p=d*0.5
elif 50<=d<=100:
    p=d*0.3
else:
    p=d*0.2
print(f"le prix a payé pour la distance {d}Km est:{p}Dhs ") 
# avec fonction
def peage():
    d=int(input("saisir la valeur de d=")) 
    if d<50:
        p=d*0.5
    elif 50<=d<=100:
        p=d*0.3
    else:
        p=d*0.2
    return f"le prix à payer pour la distance {d}Km est:{p}Dhs"
print(peage())
