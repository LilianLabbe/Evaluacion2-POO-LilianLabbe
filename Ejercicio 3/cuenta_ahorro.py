from cuenta import Cuenta

class CuentaAhorro(Cuenta):
    def __init__(self, numero, titular, saldo, interes):
        super().__init__(numero, titular, saldo)
        self.interes = interes

    def retirar(self, monto):
        if monto <= self.saldo:
            self.saldo -= monto
            self.movimientos.append(f"RETIRO {monto}")
            return True
        return False

    def aplicar_interes(self):
        ganancia = self.saldo * self.interes
        self.saldo += ganancia
        self.movimientos.append(f"INTERÉS {ganancia}")
        return ganancia
