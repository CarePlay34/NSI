def verifier_age(age):
    if age >= 18:
        return "Bonjour, vous êtes majeur."
    else:
        return "Bonjour, tu es mineur."
    
message = verifier_age(10)
print(message)