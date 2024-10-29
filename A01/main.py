import numpy as np

# matrices A & B
A = np.array([
    [2, 2],
    [3, 0],
    [1, 7]
])

B = np.array([
    [4, 9, 0, 6],
    [2, 7, 9, 2]
])

# multiplication
C = np.dot(A, B)
print(C)
