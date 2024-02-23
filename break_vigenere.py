eng = [73, 9, 30, 44, 130, 28, 16, 35, 74, 2, 3, 35, 25, 78, 74, 27, 3, 77, 63, 93, 27, 13, 16, 5, 19, 1]

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def clean(text):
    return "".join([a.upper() for a in text if a.isalpha()])

def encrypt_vigenere(plaintext, key):
    ciphertext = clean(plaintext)
    return "".join([alpha[(alpha.index(ciphertext[i]) + alpha.index(key[i % len(key)])) % 26] for i in range(len(ciphertext))])

def decrypt_vigenere(plaintext, key):
    ciphertext = clean(plaintext)
    return "".join([alpha[(alpha.index(ciphertext[i]) - alpha.index(key[i % len(key)])) % 26] for i in range(len(ciphertext))])

def score_text(text):
    counts = [text.count(a) for a in alpha]
    return sum(counts[i] * eng[i] for i in range(26))

def best_caesar_shift(ciphertext):
    scores = [score_text(decrypt_vigenere(ciphertext, a)) for a in alpha]
    return alpha[scores.index(max(scores))]

def best_vigenere_keyword(ciphertext, length):
    clean_ciphertext = clean(ciphertext)
    return "".join([best_caesar_shift("".join([clean_ciphertext[i] for i in range(len(clean_ciphertext)) if i % length == p])) for p in range(length)])

ciphertext = "XNIPH RVRIW HLRRS TWEHS QTAZY XHJTW PBHZH GSIJU SWWTP RGIZH AVQLT RGTAQ BZLHI WALEW PBKSH VPDRM GAEQP DMPTH HBRUP FEQJS EVEPV XMQYT VONSM EOILC BWGAG DEAKV MMHHA BPUWE JTUEF GPPNC FPMOA FIPXG KPLTR GKHHT PNMWL BPTLW MGCOB RQMVI IVZKE UAELT XWWXM MNLGE HAVQH XKTRB REIYX SQBGR HLSLV OMVXO VFMSV PYVBM LLCGW SGIZH PICXV VHTZH ZKOTT WSBRG CEEJT CVIOK NIXLK ABROM"

for i in range(1, 10):
    print(i, best_vigenere_keyword(ciphertext, i), score_text(decrypt_vigenere(ciphertext, best_vigenere_keyword(ciphertext, i))))
    
print(decrypt_vigenere(ciphertext, "PAINTED"))