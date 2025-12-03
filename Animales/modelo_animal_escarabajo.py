
from modelo_animal import Animal

class Escarabajo(Animal):
    def __init__(self, nombre, edad, habitat, dieta, tamaño, color, tiene_alas, tipo):
        super().__init__(nombre, edad, habitat, dieta, tamaño, color)
        self.tiene_alas = tiene_alas
        self.tipo = tipo

    def volar(self):
        if self.tiene_alas:
            print(f"{self.nombre} está volando.")
        else:
            print(f"{self.nombre} no puede volar.")

    def enrollarse(self):
        print(f"{self.nombre} se enrolla para protegerse.")

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Tipo: {self.tipo}")
        print(f"Tiene Alas: {self.tiene_alas}")
        return "Información del escarabajo"