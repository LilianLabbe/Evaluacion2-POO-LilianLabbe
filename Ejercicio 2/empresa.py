class Empresa:
    def __init__(self):
        self.personal = []

    def agregar(self, trabajador):
        self.personal.append(trabajador)

    def activos(self):
        return [t for t in self.personal if t.activo]

    def total_sueldos(self):
        return sum(t.pago_final() for t in self.activos())