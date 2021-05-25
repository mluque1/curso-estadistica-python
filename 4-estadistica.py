import random
import math

def media(x_arr):
    return sum(x_arr) / len(x_arr)

def varianza(x_arr):
    mu = media(x_arr)
    acum = 0
    for xi in x_arr:
        acum += math.pow(xi - mu, 2)
    return acum / len(x_arr)

def desviacion_estandar(x_arr):
    return math.sqrt(varianza(x_arr))

if __name__ == '__main__':
    x_arr = [random.randint(9, 12) for _ in range (20)]
    mu = media(x_arr)
    Var = varianza(x_arr)
    sigma = desviacion_estandar(x_arr)

    print(x_arr)
    print(f'Media: {mu}')
    print(f'Varianza: {Var}')
    print(f'Desviación estándar: {sigma}')
