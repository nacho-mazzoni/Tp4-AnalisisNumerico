import numpy as np 
import matplotlib.pyplot as plt
from inciso1b import condicionMatriz


distancia = np.linspace(0, 300, 7)
altura = [10, 60, 55, 70, 40, 50, 30]

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
y = coeficientes[6]*(distancia**6) + coeficientes[5]*(distancia**5) + coeficientes[4]*(distancia**4) + coeficientes[3]*(distancia**3) + coeficientes[2]*(distancia**2) + coeficientes[1]*distancia + coeficientes[0]

#recta
plt.plot(distancia, y, label="interpolacion Vandermonde", color="blue")

#puntos sobre la recta
plt.scatter(distancia, altura, label="puntos", color="black")

#supuestamente la grafica queda asi recta porque no hay suficientes puntos de muestra 

plt.title('Recta con puntos')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

#inciso b Condicion de Matriz de vandermonde

condicionVandermonde = condicionMatriz(matrizVandermonde)
print(condicionVandermonde)
print(np.linalg.cond(matrizVandermonde))