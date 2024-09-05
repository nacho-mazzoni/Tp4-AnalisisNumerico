#realizar interpolacion de los mismos puntos con splines cubicos

import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate

distancia = np.linspace(0, 300, 7)
altura = [10, 60, 55, 70, 40, 50, 30]

splineCubica = interpolate.CubicSpline(distancia, altura)

plt.plot(distancia, altura, label="Datos originales")
plt.scatter(distancia, altura, label="puntos", color="black")
plt.xlabel('x')
plt.ylabel('y')
plt.show()
