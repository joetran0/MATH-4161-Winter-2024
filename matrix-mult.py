import numpy as np

p1 = int(input("p1:"))
p2 = int(input("p2:"))
p3 = int(input("p3:"))
p4 = int(input("p4:"))

A = np.array([[5, 13], [1, 17]])
P = np.array([p1, p2], [p3, p4])


B = np.multiply(A, P) % 29

print(B)