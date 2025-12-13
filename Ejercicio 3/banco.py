class Banco:
    def __init__(self):
        self.cuentas = []

    def agregar(self, cuenta):
        self.cuentas.append(cuenta)

    def buscar(self, numero):
        for c in self.cuentas:
            if c.numero == numero:
                return c
        return None

    def saldo_total(self):
        return sum(c.saldo for c in self.cuentas)
