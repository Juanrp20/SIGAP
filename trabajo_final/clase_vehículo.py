from datetime import datetime
from datetime import date

class Vehículo: 

    def __init__(self, vehicle_brand: str, vehicle_license_plate: str, vehicle_manufacture_year: int, vehicle_driver_identity_document : str):

        if len(vehicle_brand.strip()) == 0: 
            raise ValueError("La cadena con la marca del vehículo no puede estar vacía")
        
        if len(vehicle_license_plate.strip()) == 0:
            raise ValueError("La cadena con la matrícula del vehículo no puede estar vacía")
        
        if vehicle_manufacture_year > int(date.today().year): 
            raise ValueError("El año de fabricación del veehículo no puede ser mayor al año actual")
        
        if len(vehicle_driver_identity_document.strip()) == 0: 
            raise ValueError("la cadena con el documento de identidad del conductor del vehículo no puede estar vacía")
        
        self.vehicle_brand = vehicle_brand
        self.vehicle_license_plate = vehicle_license_plate
        self.vehicle_entry_time = None
        self.vehicle_exit_time = None
        self.vehicle_manufacture_year = vehicle_manufacture_year
        self.assigned_spot = None
        self.vehicle_owner = vehicle_driver_identity_document
        self.amount_to_pay = 0

    def __repr__(self):
        return f"{self.vehicle_brand} - {self.vehicle_license_plate}"