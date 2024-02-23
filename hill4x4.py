import numpy as np
from numpy import matrix
import sympy as sp

ciphertext = "FUTJCWBLOHHH.CLFM.IOFJTCYXZZRXPNFDFMLJKPMJPWDDHDLJ!XRMKWKBWRFHSKXV.Z.?AJCDLSUEUTXJFW!EUR!CZRJ.WV"
ciphertext_44 = "FUTJCWBLOHHH.CLF"
plaintext_44 = "ITWASTHEKINDOFDA"
ciphertext_nums = []
ciphertext_nums_44 = []
plaintext_nums_44 = []
plaintext_nums = []
plaintext_letters = []
            
for char in ciphertext_44.upper():
    ciphertext_nums_44.append(ord(char) - 65)
    for i in range(len(ciphertext_nums_44)):
        if ciphertext_nums_44[i] == -19:
            ciphertext_nums_44[i] = 26
        if ciphertext_nums_44[i] == -32:
            ciphertext_nums_44[i] = 27
        if ciphertext_nums_44[i] == -2:
            ciphertext_nums_44[i] = 28
            
ciphertext_44_cols = [ciphertext_nums_44[i:i + 4] for i in range(0, len(ciphertext_nums_44), 4)]
ciphertext_44_matrix = np.array(ciphertext_44_cols).transpose()

for char in ciphertext.upper():
    ciphertext_nums.append((ord(char) - 65))
    for i in range(len(ciphertext_nums)):
        if ciphertext_nums[i] == -19:
            ciphertext_nums[i] = 26
        if ciphertext_nums[i] == -32:
            ciphertext_nums[i] = 27
        if ciphertext_nums[i] == -2:
            ciphertext_nums[i] = 28
            
ciphertext_cols = [ciphertext_nums[i:i + 4] for i in range(0, len(ciphertext_nums), 4)]
ciphertext_matrix = np.array(ciphertext_cols).transpose()

for char in plaintext_44.upper():
    plaintext_nums_44.append((ord(char) - 65))
    for i in range(len(plaintext_nums_44)):
        if plaintext_nums_44[i] ==  -19:
            plaintext_nums_44[i] = 26
        if plaintext_nums_44[i] == -32:
            plaintext_nums_44[i] = 27
        if plaintext_nums_44[i] == -2:
            plaintext_nums_44[i] = 28

plaintext_44_cols = [plaintext_nums_44[i:i + 4] for i in range(0, len(plaintext_nums_44), 4)]
plaintext_44_matrix = np.array(plaintext_44_cols).transpose()

def getInverseMod(a, n):
    for x in range(1, n):
        if ((a % n) * (x % n) % n == 1):
            return x
    return -1

def getInverseMatrix(A, n):
    detA = int(np.linalg.det(A))
    detA_inv = getInverseMod(detA, n)
    cofactor_A = (detA_inv * detA * np.linalg.inv(A)) % n
    cofactor_A[(cofactor_A > 28 + 0.5) & (cofactor_A < 29)] = 0
    return np.round(cofactor_A).astype(int)

key = np.dot(ciphertext_44_matrix, getInverseMatrix(plaintext_44_matrix, 29)) % 29

key_inv = getInverseMatrix(key, 29)

plaintext_nums = np.concatenate(np.dot(key_inv, ciphertext_matrix).T % 29)

for i in plaintext_nums:
    plaintext_letters.append(chr(i + 65))
    for j in range(len(plaintext_letters)):
        if plaintext_nums[j] == 26:
            plaintext_letters[j] = "."
        if plaintext_nums[j] == 27:
            plaintext_letters[j] = "!"
        if plaintext_nums[j] == 28:
            plaintext_letters[j] = "?"
    
print(plaintext_nums)
print(''.join(str(x) for x in plaintext_letters))