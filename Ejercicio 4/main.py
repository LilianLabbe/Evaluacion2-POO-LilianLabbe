from Producto_fisico import ProductoFisico
from Producto_digital import ProductoDigital
from Carrito import Carrito

def main():
    c = Carrito()

    libro = ProductoFisico("P1", "Libro Cazadores de Sombras", 15000, 10, "liviano")
    polera = ProductoFisico("P2", "Polera Cuello en V", 12000, 5, "pesado")
    curso = ProductoDigital("D1", "Curso Peluqueria", 50000, 999, "personal")
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


