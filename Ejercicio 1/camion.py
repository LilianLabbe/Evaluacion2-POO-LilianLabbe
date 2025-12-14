from Vehiculo import Vehiculo

class Camion(Vehiculo):
    def __init__(self, codigo, marca, modelo, anio, carga_max):
        super().__init__(codigo, marca, modelo, anio)
        self.carga_max = carga_max

    def tipo(self):
        return "Camión"

    def consumo(self, km):
        factor = 1 + (self.carga_max * 0.03)
        return round((km / 4) * factor, 2)
    
