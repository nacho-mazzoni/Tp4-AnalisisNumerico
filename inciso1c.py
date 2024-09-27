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
plt.title('Montaña rusa')
plt.xlabel('distancia(m)')
plt.ylabel('altura(m)')
plt.grid(True)
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
