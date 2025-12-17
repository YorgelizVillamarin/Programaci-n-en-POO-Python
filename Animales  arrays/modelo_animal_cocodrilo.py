from modelo_animal import Animal

class Cocodrilo(Animal):
    def __init__(self, nombre, edad, habitat, dieta, tamaño, color, fuerza_mordida):
        super().__init__(nombre, edad, habitat, dieta, tamaño, color)
        self.fuerza_mordida = fuerza_mordida

    def atacar(self):
        print(f"{self.nombre} ataca con una mordida de {self.fuerza_mordida} PSI.")

    def nadar(self):
        print(f"{self.nombre} está nadando sigilosamente.")

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Fuerza de Mordida: {self.fuerza_mordida} PSI")
        return "Información del cocodrilo"