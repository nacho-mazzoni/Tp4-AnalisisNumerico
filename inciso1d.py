import numpy as np 
import matplotlib.pyplot as plt
from scipy import interpolate

from inciso1a import vandermonde
from inciso1c import splinecubica

distancia = np.linspace(0, 300, 7)
altura = [10, 60, 55, 70, 40, 50, 30]

#comparacion de vandermonde y spline cubico
x = np.linspace(0, 300, 400)
y_vandermonde = vandermonde(x)

splinecubica = interpolate.CubicSpline(distancia, altura)
y_s = splinecubica(x)

plt.plot(x, y_vandermonde, label="interpolacion Vandermonde", color="blue")
plt.plot(x, y_s, label="Interpolacion Spline Cubica", color="red")
plt.scatter(distancia, altura, color="black")
plt.title('Montaña rusa')
plt.xlabel('distancia(m)')
plt.ylabel('altura(m)')
plt.grid(True)
plt.legend()
plt.show()