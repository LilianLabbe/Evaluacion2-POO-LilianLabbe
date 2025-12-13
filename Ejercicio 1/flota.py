class Flota:
    def __init__(self):
        self.items = []

    def agregar(self, vehiculo):
        if not any(v.codigo == vehiculo.codigo for v in self.items):
            self.items.append(vehiculo)

    def listar(self):
        for v in self.items:
            print(v.descripcion(), "-", v.tipo())

    def consumo_total(self, km):
        return sum(v.consumo(km) for v in self.items)