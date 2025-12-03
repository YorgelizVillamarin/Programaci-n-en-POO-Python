from modelo_vehiculo import Vehiculo
from modelo_vehiculo_deportivo import Vehiculo_deportivo
from modelo_vehiculo_carga import Vehiculo_carga
from modelo_vehiculo_transporte import Vehiculo_transporte

#Instancia del padre 
objVehiculo = Vehiculo("Ferrari","MN678","Negro")
objVehiculo.imprimir_info()

#Instancia de la hija vehiculo_deportivo
objVehiculo_deportivo = Vehiculo_deportivo("Lamborghini","GTX987", "Rojo", "V12 6.5L", "LED delanteras", "Eléctricas")
dato_vehiculo_deportivo = objVehiculo_deportivo.imprimir_info()
print(dato_vehiculo_deportivo)

#Instancia de la hija vehiculo_carga
objVehiculo_carga = Vehiculo_carga("Chevrolet NHR", "TR909", "Blanco", 3, "Diesel")
dato_vehiculo_carga = objVehiculo_carga.imprimir_info()
print(dato_vehiculo_carga)

#Instancia de la hija vehiculo_transporte
objVehiculo_transporte = Vehiculo_transporte("Mercedes Benz","GT500","Azul", 4, 6 )
dato_vehiculo_transporte = objVehiculo_transporte.imprimir_info()
print(dato_vehiculo_transporte)