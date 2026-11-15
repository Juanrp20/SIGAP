from lógica_clase_parqueadero import Parqueadero
from datetime import date
from programa_para_guardar import (
    save_parking_lots,
    read_parking_lots,
    save_drivers,
    read_drivers,
    save_vehicle,
    read_vehicle
)

parking_lot = Parqueadero("¿Se me escucha bien?", 100)
parking_lot_1 = Parqueadero("Ciao pescadinho", 64)

#---------------------------- HISTORIA #1 ----------------------------

print(f"Parqueadero 3, A1 = {parking_lot.calculate_spot_cost("A", 1)}")
print(f"Parqueadero 3, C3 = {parking_lot.calculate_spot_cost("C", 3)}")

#---------------------------- HISTORIA #2 ----------------------------

print(f"Puesto = {parking_lot.assign_parking_spot(10000, "Juan", date(2000,1,1), "M", "Honda", "A1V3", 2020, "159753")}")
print(f"Puesto = {parking_lot.assign_parking_spot(50000, "María", date(2000,1,1), "F", "Toyota", "A1V53", 2019, "951357")}")

#---------------------------- HISTORIA #3 ----------------------------

parking_lot.print_square_matrix()
print()
parking_lot_1.print_square_matrix()


#---------------------------- HISTORIA #4 ----------------------------

print(parking_lot.determine_vehicle_in_cell("A", 1))
print(parking_lot.determine_vehicle_location("A1V3"))

#---------------------------- HISTORIA #5-6 ----------------------------

print(f"Valor a pagar en A1: {parking_lot.determine_vehicle_amount_to_pay("A1V53")}")
print(f"Valor a pagar en : {parking_lot.determine_vehicle_amount_to_pay("A1V3")} ")
print()
parking_lot.print_square_matrix()

#---------------------------- HISTORIA #7----------------------------

print(F"Dinero Ingresado : {parking_lot.determine_received_money()}")

print(f"Cantidad de Vehículos Ingresados : {parking_lot.determine_vehicles_entered_count()}")

print(f"Cantidad puestos utilizados : {parking_lot.determine_used_spot_count()}")

#---------------------------- HISTORIA #8----------------------------

print(f"Zona más utilizada : {parking_lot.determine_most_used_zone()}")

print(f"Tasa de ocupación parqueadero: {parking_lot.determine_occupancy_rate()}%")

#---------------------------- HISTORIA #9----------------------------

print(f"Tasa de ocupación Hombres parqueadero: {parking_lot.determine_male_occupancy_rate()}%")
print(f"Tasa de ocupación Mujeres parqueadero: {parking_lot.determine_female_occupancy_rate()}%")


#---------------------------- HISTORIA #10----------------------------
print(f"Marcas parqueadero: \n {parking_lot.determine_vehicle_percentage_by_brand()}")
print(f"Porcentaje de vehículos por año de fabricación: \n {parking_lot.determine_vehicle_percentage_by_manufacture_year()}")
