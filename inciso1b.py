#calcular el numero de condicion de la matriz de Vandermonde

import numpy as np

def condicionMatriz(matriz):
    matInv = np.linalg.inv(matriz)
    return ((np.linalg.norm(matriz,2))*(np.linalg.norm(matInv,2)))


