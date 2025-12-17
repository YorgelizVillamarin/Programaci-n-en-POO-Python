class Base_datos:

    def __init__(self,):
        self.lista_vehiculo = []
    
    def guardar_objeto(self, nuevo_objeto):
        self.lista_vehiculo.append(nuevo_objeto)
    
    def agregar_varios_objetos(self):
        self.lista_vehiculo.extend(self.lista_nueva)
    
    def imprimir_info(self):
        for objeto in self.lista_vehiculo:
            def imprimir_info(self):
                print ("\n")
                print (f"La marca del vehiculo es: {self.marca}")
                print (f"La placa del vehiculo es: {self.placa}")
                print (f"El color del vehiculo {self.marca} es {self.color}")