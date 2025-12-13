#E1 — Flota de Vehículos y Consumo de Combustible 
#Una empresa de transporte quiere contar con un sistema para gestionar su flota de vehículos y 
#estimar el consumo de combustible de cada uno, así como el consumo total para ciertos trayectos. 
#Se necesita que éste permita: 
#1. Registrar vehículos de la flota, almacenando al menos: 
#• Identificación del vehículo (por ejemplo, patente). 
#• Marca. 
#• Modelo. 
#• Año de fabricación.

class Vehiculo:
    def __init__(self, codigo, marca, modelo, anio):
        self.codigo = codigo
        self.marca = marca
        self.modelo = modelo
        self.anio = anio

    def descripcion(self):
        return f"{self.codigo} -> {self.marca} {self.modelo} ({self.anio})"

    def tipo(self):
        return "Vehículo"

    def consumo(self, km):
        raise NotImplementedError()