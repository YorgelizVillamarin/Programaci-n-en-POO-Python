from modelo_animal_caballo import Caballo
from modelo_animal_cocodrilo import Cocodrilo
from modelo_animal_escarabajo import Escarabajo
from modelo_animal_pescado import Pescado
from modelo_animal_pato import Pato
from Database import Base_datos
from modelo_animal import Animal
# --------------------------------------------CODIGO PRINCIPAL-----------------------------------
# CABALLO
caballo = Caballo("Spirit", 5, "Pradera", "Hierba", "Grande", "Marrón", "Mustang", 60)
caballo.mostrar_info()
caballo.galopar()
print()

# COCODRILO
cocodrilo = Cocodrilo("Coco", 12, "Pantano", "Carnívoro", "Grande", "Verde", 3000)
cocodrilo.mostrar_info()
cocodrilo.atacar()
print()

# ESCARABAJO
escarabajo = Escarabajo("Bicho", 1, "Bosque", "Hojas", "Pequeño", "Negro", True, "Hércules")
escarabajo.mostrar_info()
escarabajo.volar()
print()

# PESCADO
pescado = Pescado("Nemo", 2, "Arrecife", "Plancton", "Pequeño", "Naranja", "Salada")
pescado.mostrar_info()
pescado.nadar()
print()

# PATO
pato = Pato("Donald", 3, "Lago", "Omnívoro", "Mediano", "Blanco", "Ancho")
pato.mostrar_info()
pato.graznar()
print()
print()

#-------------------------CODIGO PRINCIPAL BASE DE DATOS------------------------
print()

obj_base_datos = Base_datos()
nombre = input("Ingrese el nombre para su animal: ")
edad  = input("Ingrese la  edad del animal: ")
habitat = input("Ingrese donde habitat: ")
dieta = input("Ingresa la dieta del animal: ")
tamaño = input("Ingrese el tamaño del animal: ")
color  = input("Ingrese el color para su animal: ")

obj_animal = Animal(nombre, edad, habitat, dieta, tamaño, color)
obj_base_datos.guardar_objetos(obj_animal)
obj_base_datos.imprimir_info()





