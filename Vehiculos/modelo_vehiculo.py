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