from vendedor import Vendedor
from gerente import Gerente
from practicante import Practicante
from empresa import Empresa

def main():
    empresa = Empresa()
    empresa.agregar(Vendedor("Lilian", "17.871.561-1", 450000, 1500000, 0.04))
    empresa.agregar(Gerente("Benjamin", "22.472.652-2", 1200000, 200000))
    empresa.agregar(Practicante("Edgard", "18.263.983-3", 60, 4500))

    print("\nTrabajadores activos:")
    for t in empresa.activos():
        print(t.resumen())

    print("\nGasto total mensual:", empresa.total_sueldos())

if __name__ == "__main__":
    main()
