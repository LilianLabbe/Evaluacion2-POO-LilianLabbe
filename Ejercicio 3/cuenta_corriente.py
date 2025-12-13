from cuenta import Cuenta

class CuentaCorriente(Cuenta):
    def __init__(self, numero, titular, saldo, linea_credito):
        super().__init__(numero, titular, saldo)
        self.linea = linea_credito

    def retirar(self, monto):
        if self.saldo - monto >= -self.linea:
            self.saldo -= monto
            self.movimientos.append(f"RETIRO {monto}")
            return True
        return False
