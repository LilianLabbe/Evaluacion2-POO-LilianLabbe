class Trabajador:
    def __init__(self, nombre, rut, sueldo_base):
        self.nombre = nombre
        self.rut = rut
        self.sueldo = sueldo_base
        self.activo = True

    def pago_final(self):
        return self.sueldo

    def resumen(self):
        return f"{self.nombre} ({self.rut}) - Sueldo Final: ${self.pago_final():,.0f}"