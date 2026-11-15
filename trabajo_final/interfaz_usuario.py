from lógica_clase_parqueadero import Parqueadero
import os
import platform
from datetime import datetime
from datetime import date
from programa_para_guardar import (
    save_parking_lots,
    read_parking_lots,
    save_drivers,
    read_drivers,
    save_vehicle,
    read_vehicle
)

#----------------------------------- FUNCIONALIDADES DE LA INTERFAX DE USUARIO --------------------------------------------------

def clear_screen():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def show_start_menu():
    print("***********************************************************************")
    print("**************** BIENVENIDO AL PROGRAMA DE PARQUEADERO ****************")
    print("***********************************************************************")
    print("\n1. Crear parqueadero")
    print("2. Salir del programa")
    print("\n***********************************************************************")

def show_start_menu_with_existing_parking():
    print("*"*71)
    print("**************** BIENVENIDO AL PROGRAMA DE PARQUEADERO ****************")
    print("*"*71)
    print(f"\nYa ha creado un parqueadero anteriormente con el nombre de {parking_lot.name}.")
    print()
    print("-"*71)
    input("\nPresione enter para ir al menú de opciones.")

def show_parking_types():
    print("\n------------------------- TIPOS DE PARQUEADERO -------------------------")
    print("1. 36 puestos\n2. 64 puestos\n3. 100 puestos")
    print("-"*72)

def show_parking_menu():
    print("**************************** MENÚ FUNCIONES ****************************")
    print("\n1. Registrar entrada vehículo")
    print("2. Mostrar puestos ocupados parqueadero")
    print("3. Buscar vehículo en el parqueadero")
    print("4. Registrar salida de un vehículo")
    print("5. Reporte general del parquadero (Cantidad dinero, autos, puestos inrgesados historicamente)")
    print("6. Reporte zona más utilizada")
    print("7. Tasa ocupación del parqueadero")
    print("8. Tasa de ocupación por genero del conductor en el parqueadero")
    print("9. Tasa de ocupación por marca y año del vehículo")
    print("10. Salir del programa\n")
    print("*"*72)
 
def show_parking_zones_and_prices():
    print("\n---------------- TIPOS ZONAS PARQUEADERO ----------------")
    print()
    for key, value in parking_lot.determine_parking_zone_count().items():
        print(f"{key} : {value}")
    print("-"*57)


#--------------------------------------------------- INTERFAZ DE USUARIO ---------------------------------------------------

if os.path.exists("parqueaderos.csv"):
    parking_list = read_parking_lots()
    parking_lot = parking_list[0]
    show_start_menu_with_existing_parking()
    if os.path.exists('registro_conductores.csv'):
        parking_lot.driver_records = read_drivers()

        if os.path.exists('registro_vehículos.csv'):
            parking_lot.vehicle_records = read_vehicle()
            parking_lot.determine_assigned_spots_matrix()

else:
    

    show_start_menu()
    selected_option = input("Seleccione el número de la opción a realizar: ")
    valid_values = ("1", "2")
    while selected_option not in valid_values:
        selected_option = input("Ingrese una opción válida: ")



    if selected_option == valid_values[0]: 
        clear_screen()
        print("\n--------------------------- DATOS NECESARIOS ---------------------------")

        parking_name = input("\n Escriba el nombre del parqueadero: ")
        while len(parking_name.strip()) == 0:
            parking_name = input("El nombre del parqueadero no puede estar vacío: ")
        
        clear_screen()
        show_parking_types()

        parking_spot_count_string = input("Ahora, seleccione la cantidad de puestos del parqueadero teniendo en cuenta los tipos posibles: ")
        while parking_spot_count_string not in ("36", "64", "100") or len(parking_spot_count_string.strip()) == 0:
            parking_spot_count_string = input("Ingrese una cantidad de puestos válida: ")
        parking_spot_count = int(parking_spot_count_string)
        print("-"* 70)
        parking_lot = Parqueadero(parking_name, parking_spot_count)
        selected_option = None
        print("Parqueadero creado con éxito!\n")
        save_parking_lots(parking_lot)

    elif selected_option == valid_values[1]: 
        clear_screen()
        selected_option = None
        print("-"*72)
        print("--------------------- GRACIAS POR USAR EL PROGRAMA ---------------------")
        print("-"*72)

        raise SystemExit

keep_using_program = True
while keep_using_program:
    clear_screen()
    show_parking_menu()
    selected_option = input("\nSelecciones la opción que necesite: ")
    print()
    while selected_option not in ("1","2","3","4","5","6","7","8","9","10"):
        selected_option = input("Ingrese una opción válida: ")
    


    if selected_option == "1":
        
        keep_registering_vehicles = True
        while keep_registering_vehicles:
            clear_screen()
            print("\n************************** REGISTRAR VEHÍCULO **************************")
            print()
            print("------------------ Datos Necesarios para el registro -------------------")
            print()

            driver_name = input("Ingrese el nombre del conductor del vehículo: ")
            while len(driver_name.strip()) == 0:
                driver_name = input("El nombre del conductor no puede estar vacío: ")

            
            driver_birth_date_string = input("Ingrese la fecha de nacimiento del conductor (AÑO-MES-DÍA), ejemplo: 2000-01-02: ")
            keep_asking_birth_date = True
            while keep_asking_birth_date: 
                if len(driver_birth_date_string.strip()) == 0: 
                    driver_birth_date_string = input("La fecha de nacimiento del conductor no puede estar vacía: ")

                elif len(driver_birth_date_string.strip()) != 0:
                    try:
                        driver_birth_date = datetime.strptime(driver_birth_date_string, "%Y-%m-%d")

                        driver_birth_date_parsed = driver_birth_date.date()
                        if driver_birth_date_parsed > date.today(): 
                            driver_birth_date_string = input("La fecha de nacimiento del conductor no puede ser mayor a la fecha actual, ingrese nuevamente: ")
                        else:
                            break

                    except ValueError:
                        driver_birth_date_string = input("Ingrese una fecha de nacimiento valida: ")
            driver_birth_date = (datetime.strptime(driver_birth_date_string, "%Y-%m-%d")).date()

            driver_biological_sex = (input("Ingrese el sexo biológico del conductor del vehículo (M: Masculino, F: Femenino): ")).upper()
            while len(driver_biological_sex.strip()) == 0 or driver_biological_sex not in ("M", "F"):
                driver_biological_sex = (input("Ingrese un valor valido para el sexo del conductor: ")).upper()

            driver_identity_document = input("Ingrese el documento de identidad del conductor: ")
            while len(driver_identity_document.strip()) == 0:
                driver_identity_document = input("El documento de identida del conductor no puede estar vacío, ingrese nuevamente: ")

            print("\n---------------------------- Datos vehículo ----------------------------")
            vehicle_brand = input("\nIngrese la marca del vehículo a registrar: ")
            while len(vehicle_brand.strip()) == 0:
                vehicle_brand = input("No puede dejar esto vacío, ingrese una marca valida: ")

            vehicle_license_plate = input("Ingrese la matrícula del vehículo a registrar: ")
            while len(vehicle_license_plate.strip()) == 0: 
                vehicle_license_plate = input("No puede dejar esto vacío, ingrese una matrícula valida: ")

            vehicle_manufacture_year_string = input("Ingrese el año de fabricación del vehículo a asignar (Año : XXXX): ")
            while True:
                while len(vehicle_manufacture_year_string.strip()) == 0:
                    vehicle_manufacture_year_string = input("No puede dejar esto vacío, ingrese nuevamente el año de fabricación del vehículo: ")
                vehicle_manufacture_year = int(vehicle_manufacture_year_string)

                if vehicle_manufacture_year > int(date.today().year):
                    vehicle_manufacture_year_string = input("El año de fabricación no puede ser mayor al año actual: ")
                else: 
                    break

                
            show_parking_zones_and_prices()

            price_preference_string = input("Ingrese el valor monetario de la zona dónde se quiere ubicar: ")
            while True: 
                if len(price_preference_string.strip()) == 0: 
                    price_preference_string = input("La preferencia de precio no puede estar vacía,  ingrese nuevamente: ")
                
                else: 
                    try: 
                        price_preference = int(price_preference_string)

                        if price_preference not in parking_lot.determine_parking_zone_count().values(): 
                            price_preference_string = input("La preferencia de precio debe estar entre los valores disponibles: ")
                        
                        else: 
                            break
                    
                    except ValueError: 
                        price_preference_string = input("La preferencia de precio debe ser un número: ")
            
            try:
                assigned_vehicle_spot = parking_lot.assign_parking_spot(price_preference, driver_name, driver_birth_date, driver_biological_sex, vehicle_brand, vehicle_license_plate, vehicle_manufacture_year, driver_identity_document)

            except ValueError:
                print("-"*72)
                print("---------------- No fue posible registrar el vehículo ------------------")
                print("-"*72)
                print("\nPresiona enter para volver al menú principal")
                input("")

                break
            
            print("-"*72)
            print("\nEl vehículo ha sido ingresado correctamente!!")
            print(f"\nVehículo ubicado en puesto : {assigned_vehicle_spot[0]}{assigned_vehicle_spot[1]}")
            print()
            print("-"*72)

            keep_registering_string = input("¿Desea seguir registrando vehículos (Sí, No): ")
            keep_registering = keep_registering_string.upper()
            while True:
                if len(keep_registering.strip()) == 0: 
                    keep_registering = input("No puede dejar esta respuesta vacía, responda nuevamente: ")
                
                else:
                    while keep_registering not in ("SÍ, SI, NO"): 
                        keep_registering = (input("Ingrese una respuesta valida (Sí, No): ")).upper()
            
                    break
            if keep_registering == "NO":
                keep_registering_vehicles = False


    elif selected_option == "2":
        clear_screen()
        print("---------------------- REPRESENTACIÓN PARQUEADERO -----------------------")
        print()
        parking_matrix_to_show = parking_lot.print_square_matrix()
        print()
        print("-"*73)
        print("\nPresiona enter para volver al menú principal")
        input("")


    elif selected_option == "3":
        clear_screen()
        print("\n*************************** BUSCAR  VEHÍCULO ***************************")
        vehicle_license_plate_to_find = input("\nIngrese la matrícula del vehículo a buscar: ")
        while len(vehicle_license_plate_to_find.strip()) == 0: 
            vehicle_license_plate_to_find = input("Debe digitar una matrícula para buscar, ingrese nuevamente: ")

        vehicle_location = parking_lot.determine_vehicle_location(vehicle_license_plate_to_find)
        if vehicle_location is not None:
            print("-"*72)
            print()
            print(f"La ubicación del vehículo con matrícula '{vehicle_license_plate_to_find}' es: {vehicle_location}")
            print()
            print("-"*72)
            print("\nPresiona enter para volver al menú principal")
            input("")
        else: 
            print("-"*72)
            print()
            print(f"El vehículo con matrícula {vehicle_license_plate_to_find} no se encuentra actualmente en el parqueadero.")
            print()
            print("-"*72)
            print("\nPresiona enter para volver al menú principal")
            input("")

    elif selected_option == "4":
        clear_screen()
        keep_registering_vehicle_exits = True
        while keep_registering_vehicle_exits:
            print("********************** REGISTRAR SALIDA VEHÍCULO ***********************")
            vehicle_license_plate_for_exit = input("\nIngrese la matrícula del vehículo que se le va a registrar la salida : ")
            while len(vehicle_license_plate_for_exit.strip()) == 0: 
                    vehicle_license_plate_for_exit = input("\nDebe digitar una matrícula, ingrese nuevamente: ")
                 
            try:
                parking_exit_time = parking_lot.determine_vehicle_exit_time(vehicle_license_plate_for_exit)
                vehicle_stay_hours = parking_lot.determine_vehicle_parking_hours(vehicle_license_plate_for_exit)
                vehicle_amount_to_pay = parking_lot.determine_vehicle_amount_to_pay(vehicle_license_plate_for_exit)

            except ValueError:
                print("-"*72)
                print(f"\nEL vehículo con matrícula {vehicle_license_plate_for_exit} no se encuentra en el parqueadero")
                print()
                print("-"*72)
                print("\nPresiona enter para volver al menú principal")
                input("")
                keep_registering_vehicle_exits = False
                break
            
            print()
            print("-"*72)
            print()
            print(f"Se ha registrado la salida del vehículo con matrícula {vehicle_license_plate_for_exit} con éxito")
            print(f"\nHoras en el parqueadero: {vehicle_stay_hours}")
            print(f"Valor a pagar: {vehicle_amount_to_pay}")
            print()        
            print("-"*72)
            print("\nPresiona enter para volver al menú principal")
            input("")
            keep_registering_vehicle_exits = False

    elif selected_option == "5":
        clear_screen()
        print("---------------------- REPORTE GENERAL PARQUEADERO ----------------------")
        print(f"\nTotal dinero ingresado: {parking_lot.determine_received_money()}")
        print(f"Cantidad vehículos que han ingresado: {parking_lot.determine_vehicles_entered_count()}")
        print(f"Cantidad de puestos totales vendidos: {parking_lot.determine_used_spot_count()}")
        print()
        print("-"*72)
        print("\nPresiona enter para volver al menú principal")
        input("")

    elif selected_option == "6":
        clear_screen()
        if parking_lot.determine_most_used_zone() is None:
            print("-------------------------- ZONA MÁS UTILIZADA --------------------------")
            print("\nNo hay registro de vehículos ingresados en el parqueadero para determinar esto.")
            print("-"*72)
            print("\nPresiona enter para volver al menú principal")
            input("")
        else:
            print("-------------------------- ZONA MÁS UTILIZADA --------------------------")
            print(f"\nLa zona más utilizada en el parqueadero (Zona por precios) es: {parking_lot.determine_most_used_zone()}")
            print()
            print("-"*72)
            print("\nPresiona enter para volver al menú principal")
            input("")

    elif selected_option == "7": 
        clear_screen()
        print("-------------------- TASA OCUPACIÓN DEL PARQUEADERO --------------------")
        print(f"\n La tasa de ocupación del parqueadero es de: {parking_lot.determine_occupancy_rate()}%")
        print()
        print("-"*72)
        print("\nPresiona enter para volver al menú principal")
        input("")
        

    elif selected_option == "8":
        clear_screen()
        print("-------------- TASA OCUPACIÓN POR GENERO EN EL PARQUEADERO --------------")
        print(f"\nPorcentaje de conductores hombres en el parqueadero: {parking_lot.determine_male_occupancy_rate()}%")
        print(f"Porcenta de conductores mujeres en el parqueadero: {parking_lot.determine_female_occupancy_rate()}%")
        print()
        print("-"*72)
        print("\nPresiona enter para volver al menú principal")
        input("")

    elif selected_option == "9":
        clear_screen()
        print("-------------- TASA OCUPACIÓN POR MARCA Y AÑO FABRICACIÓN DE LOS VEHÍCULOS EN EL PARQUEADERO --------------")
        print(f"\nTasa de ocupación por marca: \n{parking_lot.determine_vehicle_percentage_by_brand()}")
        print(f"\nTasa de ocupación por año de fabricación: \n{parking_lot.determine_vehicle_percentage_by_manufacture_year()}")
        print()
        print("-"*107)
        print("\nPresiona enter para volver al menú principal")
        input("")

    elif selected_option == "10":
        clear_screen
        keep_using_program = False
        print("*"*72)
        print("********************* GRACIAS POR USAR EL PROGRAMA *********************")
        print("*"*72)
        print()

    save_drivers(parking_lot.driver_records)
    save_vehicle(parking_lot.vehicle_records)