from Producto import Producto

class ProductoDigital(Producto):
    def __init__(self, codigo, nombre, precio, stock, licencia):
        super().__init__(codigo, nombre, precio, stock)
        self.licencia = licencia

    def total(self, cantidad):
        extra = 3000 if self.licencia == "comercial" else 0
        return (self.precio * cantidad) + extra

