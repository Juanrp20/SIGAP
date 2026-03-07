from datetime import datetime
from datetime import date

class Vehículo: 

    def __init__(self, marca_vehículo: str, matrícula_vehículo: str, año_fabricación_vehículo: int, documento_identidad_conductor_vehículo : str):

        if len(marca_vehículo.strip()) == 0: 
            raise ValueError("La cadena con la marca del vehículo no puede estar vacía")
        
        if len(matrícula_vehículo.strip()) == 0:
            raise ValueError("La cadena con la matrícula del vehículo no puede estar vacía")
        
        if año_fabricación_vehículo > int(date.today().year): 
            raise ValueError("El año de fabricación del veehículo no puede ser mayor al año actual")
        
        if len(documento_identidad_conductor_vehículo.strip()) == 0: 
            raise ValueError("la cadena con el documento de identidad del conductor del vehículo no puede estar vacía")
        
        self.marca_vehículo = marca_vehículo
        self.matrícula_vehículo = matrícula_vehículo
        self.hora_ingreso_vehículo = None
        self.hora_egreso_vehículo = None
        self.año_fabricación_vehículo = año_fabricación_vehículo
        self.puesto_asignado = None
        self.dueño_del_vehículo = documento_identidad_conductor_vehículo
        self.valor_a_pagar = 0

    def __repr__(self):
        return f"{self.marca_vehículo} - {self.matrícula_vehículo}"