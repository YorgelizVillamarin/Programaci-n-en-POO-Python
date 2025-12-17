# Clase Padre Vehiculo

class Vehiculo:
    def __init__(self, marca, placa, color):
        self.marca = marca
        self.placa = placa
        self.color = color
    
    def arrancar_vehiculo (self, marca):    
        print (f"EL vehiculo esta arrancando: {marca}")
        print (f"Con placa: {self.placa}")
    
    def mostrar_color (self, color):
        print (f"El vehiculo {self.marca} su color es {color} ")
    
    def aceleracion_frenado(self, velocidad):
        print(f"El vehiculo {self.marca} esta acelerando a {velocidad} km/h")
        print(f"Vehiculo con placa {self.placa} puede frenar según la velocidad indicada")

#metodo q imprimime la informacion de los atributos
    
    def imprimir_info(self):
        print ("\n")
        print (f"La marca del vehiculo es: {self.marca}")
        print (f"La placa del vehiculo es: {self.placa}")
        print (f"El color del vehiculo {self.marca} es {self.color}")

#-------------------------------METODOS GETTERS Y SETTERS------------------------------------
#Getters
    def get_marca(self):
        return self.marca
    
    def get_placa(self):
        return self.placa
    
    
    def get_color(self):
        return self.color

#Setters
    def set_marca(self,marca):
        self.marca = marca
    
    def set_placa(self, placa):
        self.placa = placa
    
    def set_color(self, color):
        self.color = color
