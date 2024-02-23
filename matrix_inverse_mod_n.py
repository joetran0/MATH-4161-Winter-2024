import numpy as np

def getInverseMod(a, n):
    for x in range(1, n):
        if ((a % n) * (x % n) % n == 1):
            return x
    return -1

def getInverseMatrix(A, n):
    detA = int(np.linalg.det(A))
    detA_inv = getInverseMod(detA, n)
    cofactor_A = (detA_inv * detA * np.linalg.inv(A)) % n
    return cofactor_A

def getKey(A, B, n):
    return np.dot(A, getInverseMatrix(B, n)) % 29

A = np.array([[15, 2], [8, 10]])
B = np.array([[25, 27], [16, 6]])

print(getKey(B, A, 29))