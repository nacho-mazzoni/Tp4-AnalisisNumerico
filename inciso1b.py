import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange

from inciso1a import matrizVandermonde, y_vandermonde

#calcular el numero de condicion de la matriz de Vandermonde
def condicionMatriz(matriz):
    matInv = np.linalg.inv(matriz)
    return ((np.linalg.norm(matriz,2))*(np.linalg.norm(matInv,2)))

#condicion de la matriz
print('numero de condicion de la matriz de Vandermonde: ', condicionMatriz(matrizVandermonde))
print("funcion de libreria: ", np.linalg.cond(matrizVandermonde))

#metodo alternativo: polinomio de lagrange 
distancia = np.linspace(0, 300, 7)
altura = [10, 60, 55, 70, 40, 50, 30]

polinomio = lagrange(distancia, altura)

# Evaluar el polinomio en un rango de valores
x = np.linspace(0, 300, 400)
y_lagrange = polinomio(x)

plt.plot(x, y_vandermonde, label="interpolacion Vandermonde", color ="blue")
plt.plot(x, y_lagrange, label="interpolacion Lagrange", color ="red")
plt.scatter(distancia, altura, color='black')
plt.title('Montaña rusa')
plt.xlabel('distancia(m)')
plt.ylabel('altura(m)')
plt.grid(True)
plt.legend()
plt.show()