from modelo_botella import Botella
class Botella_plastico(Botella):
    #constructor vacio
    def __init__(self,marca, capacidad,tapa, diseño, material, tinte ):
        super().__init__(marca,capacidad, tapa) 
        self.diseño = ""
        self.material = ""
        self.tinte = ""
    
    #metodo vacio
    def reciclar_botella(self):
        print(f"La botella se va reciclar, Material: {self.material}")
    #polimorfismo
    def imprimir_info(self):
        print(f"El diseño es: {self.diseño}")
        print(f"El material es: {self.material}")
        print(f"El color es:{self.tinte}")
        super().imprimir_info()
        print(f"La tapa padre es: {super().tapa}")
        return"Informacion encontrada"
        #traemos el metodo del padre= lo q tenga super son metodos o aatributos del padre
       