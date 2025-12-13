from vehiculo import Vehiculo

class Motocicleta(Vehiculo):
    def __init__(self, codigo, marca, modelo, anio, cc):
        super().__init__(codigo, marca, modelo, anio)
        self.cc = cc

    def tipo(self):
        return "Moto"

    def consumo(self, km):
        base = km / 30
        if self.cc > 400:
            base *= 1.12
        return round(base, 2)