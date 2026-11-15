from lógica_clase_parqueadero import Parqueadero
from clase_vehículo import Vehículo
from clase_conductor import Conductor
from datetime import datetime
from datetime import date
import ast
import csv


def save_parking_lots(parking_lot : Parqueadero):
    parking_list = []
    parking_list.append(parking_lot)

    with open("parqueaderos.csv", mode= 'w', newline= '') as file: 
        column_names = ['nombre_parqueadero', 'cantidad_puestos_parqueadero']
        writer = csv.DictWriter(file, fieldnames=column_names)
        writer.writeheader()

        for parking_lot in parking_list:
            writer.writerow({
                'nombre_parqueadero' : parking_lot.name, 
                'cantidad_puestos_parqueadero' : parking_lot.parking_spot_count
            })

def read_parking_lots() -> list:
    registered_parking_lots = []
    with open("parqueaderos.csv", mode='r', newline='') as file: 
        reader = csv.DictReader(file)

        for row in reader: 
            parking_name = row['nombre_parqueadero']
            parking_spot_count = int(row['cantidad_puestos_parqueadero'])
            registered_parking_lots.append(Parqueadero(parking_name, parking_spot_count))
    return registered_parking_lots

def save_drivers(driver_records : list):
    with open('registro_conductores.csv', mode='w', newline='') as file: 
        column_names = ['nombre_conductor', 'fecha_nacimiento_conductor', 'sexo_conductor', 'documento_identidad_conductor']
        writer = csv.DictWriter(file, fieldnames=column_names)
        writer.writeheader()

        for driver in driver_records: 
            writer.writerow({
                'nombre_conductor' : driver.driver_name,
                'fecha_nacimiento_conductor' : driver.driver_birth_date,
                'sexo_conductor' : driver.driver_sex,
                'documento_identidad_conductor' : driver.driver_identity_document
            })

def read_drivers() -> list: 
    driver_records = []
    with open('registro_conductores.csv', mode='r', newline='') as file:
        reader = csv.DictReader(file)

        for row in reader: 
            driver_name = row['nombre_conductor']
            driver_birth_date = (datetime.strptime(row['fecha_nacimiento_conductor'], "%Y-%m-%d")).date()
            driver_sex = row['sexo_conductor']
            driver_identity_document = row['documento_identidad_conductor']
            driver_records.append(Conductor(driver_name, driver_birth_date, driver_sex, driver_identity_document))
        return driver_records

def save_vehicle(vehicle_list : list): 
    with open('registro_vehículos.csv', mode='w', newline='') as file: 
        column_names = ['marca_vehículo', 'matrícula_vehículo','año_fabricación_vehículo', 'documento_identidad_conductor_vehículo', 
                            'hora_ingreso_vehículo', 'hora_egreso_vehículo', 'puesto_asignado']
        writer = csv.DictWriter(file, fieldnames=column_names)
        writer.writeheader()

        for vehicle in vehicle_list:
            entry_time_string = vehicle.vehicle_entry_time.strftime('%Y-%m-%d %H:%M:%S') if vehicle.vehicle_entry_time else ''
            exit_time_string = vehicle.vehicle_exit_time.strftime('%Y-%m-%d %H:%M:%S') if vehicle.vehicle_exit_time else ''
       
            writer.writerow({
                'marca_vehículo' : vehicle.vehicle_brand,
                'matrícula_vehículo' : vehicle.vehicle_license_plate,
                'año_fabricación_vehículo' : vehicle.vehicle_manufacture_year,
                'documento_identidad_conductor_vehículo': vehicle.vehicle_owner,
                'hora_ingreso_vehículo': entry_time_string,
                'hora_egreso_vehículo': exit_time_string,
                'puesto_asignado' : vehicle.assigned_spot 

            })

def read_vehicle() -> list:
    vehicle_list = []
    with open('registro_vehículos.csv', mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader: 
            vehicle_brand = row['marca_vehículo']
            vehicle_license_plate = row['matrícula_vehículo']
            vehicle_manufacture_year = int(row['año_fabricación_vehículo'])
            vehicle_owner = row['documento_identidad_conductor_vehículo']

            if row['hora_ingreso_vehículo']:
                vehicle_entry_time = datetime.strptime(row['hora_ingreso_vehículo'], '%Y-%m-%d %H:%M:%S')
            else:
                vehicle_entry_time = None

            if row['hora_egreso_vehículo']:
                vehicle_exit_time = datetime.strptime(row['hora_egreso_vehículo'], '%Y-%m-%d %H:%M:%S')
            else:
                vehicle_exit_time = None

            assigned_spot = ast.literal_eval(row['puesto_asignado'])
            vehicle_list.append(Vehículo(vehicle_brand, vehicle_license_plate, vehicle_manufacture_year, vehicle_owner))
            
            vehicle_list[(len(vehicle_list)-1)].vehicle_entry_time = vehicle_entry_time
            vehicle_list[(len(vehicle_list)-1)].vehicle_exit_time = vehicle_exit_time
            vehicle_list[(len(vehicle_list)-1)].assigned_spot = assigned_spot

        return vehicle_list