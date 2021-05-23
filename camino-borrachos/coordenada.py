import math
class Coordenada:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def mover(self, delta_x, delta_y):
        return Coordenada(self.x + delta_x, self.y + delta_y)
    
    def distancia(self, otra_coordenada):
        delta_x = self.x - otra_coordenada.x
        delta_y = self.y - otra_coordenada.y
        return math.sqrt( math.pow(delta_x, 2) + math.pow(delta_y, 2) )
    
    def distanciaOrigen(self):
        return distancia(Coordenada(0,0))
