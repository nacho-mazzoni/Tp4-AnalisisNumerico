import numpy as np 
import matplotlib.pyplot as plt

distancia = np.linspace(0, 300, 7)
altura = [10, 60, 55, 70, 40, 50, 30]

matrizVandermonde = np.zeros((7,7))

for i in range(matrizVandermonde.shape[0]):
    for j in range(matrizVandermonde.shape[1]):
        matrizVandermonde[i, j]=distancia[i]**(j)

#for i in range(matrizVandermonde.shape[0]):
 #   for j in range(matrizVandermonde.shape[1]):
  #      print(matrizVandermonde[i,j])

#resuelvo el sistema Ax=b --> x=b*1/A
coeficientes = np.linalg.solve(matrizVandermonde, altura)

#for i in range(coeficientes.shape[0]):
    #print(coeficientes[i])

#ecuacion de la recta de interpolacion
def vandermonde(x):
    return coeficientes[6]*(x**6) + coeficientes[5]*(x**5) + coeficientes[4]*(x**4) + coeficientes[3]*(x**3) + coeficientes[2]*(x**2) + coeficientes[1]*x + coeficientes[0]

x_vandermonde = np.linspace(0, 300, 400)
y_vandermonde = vandermonde(x_vandermonde)

plt.plot(x_vandermonde, y_vandermonde, label="interpolacion Vandermonde", color="blue")
plt.scatter(distancia, altura, color="black")
plt.title('Montaña rusa')
plt.xlabel('distancia(m)')
plt.ylabel('altura(m)')
plt.grid(True)
plt.legend()
plt.show()

