from producto_fisico import ProductoFisico
from producto_digital import ProductoDigital
from carrito import Carrito

def main():
    c = Carrito()

    libro = ProductoFisico("P1", "Libro Python", 15000, 10, "liviano")
    polera = ProductoFisico("P2", "Polera Negra", 12000, 5, "pesado")
    curso = ProductoDigital("D1", "Curso IA", 50000, 999, "personal")
    soft = ProductoDigital("D2", "Software Pro", 30000, 999, "comercial")

    c.agregar(libro, 2)
    c.agregar(polera, 1)
    c.agregar(curso, 1)
    c.agregar(soft, 1)

    print("\n=== DETALLE CARRITO ===")
    c.detalle()

    print("\nTOTAL:", c.total_general())

if __name__ == "__main__":
    main()
