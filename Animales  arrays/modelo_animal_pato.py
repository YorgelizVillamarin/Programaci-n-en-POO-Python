from modelo_animal import Animal

class Pato(Animal):
    def __init__(self, nombre, edad, habitat, dieta, tamaño, color, tipo_pico):
        super().__init__(nombre, edad, habitat, dieta, tamaño, color)
        self.tipo_pico = tipo_pico

    def graznar(self):
        print(f"{self.nombre} dice: ¡Cuack cuack!")

    def nadar(self):
        print(f"{self.nombre} está nadando con sus patas palmeadas.")

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Tipo de Pico: {self.tipo_pico}")
        return "Información del pato"
