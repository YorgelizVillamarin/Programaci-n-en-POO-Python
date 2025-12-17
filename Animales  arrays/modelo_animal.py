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
    
#--------------------------------------- METODOS GETTERS AND SETTERS----------------------------
#Getters
    def get_nombre(self):
        return self.nombre 
    
    def get_edad(self):
        return self.edad 
    
    def get_habitat(self):
        return self.habitat
    
    def get_dieta(self):
        return self.dieta
    
    def get_tamaño(self):
        return self.tamaño
    
    def get_color(self):
        return self.color
    
#Setters
    def set_nombre(self, nombre):
        self.nombre = nombre
    
    def set_edad(self, edad):
        self.edad = edad
    
    def set_habitat(self, habitat):
        self.habitat = habitat
    
    def set_dieta(self, dieta):
        self.dieta = dieta
    
    def set_tamaño(self, tamaño):
        self.tamaño = tamaño
    
    def set_color(self, color):
        self.color = color


