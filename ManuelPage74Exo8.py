def palindrome(chaine):
    # Un palindrome se lit de la même façon à l'endroit et à l'envers
    return chaine == chaine[::-1]

print(palindrome("ressasser"))  # True
print(palindrome("kayak"))      # True
print(palindrome("python"))     # False