import numpy as np

# Datos de ejemplo
datos = [15, 18, 22, 24, 26, 28, 30, 32, 35, 38]

# Cálculo de la varianza
varianza = np.var(datos)
print(f"Varianza: {varianza}")

# Cálculo de la desviación estándar
desv_std = np.std(datos)
print(f"Desviación estándar: {desv_std}")

# Ejemplo de normalización usando la desviación estándar
datos_normalizados = (datos - np.mean(datos)) / np.std(datos)
print("Datos normalizados:", datos_normalizados)