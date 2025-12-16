class Base_datos:
    def __init__(self,):
        self.lista_botellas = []
        self.lista_plastica = []
        self.lista_vidrio = []
    
    def guardar_objetos (self, nuevo_objeto):
        self.lista_botellas.append(nuevo_objeto)
    
    def agregar_varios_objetos(self):
        self.lista_botellas.extend(self.lista_nueva)
    
    def imprimir_info(self):
        for objeto in self.lista_botellas:
            print(objeto.get_marca())
            print(objeto.get_capacidad())
            print(objeto.get_tapa())