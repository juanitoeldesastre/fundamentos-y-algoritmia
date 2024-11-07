import numpy as np

#vectores
vector_a = np.array([1, 2, 3])
vector_b = np.array([4, 5, 6])

#operaciones básicas con vectores
suma_vectores = vector_a + vector_b      #suma
resta_vectores = vector_a - vector_b     #resta
producto_escalar = np.dot(vector_a, vector_b)  #producto

#imprimir resultados vectores
print("Suma de vectores:", suma_vectores)
print("Resta de vectores:", resta_vectores)
print("Producto escalar de los vectores:", producto_escalar)

#matrices
matriz_A = np.array([[1, 2], [3, 4]])
matriz_B = np.array([[5, 6], [7, 8]])

#operaciones básicas con matrices
suma_matrices = matriz_A + matriz_B       # Suma
resta_matrices = matriz_A - matriz_B      # Resta
producto_matrices = np.dot(matriz_A, matriz_B)  #producto

#transposición de una matriz
transpuesta_A = matriz_A.T

#determinante de una matriz
determinante_A = np.linalg.det(matriz_A)

#imprimir resultados matrices
print("Suma de matrices:\n", suma_matrices)
print("Resta de matrices:\n", resta_matrices)
print("Producto matricial:\n", producto_matrices)
print("Transpuesta de matriz A:\n", transpuesta_A)
print("Determinante de matriz A:", determinante_A)
