class Carrito:
    def __init__(self):
        self.items = []

    def agregar(self, producto, cantidad):
        total = producto.total(cantidad)
        if total is None:
            return False
        self.items.append((producto, cantidad, total))
        producto.stock -= cantidad
        return True

    def detalle(self):
        for p, cant, total in self.items:
            print(f"{p.nombre} x{cant} -> ${total}")

    def total_general(self):
        return sum(t for _, _, t in self.items)
