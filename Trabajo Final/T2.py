import numpy as np

# Operaciones con Vectores
vector1 = np.array([1, 2, 3])
vector2 = np.array([4, 5, 6])

# Suma de vectores
suma_vectores = vector1 + vector2
print("Suma de vectores:", suma_vectores)

# Producto punto
producto_punto = np.dot(vector1, vector2)
print("Producto punto:", producto_punto)

# Operaciones con Matrices
matriz1 = np.array([[1, 2], [3, 4]])
matriz2 = np.array([[5, 6], [7, 8]])

# Multiplicación de matrices
mult_matrices = np.dot(matriz1, matriz2)
print("Multiplicación de matrices:\n", mult_matrices)

# Transpuesta
transpuesta = matriz1.T
print("Matriz transpuesta:\n", transpuesta)