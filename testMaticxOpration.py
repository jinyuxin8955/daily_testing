import numpy as np

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print(A + B, A - B)

print(np.dot(A, B))

print(A.T)

print(np.linalg.inv(A))
print(np.linalg.det(A))
print(np.linalg.eig(A))

print(np.dot(np.linalg.inv(A), A))

