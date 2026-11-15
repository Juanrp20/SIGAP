from datetime import datetime
from clase_vehículo import Vehículo
from datetime import date

class Conductor:
    def __init__(self, driver_name:str,  driver_birth_date:date, driver_sex:str, driver_identity_document:str) -> None:

        if len(driver_name.strip()) == 0: 
            raise ValueError("La cadena con el nombre del conductor no puede estar vacía")
        
        if driver_birth_date > date.today(): 
            raise ValueError("La fecha de nacimiento no puede ser mayor a la fecha actual")
        
        if len(driver_sex.strip()) == 0: 
            raise ValueError("La cadena con el sexo del conductor no puede estar vacía")
        
        if driver_sex not in ("M", "F"):
            raise ValueError("El sexo biológico del conductor debe estar en el rango aceptado")
              
        if len(driver_identity_document.strip()) == 0: 
            raise ValueError("La cadena con el documento de identidad del conductor no puede estar vacía")
        
        self.driver_name = driver_name
        self.driver_birth_date = driver_birth_date
        self.driver_sex = driver_sex
        self.driver_identity_document = driver_identity_document
        self.vehicles = []

    def __repr__(self) -> str:
        return f"{self.driver_name}, Documento de identidad:{self.driver_identity_document}"
    
        """def asignar_vehículo(self, marca_vehículo : str, matrícula_vehículo:str,  año_fabricación_vehículo:int):
            vehículo = Vehículo(marca_vehículo, matrícula_vehículo, año_fabricación_vehículo, self.documento_de_identidad_conductor)
            self.vehículos.append(vehículo)"""

    def calculate_current_age_in_years(self) -> int:
        today_date = date.today()
        age_in_years = today_date.year - self.driver_birth_date.year
        month_difference = today_date.month - self.driver_birth_date.month
        day_difference = today_date.day - self.driver_birth_date.day
        if month_difference < 0 or (month_difference == 0 and day_difference < 0):
            age_in_years -= 1
        return age_in_years

    def check_legal_age(self)-> bool:
        age_in_years = self.calculate_current_age_in_years()
        is_adult = False
        legal_age_colombia = 18
        if age_in_years >= legal_age_colombia:
            is_adult = True
        return is_adult