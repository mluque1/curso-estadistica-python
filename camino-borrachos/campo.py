
class Campo:

    def __init__(self):
        self.coordenadas_de_borrachos = {}
    
    def anadir_borracho(self, borracho, coordenada):
        self.coordenadas_de_borrachos[borracho] = coordenada
    
    def mover_borracho(self, borracho):
        delta_x, delta_y = borracho.camina() # Determina el siguiente paso a seguir
        coordenada_actual = self.coordenadas_de_borrachos[borracho] # Busca la coordenada donde se encuentra el borracho
        nueva_coordenada = coordenada_actual.mover(delta_x, delta_y) # Determina la nueva coordenada según la diferencia

        self.coordenadas_de_borrachos[borracho] = nueva_coordenada # Asigna nueva coordenada

    def obtener_coordenada(self, borracho):
        return self.coordenadas_de_borrachos[borracho]