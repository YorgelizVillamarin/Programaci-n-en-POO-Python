from modelo_animal import Animal

class Caballo(Animal):
    def __init__(self, nombre, edad, habitat, dieta, tamaño, color, raza, velocidad):
        super().__init__(nombre, edad, habitat, dieta, tamaño, color)
        self.raza = raza
        self.velocidad = velocidad

    def galopar(self):
        print(f"{self.nombre} está galopando a {self.velocidad} km/h.")

    def relinchar(self):
        print(f"{self.nombre} está relinchando.")

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Raza: {self.raza}")
        print(f"Velocidad: {self.velocidad} km/h")
        return "Información del caballo"