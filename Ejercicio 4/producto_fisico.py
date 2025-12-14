from Producto import Producto

class ProductoFisico(Producto):
    def __init__(self, codigo, nombre, precio, stock, envio):
        super().__init__(codigo, nombre, precio, stock)
        self.envio = envio

    def total(self, cantidad):
        if cantidad > self.stock:
            return None
        costo_envio = 2000 if self.envio == "liviano" else 4000
        return (self.precio * cantidad) + costo_envio

