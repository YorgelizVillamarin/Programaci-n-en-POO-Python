from modelo_botella import Botella
from modelo_botella_plastico import Botella_plastico

#codigo principal
#Aqui va la logica del negocio

# instancia del padre
objBotella = Botella("Coca-Cola","1.5L","Especial")
objBotella.imprimir_info()
# Instancia hija 
objBotella = Botella_plastico("Pepsi","500ml","Comun", "Redondo", "Plastico ", "Sin tinte")
dato_out=objBotella.imprimir_info()
print(dato_out)

