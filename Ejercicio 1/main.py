
from automovil import Automovil
from motocicleta import Motocicleta
from camion import Camion
from flota import Flota

def main():
        flota = Flota()
        flota.agregar(Automovil("A1", "Mazda", "3", 2020, 17))
        flota.agregar(Motocicleta("M1", "Yamaha", "R3", 2018, 300))
        flota.agregar(Camion("C1", "Mercedes", "Actros", 2015, 10))

        print("\nVehículos registrados:")
        flota.listar()

        km = 120
        print(f"\nConsumos para {km} km:")
        for v in flota.items:  
            print(f"{v.codigo}: {v.consumo(km)} L")

        print("\nConsumo total:", flota.consumo_total(km), "L")  
if __name__ == "__main__":
    main()

