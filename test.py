releve=[(10,20),(11,20),(8,17),(6,18),(7,15),(10,14),(12,17)]
moyenne=[]
def moyennee():
    for i in range(len(releve)):
        moy=sum(releve[i])/len(releve[i])
        moyenne.append(moy)
print(moyennee(),moyenne)