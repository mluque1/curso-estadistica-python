from borracho import BorrachoTradicional
from borracho import BorrachoSureno
from campo import Campo
from coordenada import Coordenada
import camino_aleatorio as ca

from bokeh.plotting import figure, show

def graficar(x, y, tipo_de_borracho, pasos):
    grafica = figure(title=f'Con: {pasos} pasos.', width=900, height=900, x_range=(-100,100), y_range=(-100,100))
    grafica.line(x, y, legend=f'{tipo_de_borracho.__name__}')

    print(f'Imprimiendo grafico del {tipo_de_borracho.__name__} con {pasos} pasos.')
    show(grafica)

def simular_caminata(pasos, tipo_de_borracho):
    borracho = tipo_de_borracho(nombre='X')
    origen = Coordenada(0,0)
    
    x_arr = [origen.x]
    y_arr = [origen.y]

    campo = Campo()
    campo.anadir_borracho(borracho, origen)
    
    # Movemos al borracho X veces de pasos.
    for _ in range(pasos):
        campo.mover_borracho(borracho)
        coordenada = campo.obtener_coordenada(borracho)
        x_arr.append(coordenada.x)
        y_arr.append(coordenada.y)
    graficar(x_arr, y_arr, tipo_de_borracho, pasos)

def main(distancias_de_caminata, tipo_de_borracho):
    for pasos in distancias_de_caminata:
        simular_caminata(pasos, tipo_de_borracho)
        input()


if __name__=='__main__':
    distancias_de_caminata = [1000]#[10, 100, 1000, 10000]
    #main(distancias_de_caminata, BorrachoTradicional)
    main(distancias_de_caminata, BorrachoSureno)
