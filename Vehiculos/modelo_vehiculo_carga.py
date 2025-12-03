#clase hija  Vehiculo_carga

from modelo_vehiculo import Vehiculo

class Vehiculo_carga(Vehiculo):
    def __init__(self, marca, placa, color, pasajeros, combustible ):
        super().__init__(marca, placa, color)
        self.pasajeros = pasajeros
        self.combustible = combustible
    
    def contar_pasajeros(self):
        print(f"La cantidad de pasajeros son: {self.pasajeros}")
    
    def consumir_combustible(self):
        print(f"El consumo del vehiculo de carga es: {self.combustible}")
    
    def imprimir_info(self):
        super().imprimir_info()
        print(f"La cantidad de pasajeros es: {self.pasajeros}")
        print(f"El consumo de combustible es: {self.combustible}")
        return "Informacion encontrada"

