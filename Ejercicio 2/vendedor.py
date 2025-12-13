from trabajador import Trabajador

class Vendedor(Trabajador):
    def __init__(self, nombre, rut, sueldo_base, ventas_mes, comision):
        super().__init__(nombre, rut, sueldo_base)
        self.ventas_mes = ventas_mes
        self.comision = comision

    def pago_final(self):
        return self.sueldo + (self.ventas_mes * self.comision)