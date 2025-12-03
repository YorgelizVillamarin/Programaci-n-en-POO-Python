#Clase Padre Animal

class Animal:
    def __init__(self, nombre, edad, habitat, dieta, tamaño, color):
        self.nombre = nombre
        self.edad = edad
        self.habitat = habitat
        self.dieta = dieta
        self.tamaño = tamaño
        self.color = color

    # MÉTODOS GENERALES
    def moverse(self):
        print(f"{self.nombre} se está moviendo.")

    def comunicarse(self):
        print(f"{self.nombre} está comunicándose con su especie.")

    def reproducirse(self):
        print(f"{self.nombre} está en proceso de reproducción.")

    def alimentarse(self):
        print(f"{self.nombre} se alimenta de {self.dieta}.")

    def adaptarse(self):
        print(f"{self.nombre} se está adaptando a su entorno en {self.habitat}.")

    def instinto(self):
        print(f"{self.nombre} está actuando según sus instintos naturales.")

    def descansar(self):
        print(f"{self.nombre} está descansando.")

    def sueño(self):
        print(f"{self.nombre} está durmiendo profundamente.")

    def interaccion_social(self):
        print(f"{self.nombre} está interactuando socialmente.")

    def mostrar_info(self):
        print("\n  Información del Animal ")
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Hábitat: {self.habitat}")
        print(f"Dieta: {self.dieta}")
        print(f"Tamaño: {self.tamaño}")
        print(f"Color: {self.color}")
        print("-------------------------------")
        return "Información mostrada"