def encrypt(plaintext, shift):
    ans = ""
    for i in range(len(plaintext)):
        ch = plaintext[i]
        if ch == " ":
            ans += " "
        elif (ch.isupper()):
            ans += chr((ord(ch) + shift - 65) % 26 + 65)
        else:
            ans += chr((ord(ch) + shift - 97) % 26 + 97)
    return ans

def main():
    plaintext = input("Enter String: ")
    shift = int(input("Enter Shift: "))
    encrypt(plaintext, shift)
    
    print(plaintext, shift, encrypt(plaintext, shift))
    
main()