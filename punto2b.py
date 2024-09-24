import numpy as np
from scipy import interpolate
import random
import matplotlib.pyplot as plt

# Datos iniciales de la pista
distancias = np.linspace(0, 300, 7)
alturas = [10, 60, 55, 70, 40, 50, 30]

# Creamos la spline cúbica
spline_cubica = interpolate.CubicSpline(distancias, alturas)
curvatura = spline_cubica.derivative(2)

xSpline = np.linspace(0, 300, 400)
ySpline = spline_cubica(xSpline)


# Parámetros del algoritmo genético
tamano_poblacion = 500  # Tamaño de la población reducido
num_generaciones = 1000  # Número de generaciones reducido
tasa_mutacion = 0.2  # Tasa de mutación
distancia_minima = 10  # Distancia mínima entre soportes
distancia_maxima = 20  # Distancia máxima entre soportes
num_soportes = 20  # Número de soportes
longitud_pista = 300  # Longitud total de la pista

# Funcion que valida individuo
def validar_individuo(individuo, min_separacion, max_separacion):
    if len(individuo) != num_soportes:
        return False
    for i in range(1, len(individuo)):
        if not (min_separacion <= individuo[i] - individuo[i-1] <= max_separacion):
            return False
    return individuo[-1] <= 300

# Función que genera un individuo válido con exactamente 20 soportes
def generar_individuo_valido(min_separacion, max_separacion, num_soportes):
    while True:
        individuo = [0]  # Primer soporte siempre en 0
        for _ in range(1, num_soportes - 1):
            nuevo_soporte = individuo[-1] + np.random.uniform(min_separacion, max_separacion)
            if nuevo_soporte > 300:
                break
            individuo.append(nuevo_soporte)
        if len(individuo) == num_soportes - 1:
            ultimo_soporte = min(individuo[-1] + np.random.uniform(min_separacion, max_separacion), 300)
            individuo.append(ultimo_soporte)
            if validar_individuo(individuo, min_separacion, max_separacion):
                return individuo

# Función para calcular el promedio ponderado (aptitud)
def calcular_aptitud(individuo):
    y = spline_cubica(individuo)
    w = np.abs(curvatura(individuo))
    return np.sum(y * w) / np.sum(w)

# Inicialización de la población
poblacion = [generar_individuo_valido(distancia_minima, distancia_maxima, num_soportes) for _ in range(tamano_poblacion)]

# Función para seleccionar individuos (torneo)
def seleccionar(poblacion, aptitudes):
    idx1, idx2 = random.sample(range(len(poblacion)), 2)
    return poblacion[idx1] if aptitudes[idx1] < aptitudes[idx2] else poblacion[idx2]

# Función de cruza (crossover)
def crossover(parent1, parent2, min_separacion, max_separacion):
    while True:
        cross_point = np.random.randint(1, num_soportes - 1)
        child1 = parent1[:cross_point] + [x for x in parent2[cross_point:] if x > parent1[cross_point-1]]
        child2 = parent2[:cross_point] + [x for x in parent1[cross_point:] if x > parent2[cross_point-1]]
        
        # Ajustar la longitud si es necesario
        while len(child1) > num_soportes:
            child1.pop(np.random.randint(1, len(child1)-1))
        while len(child1) < num_soportes:
            idx = np.random.randint(1, len(child1)-1)
            child1.insert(idx, (child1[idx-1] + child1[idx]) / 2)
        
        while len(child2) > num_soportes:
            child2.pop(np.random.randint(1, len(child2)-1))
        while len(child2) < num_soportes:
            idx = np.random.randint(1, len(child2)-1)
            child2.insert(idx, (child2[idx-1] + child2[idx]) / 2)
        
        if validar_individuo(child1, min_separacion, max_separacion) and validar_individuo(child2, min_separacion, max_separacion):
            return child1, child2

# Función de mutación (ajustada para verificar)
# Función de mutación que respeta las restricciones de separación
def mutar(individuo, prob, min_separacion, max_separacion):
    for i in range(1, len(individuo) - 1):  # No mutamos el primer ni el último soporte
        if np.random.random() < prob:
            min_pos = max(individuo[i-1] + min_separacion, individuo[i] - (max_separacion - min_separacion))
            max_pos = min(individuo[i+1] - min_separacion, individuo[i] + (max_separacion - min_separacion))
            if min_pos < max_pos:
                individuo[i] = np.random.uniform(min_pos, max_pos)
    return individuo

# Bucle principal del algoritmo genético
for gen in range(num_generaciones):
    fitness = []

    # Calcular el fitness de cada individuo
    for individuo in poblacion:
        fitness_value = calcular_aptitud(individuo)
        fitness.append(1 / (fitness_value + 1e-6))  # Invertimos porque queremos minimizar

    fitness = np.array(fitness)
    fitness = fitness / fitness.sum()  # Normalizar fitness para usar en selección por probabilidad

    # Encontrar el mejor individuo de esta generación
    mejor_indice = np.argmax(fitness)
    mejor_fitness = 1 / (fitness[mejor_indice] + 1e-6) - 1e-6
    
    if gen % 100 == 0:  # Imprimir progreso cada 100 generaciones
        print(f"Generación {gen}: Mejor fitness = {mejor_fitness:.2f}")

    # Crear la nueva generación
    offspring = []
    while len(offspring) < tamano_poblacion:
        parents = np.random.choice(len(poblacion), 2, p=fitness)
        parent1 = poblacion[parents[0]]
        parent2 = poblacion[parents[1]]
        child1, child2 = crossover(parent1, parent2, distancia_minima, distancia_maxima)
        offspring.extend([child1, child2])

    # Aplicar mutación
    for i in range(len(offspring)):
        offspring[i] = mutar(offspring[i], tasa_mutacion, distancia_minima, distancia_maxima)
        # Asegurarse de que el individuo sigue siendo válido después de la mutación
        while not validar_individuo(offspring[i], distancia_minima, distancia_maxima):
            offspring[i] = generar_individuo_valido(distancia_minima, distancia_maxima, num_soportes)

    # Elitismo: mantener al mejor individuo
    offspring[0] = poblacion[mejor_indice]

    poblacion = offspring
    

# Encontrar el mejor individuo
mejor_individuo = poblacion[np.argmax(fitness)]

# Graficar la solución final
plt.figure(figsize=(12, 6))
plt.plot(xSpline, ySpline, label='Spline cúbica')
plt.plot(mejor_individuo, spline_cubica(mejor_individuo), 'rx', label='Soportes optimizados inciso b')
plt.xlabel('Distancia')
plt.ylabel('Altura')
plt.title('Disposición optimizada de 20 soportes')
plt.legend()
plt.grid(True)
plt.show()

#defino funcion para calcular las alturas
def calcular_Alturas(individuo):
    return np.sum(spline_cubica(individuo))

# Imprimir la mejor solución encontrada
print("Mejor disposición de soportes:", mejor_individuo)
print("Número de soportes:", len(mejor_individuo))
print("Altura total:", calcular_Alturas(mejor_individuo))

# Verificar las separaciones
separaciones = np.diff(mejor_individuo)
print("Separaciones entre soportes:", separaciones)
print("Separación mínima:", np.min(separaciones))
print("Separación máxima:", np.max(separaciones))
