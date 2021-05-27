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