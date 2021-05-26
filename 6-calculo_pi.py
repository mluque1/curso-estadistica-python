import random
import math
from estadisticas import desviacion_estandar, media

def lanzar_agujas(numero_de_agujas):
    circulo = 0
    for _ in range (numero_de_agujas):
        x = random.random() * random.choice([-1, 1])
        y = random.random() * random.choice([-1, 1])
        distancia_desde_el_centro = math.sqrt(math.pow(x, 2) + math.pow(y, 2))

        if distancia_desde_el_centro <= 1:
            circulo += 1
    
    return (4 * circulo) / numero_de_agujas

def estimacion(numero_de_agujas, intentos):
    estimados = []
    for _ in range (intentos):
        estimacion_pi = lanzar_agujas(numero_de_agujas)
        estimados.append(estimacion_pi)
    
    mean = media(estimados)
    sigma = desviacion_estandar(estimados)

    print(f'Media: {round(mean, 5)}, Sigma: {round(sigma, 5)}, Agujas: {numero_de_agujas}')
    return (mean, sigma)

def estimar_pi(precision, intentos):
    numero_de_agujas = 1000
    sigma = precision
    while(sigma >= precision / 1.96):
        mean, sigma = estimacion(numero_de_agujas, intentos)
        numero_de_agujas *= 2
    return mean


if __name__ == '__main__':
    estimar_pi(0.01, 1000)