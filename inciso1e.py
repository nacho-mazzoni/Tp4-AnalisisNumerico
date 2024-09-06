#Estimar la altura de la pista a los 75 y 225 metros utilizando ambos metodos
import numpy as np

#se le pasa el polinomio como si fuera un array
def evaluarPolinomio(f, x):
    resultado=0
    grado = len(f)-1
    for i in f:
        resultado += i*(x**grado)
        grado-=1
    return resultado


