import numpy as np
import matplotlib.pyplot as plt

# Datos para el gráfico
columnas = ['Prob 1', 'Prob 2', 'Prob 3', 'Prob 4', 'Prob 5']
subcolumnas = ['a, b', 'a, b', 'a, b, c', '', 'a, b']
valores = np.array([
    [10, 20, 30, 40, 50],
    [15, 25, 35, 45, 55],
    [7, 14, 21, 28, 35],
    [12, 24, 36, 48, 60],
    [18, 36, 54, 72, 90]
])

# Crear el gráfico de barras
ancho_barras = 0.15
posiciones = np.arange(len(columnas))
fig, ax = plt.subplots()

for i in range(len(subcolumnas)):
    ax.bar(posiciones + i * ancho_barras, valores[:, i], width=ancho_barras, label=subcolumnas[i])

# Personalizar el gráfico
ax.set_xticks(posiciones + (len(subcolumnas) - 1) * ancho_barras / 2)
ax.set_xticklabels(columnas)
ax.set_xlabel('Columnas')
ax.set_ylabel('Valores')
ax.set_title('Gráfico de barras con columnas y subcolumnas')
ax.legend()

# Mostrar el gráfico
plt.show()
