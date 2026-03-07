from lógica_clase_parqueadero import Parqueadero
import os
import platform
from datetime import datetime
from datetime import date
from programa_para_guardar import (
    guardar_parqueaderos,
    leer_parqueaderos,
    guardar_conductor_vehículo,
    leer_conductor_vehículo,
    guardar_vehículo,
    leer_vehículo
)

#----------------------------------- FUNCIONALIDADES DE LA INTERFAX DE USUARIO --------------------------------------------------

def clear_screen():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def mostrar_menú_inicio():
    print("***********************************************************************")
    print("**************** BIENVENIDO AL PROGRAMA DE PARQUEADERO ****************")
    print("***********************************************************************")
    print("\n1. Crear parqueadero")
    print("2. Salir del programa")
    print("\n***********************************************************************")

def mostrar_menú_inicio_con_clase_creada():
    print("*"*71)
    print("**************** BIENVENIDO AL PROGRAMA DE PARQUEADERO ****************")
    print("*"*71)
    print(f"\nYa ha creado un parqueadero anteriormente con el nombre de {parqueadero.nombre}.")
    print()
    print("-"*71)
    input("\nPresione enter para ir al menú de opciones.")

def mostrar_tipos_parqueaderos():
    print("\n------------------------- TIPOS DE PARQUEADERO -------------------------")
    print("1. 36 puestos\n2. 64 puestos\n3. 100 puestos")
    print("-"*72)

def mostrar_menú_parqueadero():
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
 
def mostrar_zonas_y_precios_del_parqueadero():
    print("\n---------------- TIPOS ZONAS PARQUEADERO ----------------")
    print()
    for clave, valor in parqueadero.determinar_cantidad_zonas_parqueaderos().items():
        print(f"{clave} : {valor}")
    print("-"*57)


#--------------------------------------------------- INTERFAZ DE USUARIO ---------------------------------------------------

if os.path.exists("parqueaderos.csv"):
    lista_clase_parqueadero = leer_parqueaderos()
    parqueadero = lista_clase_parqueadero[0]
    mostrar_menú_inicio_con_clase_creada()
    if os.path.exists('registro_conductores.csv'):
        parqueadero.registro_conductores = leer_conductor_vehículo()

        if os.path.exists('registro_vehículos.csv'):
            parqueadero.registro_vehículos = leer_vehículo()
            parqueadero.determinar_puestos_asignados_matriz()

else:
    

    mostrar_menú_inicio()
    opción_seleccionada = input("Seleccione el número de la opción a realizar: ")
    valores_válidos = ("1", "2")
    while opción_seleccionada not in valores_válidos:
        opción_seleccionada = input("Ingrese una opción válida: ")



    if opción_seleccionada == valores_válidos[0]: 
        clear_screen()
        print("\n--------------------------- DATOS NECESARIOS ---------------------------")

        nombre_parqueadero = input("\n Escriba el nombre del parqueadero: ")
        while len(nombre_parqueadero.strip()) == 0:
            nombre_parqueadero = input("El nombre del parqueadero no puede estar vacío: ")
        
        clear_screen()
        mostrar_tipos_parqueaderos()

        cantidad_puestos_parqueadero_cadena = input("Ahora, seleccione la cantidad de puestos del parqueadero teniendo en cuenta los tipos posibles: ")
        while cantidad_puestos_parqueadero_cadena not in ("36", "64", "100") or len(cantidad_puestos_parqueadero_cadena.strip()) == 0:
            cantidad_puestos_parqueadero_cadena = input("Ingrese una cantidad de puestos válida: ")
        cantidad_puestos_parqueadero = int(cantidad_puestos_parqueadero_cadena)
        print("-"* 70)
        parqueadero = Parqueadero(nombre_parqueadero, cantidad_puestos_parqueadero)
        opción_seleccionada = None
        print("Parqueadero creado con éxito!\n")
        guardar_parqueaderos(parqueadero)

    elif opción_seleccionada == valores_válidos[1]: 
        clear_screen()
        opción_seleccionada = None
        print("-"*72)
        print("--------------------- GRACIAS POR USAR EL PROGRAMA ---------------------")
        print("-"*72)

        raise SystemExit

seguir_utilizando_programa = True
while seguir_utilizando_programa:
    clear_screen()
    mostrar_menú_parqueadero()
    opción_seleccionada = input("\nSelecciones la opción que necesite: ")
    print()
    while opción_seleccionada not in ("1","2","3","4","5","6","7","8","9","10"):
        opción_seleccionada = input("Ingrese una opción válida: ")
    


    if opción_seleccionada == "1":
        
        seguir_registrando_vehículos = True
        while seguir_registrando_vehículos:
            clear_screen()
            print("\n************************** REGISTRAR VEHÍCULO **************************")
            print()
            print("------------------ Datos Necesarios para el registro -------------------")
            print()

            nombre_conductor = input("Ingrese el nombre del conductor del vehículo: ")
            while len(nombre_conductor.strip()) == 0:
                nombre_conductor = input("El nombre del conductor no puede estar vacío: ")

            
            fecha_de_nacimiento_conductor_cadena = input("Ingrese la fecha de nacimiento del conductor (AÑO-MES-DÍA), ejemplo: 2000-01-02: ")
            seguir_pidiendo_fecha_nacimiento = True
            while seguir_pidiendo_fecha_nacimiento: 
                if len(fecha_de_nacimiento_conductor_cadena.strip()) == 0: 
                    fecha_de_nacimiento_conductor_cadena = input("La fecha de nacimiento del conductor no puede estar vacía: ")

                elif len(fecha_de_nacimiento_conductor_cadena.strip()) != 0:
                    try:
                        fecha_de_nacimiento_conductor = datetime.strptime(fecha_de_nacimiento_conductor_cadena, "%Y-%m-%d")

                        fecha_de_nacimiento_conductor_date = fecha_de_nacimiento_conductor.date()
                        if fecha_de_nacimiento_conductor_date > date.today(): 
                            fecha_de_nacimiento_conductor_cadena = input("La fecha de nacimiento del conductor no puede ser mayor a la fecha actual, ingrese nuevamente: ")
                        else:
                            break

                    except ValueError:
                        fecha_de_nacimiento_conductor_cadena = input("Ingrese una fecha de nacimiento valida: ")
            fecha_de_nacimiento_conductor = (datetime.strptime(fecha_de_nacimiento_conductor_cadena, "%Y-%m-%d")).date()

            sexo_biológico_del_conductor = (input("Ingrese el sexo biológico del conductor del vehículo (M: Masculino, F: Femenino): ")).upper()
            while len(sexo_biológico_del_conductor.strip()) == 0 or sexo_biológico_del_conductor not in ("M", "F"):
                sexo_biológico_del_conductor = (input("Ingrese un valor valido para el sexo del conductor: ")).upper()

            documento_identidad_conductor = input("Ingrese el documento de identidad del conductor: ")
            while len(documento_identidad_conductor.strip()) == 0:
                documento_identidad_conductor = input("El documento de identida del conductor no puede estar vacío, ingrese nuevamente: ")

            print("\n---------------------------- Datos vehículo ----------------------------")
            marca_vehículo = input("\nIngrese la marca del vehículo a registrar: ")
            while len(marca_vehículo.strip()) == 0:
                marca_vehículo = input("No puede dejar esto vacío, ingrese una marca valida: ")

            matrícula_vehículo = input("Ingrese la matrícula del vehículo a registrar: ")
            while len(matrícula_vehículo.strip()) == 0: 
                matrícula_vehículo = input("No puede dejar esto vacío, ingrese una matrícula valida: ")

            año_fabricación_vehículo_cadena = input("Ingrese el año de fabricación del vehículo a asignar (Año : XXXX): ")
            while True:
                while len(año_fabricación_vehículo_cadena.strip()) == 0:
                    año_fabricación_vehículo_cadena = input("No puede dejar esto vacío, ingrese nuevamente el año de fabricación del vehículo: ")
                año_fabricación_vehículo = int(año_fabricación_vehículo_cadena)

                if año_fabricación_vehículo > int(date.today().year):
                    año_fabricación_vehículo_cadena = input("El año de fabricación no puede ser mayor al año actual: ")
                else: 
                    break

                
            mostrar_zonas_y_precios_del_parqueadero()

            preferencia_precio_cadena = input("Ingrese el valor monetario de la zona dónde se quiere ubicar: ")
            while True: 
                if len(preferencia_precio_cadena.strip()) == 0: 
                    preferencia_precio_cadena = input("La preferencia de precio no puede estar vacía,  ingrese nuevamente: ")
                
                else: 
                    try: 
                        preferencia_precio = int(preferencia_precio_cadena)

                        if preferencia_precio not in parqueadero.determinar_cantidad_zonas_parqueaderos().values(): 
                            preferencia_precio_cadena = input("La preferencia de precio debe estar entre los valores disponibles: ")
                        
                        else: 
                            break
                    
                    except ValueError: 
                        preferencia_precio_cadena = input("La preferencia de precio debe ser un número: ")
            
            try:
                puesto_vehículo_asignado = parqueadero.asignar_puesto(preferencia_precio, nombre_conductor, fecha_de_nacimiento_conductor, sexo_biológico_del_conductor, marca_vehículo, matrícula_vehículo, año_fabricación_vehículo, documento_identidad_conductor)

            except ValueError:
                print("-"*72)
                print("---------------- No fue posible registrar el vehículo ------------------")
                print("-"*72)
                print("\nPresiona enter para volver al menú principal")
                input("")

                break
            
            print("-"*72)
            print("\nEl vehículo ha sido ingresado correctamente!!")
            print(f"\nVehículo ubicado en puesto : {puesto_vehículo_asignado[0]}{puesto_vehículo_asignado[1]}")
            print()
            print("-"*72)

            seguir_registrando_cadena = input("¿Desea seguir registrando vehículos (Sí, No): ")
            seguir_registrando = seguir_registrando_cadena.upper()
            while True:
                if len(seguir_registrando.strip()) == 0: 
                    seguir_registrando = input("No puede dejar esta respuesta vacía, responda nuevamente: ")
                
                else:
                    while seguir_registrando not in ("SÍ, SI, NO"): 
                        seguir_registrando = (input("Ingrese una respuesta valida (Sí, No): ")).upper()
            
                    break
            if seguir_registrando == "NO":
                seguir_registrando_vehículos = False


    elif opción_seleccionada == "2":
        clear_screen()
        print("---------------------- REPRESENTACIÓN PARQUEADERO -----------------------")
        print()
        matriz_parqueadero_mostrar = parqueadero.imprimir_matriz_cuadrada()
        print()
        print("-"*73)
        print("\nPresiona enter para volver al menú principal")
        input("")


    elif opción_seleccionada == "3":
        clear_screen()
        print("\n*************************** BUSCAR  VEHÍCULO ***************************")
        matrícula_vehículo_a_buscar = input("\nIngrese la matrícula del vehículo a buscar: ")
        while len(matrícula_vehículo_a_buscar.strip()) == 0: 
            matrícula_vehículo_a_buscar = input("Debe digitar una matrícula para buscar, ingrese nuevamente: ")

        ubicación_vehículo = parqueadero.determinar_ubicación_vehículo(matrícula_vehículo_a_buscar)
        if ubicación_vehículo is not None:
            print("-"*72)
            print()
            print(f"La ubicación del vehículo con matrícula '{matrícula_vehículo_a_buscar}' es: {ubicación_vehículo}")
            print()
            print("-"*72)
            print("\nPresiona enter para volver al menú principal")
            input("")
        else: 
            print("-"*72)
            print()
            print(f"El vehículo con matrícula {matrícula_vehículo_a_buscar} no se encuentra actualmente en el parqueadero.")
            print()
            print("-"*72)
            print("\nPresiona enter para volver al menú principal")
            input("")

    elif opción_seleccionada == "4":
        clear_screen()
        seguir_registrando_salidas_de_vehículo = True
        while seguir_registrando_salidas_de_vehículo:
            print("********************** REGISTRAR SALIDA VEHÍCULO ***********************")
            matrícula_vehículo_a_registrar_salida = input("\nIngrese la matrícula del vehículo que se le va a registrar la salida : ")
            while len(matrícula_vehículo_a_registrar_salida.strip()) == 0: 
                    matrícula_vehículo_a_registrar_salida = input("\nDebe digitar una matrícula, ingrese nuevamente: ")
                 
            try:
                parqueadero_hora_egreso = parqueadero.determinar_hora_egreso_vehículo(matrícula_vehículo_a_registrar_salida)
                horas_estadas_vehículo = parqueadero.determinar_horas_vehículo_parqueadero(matrícula_vehículo_a_registrar_salida)
                valor_a_pagar_vehículo = parqueadero.determinar_valor_a_pagar_vehículo(matrícula_vehículo_a_registrar_salida)

            except ValueError:
                print("-"*72)
                print(f"\nEL vehículo con matrícula {matrícula_vehículo_a_registrar_salida} no se encuentra en el parqueadero")
                print()
                print("-"*72)
                print("\nPresiona enter para volver al menú principal")
                input("")
                seguir_registrando_salidas_de_vehículo = False
                break
            
            print()
            print("-"*72)
            print()
            print(f"Se ha registrado la salida del vehículo con matrícula {matrícula_vehículo_a_registrar_salida} con éxito")
            print(f"\nHoras en el parqueadero: {horas_estadas_vehículo}")
            print(f"Valor a pagar: {valor_a_pagar_vehículo}")
            print()        
            print("-"*72)
            print("\nPresiona enter para volver al menú principal")
            input("")
            seguir_registrando_salidas_de_vehículo = False

    elif opción_seleccionada == "5":
        clear_screen()
        print("---------------------- REPORTE GENERAL PARQUEADERO ----------------------")
        print(f"\nTotal dinero ingresado: {parqueadero.determinar_dinero_ingresado()}")
        print(f"Cantidad vehículos que han ingresado: {parqueadero.determinar_cantidad_vehículos_ingresados()}")
        print(f"Cantidad de puestos totales vendidos: {parqueadero.determinar_cantidad_puestos_utilizados()}")
        print()
        print("-"*72)
        print("\nPresiona enter para volver al menú principal")
        input("")

    elif opción_seleccionada == "6":
        clear_screen()
        if parqueadero.determinar_zona_más_utilizada() is None:
            print("-------------------------- ZONA MÁS UTILIZADA --------------------------")
            print("\nNo hay registro de vehículos ingresados en el parqueadero para determinar esto.")
            print("-"*72)
            print("\nPresiona enter para volver al menú principal")
            input("")
        else:
            print("-------------------------- ZONA MÁS UTILIZADA --------------------------")
            print(f"\nLa zona más utilizada en el parqueadero (Zona por precios) es: {parqueadero.determinar_zona_más_utilizada()}")
            print()
            print("-"*72)
            print("\nPresiona enter para volver al menú principal")
            input("")

    elif opción_seleccionada == "7": 
        clear_screen()
        print("-------------------- TASA OCUPACIÓN DEL PARQUEADERO --------------------")
        print(f"\n La tasa de ocupación del parqueadero es de: {parqueadero.determinar_tasa_ocupación()}%")
        print()
        print("-"*72)
        print("\nPresiona enter para volver al menú principal")
        input("")
        

    elif opción_seleccionada == "8":
        clear_screen()
        print("-------------- TASA OCUPACIÓN POR GENERO EN EL PARQUEADERO --------------")
        print(f"\nPorcentaje de conductores hombres en el parqueadero: {parqueadero.determinar_tasa_ocupación_hombres()}%")
        print(f"Porcenta de conductores mujeres en el parqueadero: {parqueadero.determinar_tasa_ocupación_mujeres()}%")
        print()
        print("-"*72)
        print("\nPresiona enter para volver al menú principal")
        input("")

    elif opción_seleccionada == "9":
        clear_screen()
        print("-------------- TASA OCUPACIÓN POR MARCA Y AÑO FABRICACIÓN DE LOS VEHÍCULOS EN EL PARQUEADERO --------------")
        print(f"\nTasa de ocupación por marca: \n{parqueadero.determinar_porcentaje_de_vehículos_por_marca()}")
        print(f"\nTasa de ocupación por año de fabricación: \n{parqueadero.determinar_porcentaje_de_vehículos_por_año_fabricación()}")
        print()
        print("-"*107)
        print("\nPresiona enter para volver al menú principal")
        input("")

    elif opción_seleccionada == "10":
        clear_screen
        seguir_utilizando_programa = False
        print("*"*72)
        print("********************* GRACIAS POR USAR EL PROGRAMA *********************")
        print("*"*72)
        print()

    guardar_conductor_vehículo(parqueadero.registro_conductores)
    guardar_vehículo(parqueadero.registro_vehículos)