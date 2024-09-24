#realizar interpolacion de los mismos puntos con splines cubicos

import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate

distancia = np.linspace(0, 300, 7)
altura = [10, 60, 55, 70, 40, 50, 30]

x = np.linspace(0, 300, 400)

splinecubica = interpolate.CubicSpline(distancia, altura)

y = splinecubica(x)

plt.plot(x, y, label="Interpolacion Spline Cubica", color="blue")
plt.scatter(distancia, altura, color="black")
plt.xlabel('x')
plt.ylabel('y')
plt.show()

#ejercicio e puntos en 75 y 225 para spline
print("altura en distancia 75 para spline")
print(splinecubica(75))
print("altura en distancia 225 para spline")
print(splinecubica(225))