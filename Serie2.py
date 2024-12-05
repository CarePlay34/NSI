import math
A = int(input("Entrez la valeur entière de A : "))
B = math.exp(A / 2)
C = round((A + B) / (2 * A))
if (B > A) or (C < A):
    D = True
else:
    D = False
E = 125 + 12
F = "125" + "12"
G = "Vrai"
H = "O"
print("B =", B)
print("C =", C)
print("D =", D)
print("E =", E)
print("F =", F)
print("G =", G)
print("H =", H)