import numpy as np
from statistics import median

# Datos de ejemplo
datos = [12, 15, 18, 22, 25, 27, 30, 32, 35, 38]

# Cálculo de la media
media = np.mean(datos)
print(f"Media: {media}")

# Cálculo de la mediana
mediana = median(datos)
print(f"Mediana: {mediana}")