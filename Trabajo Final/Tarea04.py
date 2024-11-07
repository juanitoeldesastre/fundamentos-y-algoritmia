#Ejemplo01

import statistics as stats

#data
calificaciones = [85, 90, 88, 75, 95, 82, 79, 84, 91, 87]

#calcular la varianza y la desviación estándar
varianza = stats.variance(calificaciones)
desviacion_estandar = stats.stdev(calificaciones)

print(f"Varianza: {varianza}")
print(f"Desviación estándar: {desviacion_estandar}")

#Ejemplo02

import numpy as np

#data
precios = [100, 102, 98, 105, 101, 99, 97, 103, 106, 104]

#calcular la varianza y la desviación estándar
varianza = np.var(precios, ddof=1)  # ddof=1 para muestra
desviacion_estandar = np.std(precios, ddof=1)

print(f"Varianza: {varianza}")
print(f"Desviación estándar: {desviacion_estandar}")

#Ejemplo03

import numpy as np

#data
tiempos = [5.1, 5.3, 5.2, 5.4, 5.0, 5.6, 5.1, 5.2, 5.5, 5.3]

#calcular varianza y desviación estándar
varianza = np.var(tiempos, ddof=1)
desviacion_estandar = np.std(tiempos, ddof=1)

print(f"Varianza: {varianza}")
print(f"Desviación estándar: {desviacion_estandar}")
