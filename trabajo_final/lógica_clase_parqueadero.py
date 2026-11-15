from datetime import date
from datetime import datetime
from clase_conductor import Conductor
from clase_vehículo import Vehículo
import math

class Parqueadero:
    def __init__(self, name : str,  parking_spot_count : int):

        if len(name.strip()) == 0: 
            raise ValueError("El nombre no puede ser una cadena vacía")

        if parking_spot_count not in (36, 64 , 100):
            raise ValueError("El largo del parqueadero debe estar en el rango estipulado")
        
        parking_side_length = int(math.sqrt(parking_spot_count))
        
        self.name = name
        self.parking_spot_count = parking_spot_count
        self.rows = parking_side_length
        self.columns = parking_side_length
        self.row_letters = []
        for i in range(parking_side_length):
            self.row_letters.append(chr(i+65))
        self.parking_lot = [[None for _ in range(parking_side_length)] for _ in range(parking_side_length)]
        self.driver_records = []
        self.vehicle_records = []
        self.prices = []

    def determine_assigned_spots_matrix(self): 
        for vehicle in self.vehicle_records: 
            if vehicle.vehicle_exit_time is None:
                spot_letter_index = self.row_letters.index(vehicle.assigned_spot[0])
                spot_number_index = (int(vehicle.assigned_spot[1])-1)
                self.parking_lot[spot_letter_index][spot_number_index] = vehicle

    #--------------------------------- HISTOyoRIA USUARIO #1 -------------------------------------------
        
    def determine_min_spot_price(self):
        min_price = len(self.parking_lot)*1000
        return min_price

    def determine_max_spot_price(self):
        max_price = self.determine_min_spot_price() * (len(self.parking_lot)/2)
        return max_price
    
    def calculate_spot_cost(self,letter:str, column_number:int) -> float:

        if len(letter.strip()) == 0: 
            raise ValueError("La cadena con la letra del puesto no puede estar vacía")
        
        if letter not in self.row_letters: 
            raise ValueError("La cadena con la letra del puesto debe estar entre el rango estipulado")
        
        if column_number not in range((self.columns)): 
            raise ValueError("El número de la columna debe estar entre el rango aestipulado")
        
        row = self.row_letters.index(letter)
        column = column_number

        rows_distance_to_top_edge = row
        rows_distance_to_bottom_edge = (len(self.parking_lot)-1)-row
        if rows_distance_to_top_edge > rows_distance_to_bottom_edge:
            min_row_distance = rows_distance_to_bottom_edge
        else:
            min_row_distance = rows_distance_to_top_edge
        #Determina que tan cerca está de los bordes de manera vertical

        column_distance_to_left_edge = column
        column_distance_to_right_edge = (len(self.parking_lot[0])-1)-column
        if column_distance_to_left_edge > column_distance_to_right_edge:
            min_column_distance = column_distance_to_right_edge
        else:
            min_column_distance = column_distance_to_left_edge
        #determina que tan cerca está de los bordes de manera horizontal

        if min_row_distance > min_column_distance:
            min_distance_to_edge = min_column_distance
        else:
            min_distance_to_edge = min_row_distance
        #Determina que tan cerca está a un borde en general, el valor 0 es que está pegado
        spot_price = self.determine_max_spot_price() - self.determine_min_spot_price() * min_distance_to_edge
        return int(spot_price)
    
    #--------------------------------- HISTORIA USUARIO #2 -------------------------------------------
    def assign_vehicle(self, vehicle_brand, vehicle_license_plate, vehicle_manufacture_year, vehicle_driver_identity_document):
        
        vehicle = Vehículo(vehicle_brand, vehicle_license_plate, vehicle_manufacture_year, vehicle_driver_identity_document)
        self.vehicle_records.append(vehicle)    
                                                              
    def determine_vehicle_age_years(self, manufacture_year : int) -> int:
        current_year = int(date.today().year)
        if manufacture_year <= current_year:
            age_in_years = current_year - manufacture_year
            return age_in_years
        else: 
            raise ValueError("El año de fabricación del vehículo no puede ser mayor que el año actual")
           
    def determine_parking_zone_prices(self): 
        min_price = self.determine_min_spot_price()
        for zone in range(int(len(self.parking_lot)/2)):
            zone_price = min_price*(zone+1)
            self.prices.append(zone_price)

    def determine_vehicle_entry_time(self, vehicle_license_plate : str):
        if len(vehicle_license_plate.strip()) == 0: 
            raise ValueError("la cadena con la matrícula del vehículo no puede estar vacía")
        
        for row in range(0, self.rows):
            for column in range(0, self.columns):
                if self.parking_lot[row][column] is not None:
                    if self.parking_lot[row][column].vehicle_license_plate == vehicle_license_plate:
                        self.parking_lot[row][column].vehicle_entry_time = datetime.now()
                        return self.parking_lot[row][column].vehicle_entry_time
                    

    def assign_parking_spot(self, price : int,driver_name:str, driver_birth_date:date, driver_sex:str, vehicle_brand:str, 
                       vehicle_license_plate:str, vehicle_manufacture_year :int, driver_identity_document : str):
        self.determine_parking_zone_prices()
        
        if price not in self.prices:
            raise ValueError("La preferencia de precio debe estar entre el rango aceptable")
        
        vehicle_in_parking = False
        for row in range(0, self.rows):
            for column in range(0, self.columns):
                if self.parking_lot[row][column] is not None:
                    if self.parking_lot[row][column].vehicle_license_plate == vehicle_license_plate: 
                        vehicle_in_parking = True

        if vehicle_in_parking: 
            raise ValueError("El vehículo a asignar en el parqueadero noo puede ser uno que ya está asignado")
         
        driver = Conductor(driver_name, driver_birth_date, driver_sex, driver_identity_document)
        assign_parking_spot = False
        verified_spots_matrix = 0
     
        if driver.check_legal_age():
            MAX_VEHICLE_AGE = 10
            if self.determine_vehicle_age_years(vehicle_manufacture_year) <= MAX_VEHICLE_AGE:
                for row in range(0, self.rows):
                    for column in range(0, self.columns):
                        verified_spots_matrix += 1
                
                        if self.parking_lot[row][column] is None:
                            if self.calculate_spot_cost(self.row_letters[row], column) == price:
                          
                                if driver not in self.driver_records:
                                    self.driver_records.append(driver)
                                self.assign_vehicle(vehicle_brand, vehicle_license_plate, vehicle_manufacture_year, driver_identity_document)
                                self.parking_lot[row][column] = self.vehicle_records[((len(self.vehicle_records))-1)]
                                self.parking_lot[row][column].assigned_spot = (self.row_letters[row], column+1)
                                self.determine_vehicle_entry_time(vehicle_license_plate)                                
                                return (self.row_letters[row], column+1)
                        
                if verified_spots_matrix == self.parking_spot_count:
                    raise ValueError("No se encontró puestos disponibles con ese precio")
            else:
                raise ValueError("El auto no debe tener más de 10 años de antigüedad")
        else:
            raise ValueError("El conductor debe ser mayor de edad")
        return assign_parking_spot
    
    #--------------------------------- HISTORIA USUARIO #3 -------------------------------------------
        
    def show_occupied_spots(self):
        occupied = [["Disponible" for _ in range(self.rows)] for _ in range(self.columns)]

        for row in range(0, self.rows):
            for column in range(0, self.columns):
                if self.parking_lot[row][column] is not None:
                    occupied[row][column] = "Ocupado"
        return occupied
    
    def print_square_matrix(self):
        matrix = self.show_occupied_spots()

        for row in matrix:
            print(" ".join(f"{element:10}" for element in row))
    
    #--------------------------------- HISTORIA USUARIO #4 -------------------------------------------
            
                  
    def determine_vehicle_in_cell(self, row_letter:str, column:int):
        if len(row_letter.strip()) == 0: 
            raise ValueError("La cadena la letra de la fila no puede estar vacía")
        
        if row_letter not in self.row_letters: 
            raise ValueError("La letra de la fila debe estar en el rango estipulado")
        
        if column not in range(1, (self.columns +1)):
            raise ValueError("La columna ingresada debe estar entre el rango estipulado")
        
        vehicle_in_cell = None
        row_index = self.row_letters.index(row_letter)
        column_index = column - 1
        vehicle_driver_in_cell = None

        if self.parking_lot[row_index][column_index] is not None: 
            vehicle_in_cell = self.parking_lot[row_index][column_index]

            for driver in self.driver_records:
                if driver.driver_identity_document == vehicle_in_cell.vehicle_owner: 
                    vehicle_driver_in_cell = driver

        return (vehicle_in_cell, vehicle_driver_in_cell)
    
    def determine_vehicle_location(self, vehicle_license_plate : str): 
        if len(vehicle_license_plate.strip()) == 0: 
            raise ValueError("la cadena con la matrícula del vehículo no puede estar vacía")
        
        for row in range(0, self.rows):
            for column in range(0, self.columns):
                if self.parking_lot[row][column] is not None:
                    if self.parking_lot[row][column].vehicle_license_plate == vehicle_license_plate:
                        return (self.row_letters[row], column+1)
        return None
                    
    #--------------------------------- HISTORIA USUARIO #5-6 -------------------------------------------

    def determine_vehicle_exit_time(self, vehicle_license_plate : str,):
        if len(vehicle_license_plate.strip()) == 0: 
            raise ValueError("la cadena con la matrícula del vehículo no puede estar vacía")
        
        for row in range(0, self.rows):
            for column in range(0, self.columns):
                if self.parking_lot[row][column] is not None:
                    if self.parking_lot[row][column].vehicle_license_plate == vehicle_license_plate:
                        self.parking_lot[row][column].vehicle_exit_time = datetime.now()
                        return self.parking_lot[row][column].vehicle_exit_time
    
    def determine_vehicle_exit_from_parking(self, vehicle_license_plate : str): 
        if len(vehicle_license_plate.strip()) == 0: 
            raise ValueError("la cadena con la matrícula del vehículo no puede estar vacía")
        
        for row in range(0, self.rows):
            for column in range(0, self.columns):
                if self.parking_lot[row][column] is not None:
                    if self.parking_lot[row][column].vehicle_license_plate == vehicle_license_plate:
                        self.parking_lot[row][column] = None
                        break

    def determine_vehicle_parking_hours(self, vehicle_license_plate: str):
        if len(vehicle_license_plate.strip()) == 0:
            raise ValueError("La cadena con la matrícula del vehículo no puede estar vacía")
        
        vehicle_departure_time = self.determine_vehicle_exit_time(vehicle_license_plate)
        if vehicle_departure_time is None:
            raise ValueError("La hora de egreso del vehículo no está registrada")
        
        for row in range(self.rows):
            for column in range(self.columns):
                space = self.parking_lot[row][column]
                if space and space.vehicle_license_plate == vehicle_license_plate:
                    vehicle_entry_time = space.vehicle_entry_time
                    if vehicle_entry_time is None:
                        raise ValueError("La hora de ingreso del vehículo no está registrada")
                    hour_difference = ((vehicle_departure_time - vehicle_entry_time).total_seconds() // 3600) + 1
                    return int(hour_difference)
        
        raise ValueError("El vehículo con la matrícula proporcionada no se encontró en el parqueadero")


    def determine_vehicle_amount_to_pay(self, vehicle_license_plate : str):
        if len(vehicle_license_plate.strip()) == 0: 
            raise ValueError("la cadena con la matrícula del vehículo no puede estar vacía")
        
        calculate_cell_cost = 0
        calculate_vehicle_stay_hours = 0
        vehicle_amount_to_pay = 0
        for row in range(self.rows):
            for column in range(self.columns):
                if self.parking_lot[row][column] is not None:
                    if self.parking_lot[row][column].vehicle_license_plate == vehicle_license_plate: 
                            
                        calculate_cell_cost = self.calculate_spot_cost(self.parking_lot[row][column].assigned_spot[0], self.parking_lot[row][column].assigned_spot[1])
                        calculate_vehicle_stay_hours = self.determine_vehicle_parking_hours(vehicle_license_plate)
                        vehicle_amount_to_pay = (calculate_cell_cost * calculate_vehicle_stay_hours)
                        self.parking_lot[row][column].amount_to_pay = vehicle_amount_to_pay
                        self.determine_vehicle_exit_from_parking(vehicle_license_plate)

                        return vehicle_amount_to_pay

    #--------------------------------- HISTORIA USUARIO #7 -------------------------------------------

    def sold_spots(self): 
        sold_spots = []

        for vehicle in self.vehicle_records:
            if vehicle.vehicle_exit_time != 0:
                spot = vehicle.assigned_spot
                spot_total_payment = vehicle.amount_to_pay
                sold_spots.append((spot, spot_total_payment))

        return sold_spots

    def determine_received_money(self): 
        total_income = 0 
        sold_spot_records = self.sold_spots()
        for cell in range(0, len(sold_spot_records)): 
            total_income += sold_spot_records[cell][1]
        return total_income
    
    def determine_vehicles_entered_count(self): 
        registered_license_plates = []
        for vehicle in self.vehicle_records:
            if vehicle.vehicle_license_plate not in registered_license_plates:
                registered_license_plates.append(vehicle.vehicle_license_plate)
    
        vehicles_entered_count = int(len(registered_license_plates))
        return vehicles_entered_count
    
    def determine_used_spot_count(self): 
        total_used_spots = 0 
        sold_spot_records = self.sold_spots()
        total_used_spots = int(len(sold_spot_records))
        return total_used_spots 
    
        #--------------------------------- HISTORIA USUARIO #8 -------------------------------------------
    def determine_parking_zone_count(self): 
        parking_zone_prices = {}
        max_price = int(self.determine_max_spot_price())
        min_price = int(self.determine_min_spot_price())
        parking_zone_count = int(max_price/min_price)

        for zone in range(1, parking_zone_count+1):
            parking_zone_prices.setdefault(f"Zona {zone}", zone*min_price)
        return parking_zone_prices
    
    def determine_most_used_zone(self): 
        max_price = self.determine_max_spot_price()
        min_price = self.determine_min_spot_price()
        parking_zone_count = int(max_price/min_price)

        zones = [0 for _ in range(parking_zone_count)]
        if len(self.vehicle_records) == 0:
            return None
        else:
            for vehicles in self.vehicle_records:
                zones[int(((self.calculate_spot_cost(vehicles.assigned_spot[0], vehicles.assigned_spot[1]))/min_price)-1)]+=1
            max_zone_index = 0

            for zone in range(int(parking_zone_count-1)):
                if zones[max_zone_index] < zones[zone+1]:
                    max_zone_index = zone+1
        return (max_zone_index+1)*min_price

    def determine_occupancy_rate(self): 
        occupied_spot_count = 0
        occupancy_rate = 0
        parking_spot_count = self.parking_spot_count

        for row in range(0, self.rows):
            for column in range(0, self.columns):
                if self.parking_lot[row][column] is not None:
                    occupied_spot_count += 1
        
        occupancy_rate = (occupied_spot_count / parking_spot_count) * 100

        return round(occupancy_rate, 2)
    
        #--------------------------------- HISTORIA USUARIO #9 -------------------------------------------

    def determine_male_occupancy_rate(self):
        total_drivers = 0
        male_drivers = 0
        
        for row in range(self.rows):
            for column in range(self.columns):
                if self.parking_lot[row][column] is not None:
                    document = self.parking_lot[row][column].vehicle_owner
                
                    for driver in self.driver_records:
                        if driver.driver_identity_document == document:
                            total_drivers += 1
                            if driver.driver_sex == "M":
                                male_drivers += 1
                            break  
        if total_drivers == 0:
            return 0
        
        male_parking_occupancy_rate = (male_drivers / total_drivers) * 100

        return round(male_parking_occupancy_rate, 2)

    def determine_female_occupancy_rate(self): 
        driver_gender_list_using_parking = []
        female_driver_count = 0
        female_parking_occupancy_rate = 0
        for row in range(0, self.rows):
            for column in range(0, self.columns):
                if self.parking_lot[row][column] is not None:
                    for driver in self.driver_records: 
                        if self.parking_lot[row][column].vehicle_owner == driver.driver_identity_document:
                            driver_gender_list_using_parking.append(driver.driver_sex) 
        if len(driver_gender_list_using_parking) == 0:
            return 0
        for cell_iteration in range(0, len(driver_gender_list_using_parking)):
           if driver_gender_list_using_parking[cell_iteration] == "F":
               female_driver_count += 1

        female_parking_occupancy_rate = (female_driver_count/len(driver_gender_list_using_parking))*100

        return round(female_parking_occupancy_rate, 2)

    
    #--------------------------------- HISTORIA USUARIO #10 -------------------------------------------
    
    def determine_vehicle_percentage_by_brand(self):
        total_parked_vehicles = 0
        quantity_by_brand = {}
        for vehicle in self.vehicle_records:
            if vehicle.vehicle_exit_time is None:
                brand = vehicle.vehicle_brand
                if brand not in quantity_by_brand:
                    quantity_by_brand[brand] = 0
                quantity_by_brand[brand] += 1
                total_parked_vehicles += 1
        

        percentages_by_brand = {}
        for brand, quantity in quantity_by_brand.items():
            percentages_by_brand[brand] = (quantity / total_parked_vehicles) * 100

        return percentages_by_brand
    
    def get_percentage_by_brand(self, vehicle_brand : str):
        if len(vehicle_brand.strip())  == 0: 
            raise ValueError("La cadena con la marca del vehículo no puede estar vacía") 
        
        percentages = self.determine_vehicle_percentage_by_brand()
        return percentages.get(vehicle_brand, 0)
    
    def determine_vehicle_percentage_by_manufacture_year(self):
        total_parked_vehicles = 0
        quantity_by_year = {}
        for vehicle in self.vehicle_records:
            if vehicle.vehicle_exit_time is None:
                manufacture_year = vehicle.vehicle_manufacture_year
                if manufacture_year not in quantity_by_year:
                    quantity_by_year[manufacture_year] = 0
                quantity_by_year[manufacture_year] += 1
                total_parked_vehicles += 1
        

        percentages_by_year = {}
        for manufacture_year, quantity in quantity_by_year.items():
            percentages_by_year[manufacture_year] = (quantity / total_parked_vehicles) * 100

        return percentages_by_year