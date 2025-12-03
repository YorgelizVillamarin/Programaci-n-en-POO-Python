from modelo_animal import Animal

class Pescado(Animal):
    def __init__(self, nombre, edad, habitat, dieta, tamaño, color, tipo_agua):
        super().__init__(nombre, edad, habitat, dieta, tamaño, color)
        self.tipo_agua = tipo_agua

    def nadar(self):
        print(f"{self.nombre} nada rápidamente en agua {self.tipo_agua}.")

    def respirar_branquias(self):
        print(f"{self.nombre} respira por branquias.")

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Tipo de Agua: {self.tipo_agua}")
        return "Información del pescado"
