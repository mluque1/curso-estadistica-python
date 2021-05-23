from borracho import BorrachoTradicional
from borracho import BorrachoSureno
from campo import Campo
from coordenada import Coordenada

def caminata(campo, borracho, pasos):
    '''
    Simulación y ejecución de la caminata de un borracho 
    teniendo en cuenta el número de pasos. Necesita el campo 
    donde se mueve el borracho, el borracho y la cantidad de 
    pasos. Retorna la distancia entre el punto inicial del 
    borracho y el final.
    '''
    # Obtenemos la coordenada inicial de la caminata
    inicio = campo.obtener_coordenada(borracho)
    
    # Movemos al borracho X veces de pasos
    for _ in range(pasos):
        campo.mover_borracho(borracho)

    return inicio.distancia(campo.obtener_coordenada(borracho))



def simular_caminata(pasos, numero_de_intentos, tipo_de_borracho):
    borracho = tipo_de_borracho(nombre='Juanito')
    origen = Coordenada(0,0)
    distancias = []

    for _ in range(numero_de_intentos): 
        #Agregamos a todos los borrachos
        campo = Campo()
        campo.anadir_borracho(borracho, origen)
        simulacion_caminata = caminata(campo, borracho, pasos)
        distancias.append(round(simulacion_caminata, 1))
    return distancias

def main(distancias_de_caminata, numero_de_intentos, tipo_de_borracho):
    for pasos in distancias_de_caminata:
        distancias = simular_caminata(pasos, numero_de_intentos, tipo_de_borracho)
        distancia_media = round(sum(distancias)/len(distancias), 4)
        distancia_max = max(distancias)
        distancia_min = min(distancias)
        print(f'Para un total de {pasos} pasos y con el {tipo_de_borracho.__name__}. Tenemos que:')
        print(f'Distancia media: {distancia_media}')
        print(f'Distancia máxima: {distancia_max}.')
        print(f'Distancia mínima: {distancia_min}.')
        print('')
    print('------------------------------------------------')

    

if __name__ == '__main__':
    distancias_de_caminata = [10, 100, 1000, 10000]
    numero_intentos = 100

    main(distancias_de_caminata, numero_intentos, BorrachoTradicional)
    main(distancias_de_caminata, numero_intentos, BorrachoSureno)