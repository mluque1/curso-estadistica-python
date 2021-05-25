from itertools import count
import random
import collections

PALOS = ['Pica','Corazon','Rombo','Trebol']
VALORES = ['As', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jota', 'Queen', 'King']

def prob(n):
    return str(n*100) + '%'

def crear_mazo():
    mazos = []
    for palo in PALOS:
        for valor in VALORES:
            mazos.append((palo, valor))
    return mazos

def obtener_baraja(mazos, tamano_baraja):
    baraja = random.sample(mazos, tamano_baraja)
    return baraja

def simulacion(tamano_baraja, intentos):
    mazos = crear_mazo()
    barajas = []

    for _ in range(intentos):
        #Simulador de obtener barajas de x tamaño
        baraja = obtener_baraja(mazos, tamano_baraja)
        barajas.append(baraja)
    return barajas

def color(tamano_baraja, intentos):
    barajas = simulacion(tamano_baraja, intentos)

    color = 0
    for baraja in barajas:
        palos = []
        for carta in baraja:
            palos.append(carta[0])
        
        counter = dict(collections.Counter(palos))
        if len(counter) == 1:
            color += 1

    probabilidad_color = color / intentos
    print(f'La probabilidad de obtener una corrida en una baraja de {tamano_baraja} cartas es: {prob(probabilidad_color)}.')

def par(tamano_baraja, intentos):
    barajas = simulacion(tamano_baraja, intentos)
    
    pares = 0
    for baraja in barajas:
        valores = []
        for carta in baraja:
            valores.append(carta[1])
        
        counter = dict(collections.Counter(valores))
        
        for value in counter.values():
            if value == 2:
                pares += 1
                break
    
    probabilidad_par = pares / intentos
    print(f'La probabilidad de obtener un par en una baraja de {tamano_baraja} cartas es: {prob(probabilidad_par)}.')

def doble_par(tamano_baraja, intentos):
    barajas = simulacion(tamano_baraja, intentos)
    
    doble_par = 0
    for baraja in barajas:
        valores = []
        for carta in baraja:
            valores.append(carta[1])
        
        counter = dict(collections.Counter(valores))
        
        minic = 0
        for value in counter.values():
            if value == 2:
                minic += 1
        if(minic == 2):
            doble_par += 1
    
    probabilidad_doble_par = doble_par / intentos
    print(f'La probabilidad de obtener un doble par en una baraja de {tamano_baraja} cartas es: {prob(probabilidad_doble_par)}.')

if __name__ == '__main__':
    tamano_baraja = int(input('De cuantas cartas será la baraja: '))
    intentos = int(input('Cuantos intentos: '))

    color(tamano_baraja, intentos)
    par(tamano_baraja, intentos)
    doble_par(tamano_baraja, intentos)