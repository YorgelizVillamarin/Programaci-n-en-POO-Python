class Base_datos:
    def __init__(self,):
        self.lista_animales = []
    
    def guardar_objetos(self, nuevo_objeto): 
        self.lista_animales.append(nuevo_objeto)
    
    def agregar_varios_objetos(self):
        self.lista_animales.extend(self.lista_nueva)
    
    def imprimir_info(self):
        for objeto in self.lista_animales:
            print("----- Información del Animal -----")
        print(f"Nombre: {objeto.get_nombre()}")
        print(f"Edad: {objeto.get_edad()}")
        print(f"Hábitat: {objeto.get_habitat()}")
        print(f"Dieta: {objeto.get_dieta()}")
        print(f"Tamaño: {objeto.get_tamaño()}")
        print(f"Color: {objeto.get_color()}")

        