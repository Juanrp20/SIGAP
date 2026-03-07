from lógica_clase_parqueadero import Parqueadero
from clase_vehículo import Vehículo
from clase_conductor import Conductor
from datetime import datetime
from datetime import date
import ast
import csv


def guardar_parqueaderos(parqueadero : Parqueadero):
    lista_parqueadero = []
    lista_parqueadero.append(parqueadero)

    with open("parqueaderos.csv", mode= 'w', newline= '') as archivo: 
        nombres_columnas = ['nombre_parqueadero', 'cantidad_puestos_parqueadero']
        escritor = csv.DictWriter(archivo, fieldnames=nombres_columnas)
        escritor.writeheader()

        for parqueadero in lista_parqueadero:
            escritor.writerow({
                'nombre_parqueadero' : parqueadero.nombre, 
                'cantidad_puestos_parqueadero' : parqueadero.cantidad_puestos_parqueadero
            })

def leer_parqueaderos() -> list:
    parqueaderos_registrados = []
    with open("parqueaderos.csv", mode='r', newline='') as archivo: 
        lector = csv.DictReader(archivo)

        for fila in lector: 
            nombre_parqueadero = fila['nombre_parqueadero']
            cantidad_puestos_parqueadero = int(fila['cantidad_puestos_parqueadero'])
            parqueaderos_registrados.append(Parqueadero(nombre_parqueadero, cantidad_puestos_parqueadero))
    return parqueaderos_registrados

def guardar_conductor_vehículo(registro_conductores : list):
    with open('registro_conductores.csv', mode='w', newline='') as archivo: 
        nombres_columnas = ['nombre_conductor', 'fecha_nacimiento_conductor', 'sexo_conductor', 'documento_identidad_conductor']
        escritor = csv.DictWriter(archivo, fieldnames=nombres_columnas)
        escritor.writeheader()

        for conductor in registro_conductores: 
            escritor.writerow({
                'nombre_conductor' : conductor.nombre_conductor,
                'fecha_nacimiento_conductor' : conductor.fecha_nacimiento_conductor,
                'sexo_conductor' : conductor.sexo_conductor,
                'documento_identidad_conductor' : conductor.documento_identidad_conductor
            })

def leer_conductor_vehículo() -> list: 
    registro_conductores = []
    with open('registro_conductores.csv', mode='r', newline='') as archivo:
        lector = csv.DictReader(archivo)

        for fila in lector: 
            nombre_conductor = fila['nombre_conductor']
            fecha_nacimiento_conductor = (datetime.strptime(fila['fecha_nacimiento_conductor'], "%Y-%m-%d")).date()
            sexo_conductor = fila['sexo_conductor']
            documento_identidad_conductor = fila['documento_identidad_conductor']
            registro_conductores.append(Conductor(nombre_conductor, fecha_nacimiento_conductor, sexo_conductor, documento_identidad_conductor))
        return registro_conductores

def guardar_vehículo(lista_vehículos : list): 
    with open('registro_vehículos.csv', mode='w', newline='') as archivo: 
        nombres_columnas = ['marca_vehículo', 'matrícula_vehículo','año_fabricación_vehículo', 'documento_identidad_conductor_vehículo', 
                            'hora_ingreso_vehículo', 'hora_egreso_vehículo', 'puesto_asignado']
        escritor = csv.DictWriter(archivo, fieldnames=nombres_columnas)
        escritor.writeheader()

        for vehículo in lista_vehículos:
            hora_ingreso_str = vehículo.hora_ingreso_vehículo.strftime('%Y-%m-%d %H:%M:%S') if vehículo.hora_ingreso_vehículo else ''
            hora_egreso_str = vehículo.hora_egreso_vehículo.strftime('%Y-%m-%d %H:%M:%S') if vehículo.hora_egreso_vehículo else ''
       
            escritor.writerow({
                'marca_vehículo' : vehículo.marca_vehículo,
                'matrícula_vehículo' : vehículo.matrícula_vehículo,
                'año_fabricación_vehículo' : vehículo.año_fabricación_vehículo,
                'documento_identidad_conductor_vehículo': vehículo.dueño_del_vehículo,
                'hora_ingreso_vehículo': hora_ingreso_str,
                'hora_egreso_vehículo': hora_egreso_str,
                'puesto_asignado' : vehículo.puesto_asignado 

            })

def leer_vehículo() -> list:
    lista_vehículos = []
    with open('registro_vehículos.csv', mode='r', newline='') as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector: 
            marca_vehículo = fila['marca_vehículo']
            matrícula_vehículo = fila['matrícula_vehículo']
            año_fabricación_vehículo = int(fila['año_fabricación_vehículo'])
            dueño_vehículo = fila['documento_identidad_conductor_vehículo']

            if fila['hora_ingreso_vehículo']:
                hora_ingreso_vehículo = datetime.strptime(fila['hora_ingreso_vehículo'], '%Y-%m-%d %H:%M:%S')
            else:
                hora_ingreso_vehículo = None

            if fila['hora_egreso_vehículo']:
                hora_egreso_vehículo = datetime.strptime(fila['hora_egreso_vehículo'], '%Y-%m-%d %H:%M:%S')
            else:
                hora_egreso_vehículo = None

            puesto_asignado = ast.literal_eval(fila['puesto_asignado'])
            lista_vehículos.append(Vehículo(marca_vehículo, matrícula_vehículo, año_fabricación_vehículo, dueño_vehículo))
            
            lista_vehículos[(len(lista_vehículos)-1)].hora_ingreso_vehículo = hora_ingreso_vehículo
            lista_vehículos[(len(lista_vehículos)-1)].hora_egreso_vehículo = hora_egreso_vehículo
            lista_vehículos[(len(lista_vehículos)-1)].puesto_asignado = puesto_asignado

        return lista_vehículos