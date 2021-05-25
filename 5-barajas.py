from itertools import count
import random
import collections

PALOS = ['Pica','Corazon','Rombo','Trebol']
VALORES = ['As', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jota', 'Queen', 'King']

def crear_mazo():
    mazos = []
    for palo in PALOS:
        for valor in VALORES:
            mazos.append((palo, valor))
    return mazos

def obtener_baraja(mazos, tamano_baraja):
    baraja = random.sample(mazos, tamano_baraja)
    return baraja

def main(tamano_baraja, intentos):
    mazos = crear_mazo()
    barajas = []

    for _ in range(intentos):
        #Simulador de obtener barajas de x tamaño
        baraja = obtener_baraja(mazos, tamano_baraja)
        barajas.append(baraja)
    
    pares = 0
    for baraja in barajas:
        val = []
        for carta in baraja:
            val.append(carta[1])
        
        counter = dict(collections.Counter(val))
        
        for value in counter.values():
            if value == 2:
                pares += 1
                break
    
    probabilidad_par = pares / intentos
    print(f'La probabilidad de obtener un par en una baraja de {tamano_baraja} cartas es: {probabilidad_par}.')

if __name__ == '__main__':
    tamano_baraja = int(input('De cuantas cartas será la baraja: '))
    intentos = int(input('Cuantos intentos: '))
    main(tamano_baraja, intentos)