#clase hija  Vehiculo_transporte 

from modelo_vehiculo import Vehiculo

class Vehiculo_transporte(Vehiculo):
    def __init__(self, marca, placa, color, puertas, llantas):
        super().__init__(marca, placa, color)
        self.puertas = puertas
        self.llantas = llantas

    def usar_puertas(self):
        print(f"El vehiculo de transporte tiene {self.puertas}")
    
    def tener_llantas (self):
        print(f"El vehiculo tiene {self.llantas}")
    
    def imprimir_info(self):
        super().imprimir_info()
        print(f"Las puertas son:  {self.puertas}")
        print(f"Las llantas son: {self.llantas}")
        return "Informacion encontrada"