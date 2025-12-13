from vehiculo import Vehiculo

class Automovil(Vehiculo):
    def __init__(self, codigo, marca, modelo, anio, rendimiento):
        super().__init__(codigo, marca, modelo, anio)
        self.rendimiento = rendimiento

    def tipo(self):
        return "Auto"

    def consumo(self, km):
        return round(km / self.rendimiento, 2)