from lógica_clase_parqueadero import Parqueadero
from datetime import date
from programa_para_guardar import (
    guardar_parqueaderos,
    leer_parqueaderos,
    guardar_conductor_vehículo,
    leer_conductor_vehículo,
    guardar_vehículo,
    leer_vehículo
)

parqueadero = Parqueadero("¿Se me escucha bien?", 100)
parqueadero_1 = Parqueadero("Ciao pescadinho", 64)

#---------------------------- HISTORIA #1 ----------------------------

print(f"Parqueadero 3, A1 = {parqueadero.calcular_costo_puesto("A", 1)}")
print(f"Parqueadero 3, C3 = {parqueadero.calcular_costo_puesto("C", 3)}")

#---------------------------- HISTORIA #2 ----------------------------

print(f"Puesto = {parqueadero.asignar_puesto(10000, "Juan", date(2000,1,1), "M", "Honda", "A1V3", 2020, "159753")}")
print(f"Puesto = {parqueadero.asignar_puesto(50000, "María", date(2000,1,1), "F", "Toyota", "A1V53", 2019, "951357")}")

#---------------------------- HISTORIA #3 ----------------------------

parqueadero.imprimir_matriz_cuadrada()
print()
parqueadero_1.imprimir_matriz_cuadrada()


#---------------------------- HISTORIA #4 ----------------------------

print(parqueadero.determinar_vehículo_en_casilla("A", 1))
print(parqueadero.determinar_ubicación_vehículo("A1V3"))

#---------------------------- HISTORIA #5-6 ----------------------------

print(f"Valor a pagar en A1: {parqueadero.determinar_valor_a_pagar_vehículo("A1V53")}")
print(f"Valor a pagar en : {parqueadero.determinar_valor_a_pagar_vehículo("A1V3")} ")
print()
parqueadero.imprimir_matriz_cuadrada()

#---------------------------- HISTORIA #7----------------------------

print(F"Dinero Ingresado : {parqueadero.determinar_dinero_ingresado()}")

print(f"Cantidad de Vehículos Ingresados : {parqueadero.determinar_cantidad_vehículos_ingresados()}")

print(f"Cantidad puestos utilizados : {parqueadero.determinar_cantidad_puestos_utilizados()}")

#---------------------------- HISTORIA #8----------------------------

print(f"Zona más utilizada : {parqueadero.determinar_zona_más_utilizada()}")

print(f"Tasa de ocupación parqueadero: {parqueadero.determinar_tasa_ocupación()}%")

#---------------------------- HISTORIA #9----------------------------

print(f"Tasa de ocupación Hombres parqueadero: {parqueadero.determinar_tasa_ocupación_hombres()}%")
print(f"Tasa de ocupación Mujeres parqueadero: {parqueadero.determinar_tasa_ocupación_mujeres()}%")


#---------------------------- HISTORIA #10----------------------------
print(f"Marcas parqueadero: \n {parqueadero.determinar_porcentaje_de_vehículos_por_marca()}")
print(f"Porcentaje de vehículos por año de fabricación: \n {parqueadero.determinar_porcentaje_de_vehículos_por_año_fabricación()}")
