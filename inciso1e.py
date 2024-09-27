import numpy as np
from inciso1a import vandermonde
from inciso1c import splinecubica

#Estimar la altura de la pista a los 75 y 225 metros utilizando ambos metodos
print("altura en distancia 75 para spline")
print(splinecubica(75))
print("altura en distancia 75 para matriz de vandermonde")
print(vandermonde(75))
print("altura en distancia 225 para spline")
print(splinecubica(225))
print("altura en distancia 225 para matriz de vandermonde")
print(vandermonde(225))

