from trabajador import Trabajador

class Gerente(Trabajador):
    def __init__(self, nombre, rut, sueldo_base, bono):
        super().__init__(nombre, rut, sueldo_base)
        self.bono = bono

    def pago_final(self):
        return self.sueldo + self.bono