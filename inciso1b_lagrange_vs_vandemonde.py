import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange

#calcular el numero de condicion de la matriz de Vandermonde
def condicionMatriz(matriz):
    matInv = np.linalg.inv(matriz)
    return ((np.linalg.norm(matriz,2))*(np.linalg.norm(matInv,2)))

#metodo alternativo polinomio de lagrange 
distancia = np.linspace(0, 300, 7)
altura = [10, 60, 55, 70, 40, 50, 30]

polinomio = lagrange(distancia, altura)

# Evaluar el polinomio en un rango de valores
distancia_new = np.linspace(0, 300, 100)
altura_new = polinomio(distancia_new)

#comparacion vandermonde y lagrange
matrizVandermonde = np.zeros((7,7))

for i in range(matrizVandermonde.shape[0]):
    for j in range(matrizVandermonde.shape[1]):
        #(6-j) para que se haga de atars para adelante el exponente
        matrizVandermonde[i, j]=distancia[i]**(j)

#for i in range(matrizVandermonde.shape[0]):
 #   for j in range(matrizVandermonde.shape[1]):
  #      print(matrizVandermonde[i,j])

#resuelvo el sistema Ax=b --> x=b*1/A
coeficientes = np.linalg.solve(matrizVandermonde, altura)

for i in range(coeficientes.shape[0]):
    print(coeficientes[i])

#ecuacion de la recta de interpolacion
def f(x):
    return coeficientes[6]*(x**6) + coeficientes[5]*(x**5) + coeficientes[4]*(x**4) + coeficientes[3]*(x**3) + coeficientes[2]*(x**2) + coeficientes[1]*x + coeficientes[0]

y_vandermonde = f(distancia_new)

#plt.plot(distancia_new, y_vandermonde, label="interpolacion Vandermonde")
plt.plot(distancia_new, altura_new, label='interpolaciin Lagrange')
plt.scatter(distancia, altura, color='red', label='Puntos originales')
plt.legend()
plt.show()

