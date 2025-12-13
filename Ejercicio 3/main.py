from cuenta_corriente import CuentaCorriente
from cuenta_ahorro import CuentaAhorro
from banco import Banco

def main():
    banco = Banco()

    c1 = CuentaCorriente("1001", "Edgard", 50000, 80000)
    c2 = CuentaAhorro("2001", "Lilian", 150000, 0.02)

    banco.agregar(c1)
    banco.agregar(c2)

    c1.depositar(20000)
    c1.retirar(90000)

    c2.retirar(30000)
    c2.aplicar_interes()

    print("\n=== CUENTAS ===")
    for c in banco.cuentas:
        print(c.info())

    print("\nHistorial cuenta corriente:")
    for m in c1.movimientos:
        print("-", m)

    print("\nSaldo total banco:", banco.saldo_total())

if __name__ == "__main__":
    main()
