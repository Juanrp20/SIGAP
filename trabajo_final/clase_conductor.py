from datetime import datetime
from clase_vehículo import Vehículo
from datetime import date

class Conductor:
    def __init__(self, nombre_conductor:str,  fecha_nacimiento_conductor:date, sexo_conductor:str, documento_identidad_conductor:str) -> None:

        if len(nombre_conductor.strip()) == 0: 
            raise ValueError("La cadena con el nombre del conductor no puede estar vacía")
        
        if fecha_nacimiento_conductor > date.today(): 
            raise ValueError("La fecha de nacimiento no puede ser mayor a la fecha actual")
        
        if len(sexo_conductor.strip()) == 0: 
            raise ValueError("La cadena con el sexo del conductor no puede estar vacía")
        
        if sexo_conductor not in ("M", "F"):
            raise ValueError("El sexo biológico del conductor debe estar en el rango aceptado")
              
        if len(documento_identidad_conductor.strip()) == 0: 
            raise ValueError("La cadena con el documento de identidad del conductor no puede estar vacía")
        
        self.nombre_conductor = nombre_conductor
        self.fecha_nacimiento_conductor = fecha_nacimiento_conductor
        self.sexo_conductor = sexo_conductor
        self.documento_identidad_conductor = documento_identidad_conductor
        self.vehículos = []

    def __repr__(self) -> str:
        return f"{self.nombre_conductor}, Documento de identidad:{self.documento_identidad_conductor}"
    
        """def asignar_vehículo(self, marca_vehículo : str, matrícula_vehículo:str,  año_fabricación_vehículo:int):
            vehículo = Vehículo(marca_vehículo, matrícula_vehículo, año_fabricación_vehículo, self.documento_de_identidad_conductor)
            self.vehículos.append(vehículo)"""

    def calcular_edad_actual_en_años(self) -> int:
        fecha_de_hoy = date.today()
        edad_en_años = fecha_de_hoy.year - self.fecha_nacimiento_conductor.year
        diferencia_meses = fecha_de_hoy.month - self.fecha_nacimiento_conductor.month
        diferencia_días = fecha_de_hoy.day - self.fecha_nacimiento_conductor.day
        if diferencia_meses < 0 or (diferencia_meses == 0 and diferencia_días < 0):
            edad_en_años -= 1
        return edad_en_años

    def comprobar_mayoria_edad(self)-> bool:
        edad_en_años = self.calcular_edad_actual_en_años()
        mayor_edad = False
        mayoria_edad_colombia = 18
        if edad_en_años >= mayoria_edad_colombia:
            mayor_edad = True
        return mayor_edad