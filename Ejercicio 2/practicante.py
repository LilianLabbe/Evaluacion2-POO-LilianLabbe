from Trabajador import Trabajador

class Practicante(Trabajador):
    def __init__(self, nombre, rut, horas, valor_hora):
        super().__init__(nombre, rut, 0)
        self.horas = horas
        self.valor_hora = valor_hora

    def pago_final(self):
        return self.horas * self.valor_hora
