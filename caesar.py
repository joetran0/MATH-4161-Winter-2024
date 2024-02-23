import string

alphabet = string.ascii_uppercase
    
ciphertext = "INPUT THE CIPHERTEXT HERE"

for k in range(26):
    plaintext = ""
    for c in ciphertext:
        if c in alphabet:
            location = alphabet.index(c)
            new_location = (location - k) % 26
            new_char = alphabet[new_location]
            plaintext += new_char
                
        else:
            plaintext += c

    print("Shift:", k, "\n", plaintext, "\n\n")