from datetime import date
from datetime import datetime
from clase_conductor import Conductor
from clase_vehículo import Vehículo
import math

class Parqueadero:
    def __init__(self, nombre : str,  cantidad_puestos_parqueadero : int):

        if len(nombre.strip()) == 0: 
            raise ValueError("El nombre no puede ser una cadena vacía")

        if cantidad_puestos_parqueadero not in (36, 64 , 100):
            raise ValueError("El largo del parqueadero debe estar en el rango estipulado")
        
        largo_parqueadero = int(math.sqrt(cantidad_puestos_parqueadero))
        
        self.nombre = nombre
        self.cantidad_puestos_parqueadero = cantidad_puestos_parqueadero
        self.filas = largo_parqueadero
        self.columnas_filas = largo_parqueadero
        self.letras_filas = []
        for i in range(largo_parqueadero):
            self.letras_filas.append(chr(i+65))
        self.parqueadero = [[None for _ in range(largo_parqueadero)] for _ in range(largo_parqueadero)]
        self.registro_conductores = []
        self.registro_vehículos = []
        self.precios = []

    def determinar_puestos_asignados_matriz(self): 
        for vehículo in self.registro_vehículos: 
            if vehículo.hora_egreso_vehículo is None:
                índice_letra_puesto = self.letras_filas.index(vehículo.puesto_asignado[0])
                índice_número_puesto = (int(vehículo.puesto_asignado[1])-1)
                self.parqueadero[índice_letra_puesto][índice_número_puesto] = vehículo

    #--------------------------------- HISTOyoRIA USUARIO #1 -------------------------------------------
        
    def determinar_precio_mínimo_puesto_parqueadero(self):
        precio_mínimo = len(self.parqueadero)*1000
        return precio_mínimo

    def determinar_precio_máximo_puesto_parqueadero(self):
        precio_máximo = self.determinar_precio_mínimo_puesto_parqueadero() * (len(self.parqueadero)/2)
        return precio_máximo
    
    def calcular_costo_puesto(self,letra:str, número_columna:int) -> float:

        if len(letra.strip()) == 0: 
            raise ValueError("La cadena con la letra del puesto no puede estar vacía")
        
        if letra not in self.letras_filas: 
            raise ValueError("La cadena con la letra del puesto debe estar entre el rango estipulado")
        
        if número_columna not in range((self.columnas_filas)): 
            raise ValueError("El número de la columna debe estar entre el rango aestipulado")
        
        fila = self.letras_filas.index(letra)
        columna = número_columna

        filas_distancia_al_borde_arriba = fila
        filas_distancia_al_borde_abajo = (len(self.parqueadero)-1)-fila
        if filas_distancia_al_borde_arriba > filas_distancia_al_borde_abajo:
            menor_distancia_fila = filas_distancia_al_borde_abajo
        else:
            menor_distancia_fila = filas_distancia_al_borde_arriba
        #Determina que tan cerca está de los bordes de manera vertical

        columna_distancia_al_borde_izquierda = columna
        columna_distancia_al_borde_derecha = (len(self.parqueadero[0])-1)-columna
        if columna_distancia_al_borde_izquierda > columna_distancia_al_borde_derecha:
            menor_distancia_columna = columna_distancia_al_borde_derecha
        else:
            menor_distancia_columna = columna_distancia_al_borde_izquierda
        #determina que tan cerca está de los bordes de manera horizontal

        if menor_distancia_fila > menor_distancia_columna:
            menor_distancia_a_un_borde = menor_distancia_columna
        else:
            menor_distancia_a_un_borde = menor_distancia_fila
        #Determina que tan cerca está a un borde en general, el valor 0 es que está pegado
        precio_puesto = self.determinar_precio_máximo_puesto_parqueadero() - self.determinar_precio_mínimo_puesto_parqueadero() * menor_distancia_a_un_borde
        return int(precio_puesto)
    
    #--------------------------------- HISTORIA USUARIO #2 -------------------------------------------
    def asignar_vehículo(self, marca_vehículo, matrícula_vehículo, año_fabricación_vehículo, documento_identidad_conductor_vehículo):
        
        vehículo = Vehículo(marca_vehículo, matrícula_vehículo, año_fabricación_vehículo, documento_identidad_conductor_vehículo)
        self.registro_vehículos.append(vehículo)    
                                                              
    def determinar_años_de_auto(self, año_fabricación : int) -> int:
        año_actual = int(date.today().year)
        if año_fabricación <= año_actual:
            edad_en_años = año_actual - año_fabricación
            return edad_en_años
        else: 
            raise ValueError("El año de fabricación del vehículo no puede ser mayor que el año actual")
           
    def determinar_precios_zonas_parqueadero(self): 
        precio_mínimo = self.determinar_precio_mínimo_puesto_parqueadero()
        for zona in range(int(len(self.parqueadero)/2)):
            precio_zona = precio_mínimo*(zona+1)
            self.precios.append(precio_zona)

    def determinar_hora_ingreso_vehículo(self, matrícula_vehículo : str):
        if len(matrícula_vehículo.strip()) == 0: 
            raise ValueError("la cadena con la matrícula del vehículo no puede estar vacía")
        
        for fila in range(0, self.filas):
            for columna in range(0, self.columnas_filas):
                if self.parqueadero[fila][columna] is not None:
                    if self.parqueadero[fila][columna].matrícula_vehículo == matrícula_vehículo:
                        self.parqueadero[fila][columna].hora_ingreso_vehículo = datetime.now()
                        return self.parqueadero[fila][columna].hora_ingreso_vehículo
                    

    def asignar_puesto(self, precio : int,nombre_conductor:str, fecha_nacimiento_conductor:date, sexo_conductor:str, marca_vehículo:str, 
                       matrícula_vehículo:str, año_fabricación_vehículo :int, documento_identidad_del_conductor : str):
        self.determinar_precios_zonas_parqueadero()
        
        if precio not in self.precios:
            raise ValueError("La preferencia de precio debe estar entre el rango aceptable")
        
        vehículo_en_parqueadero = False
        for fila in range(0, self.filas):
            for columna in range(0, self.columnas_filas):
                if self.parqueadero[fila][columna] is not None:
                    if self.parqueadero[fila][columna].matrícula_vehículo == matrícula_vehículo: 
                        vehículo_en_parqueadero = True

        if vehículo_en_parqueadero: 
            raise ValueError("El vehículo a asignar en el parqueadero noo puede ser uno que ya está asignado")
         
        conductor = Conductor(nombre_conductor, fecha_nacimiento_conductor, sexo_conductor, documento_identidad_del_conductor)
        asignar_puesto = False
        puestos_verificados_matriz = 0
     
        if conductor.comprobar_mayoria_edad():
            MÁXIMO_ANTIGÜEDAD = 10
            if self.determinar_años_de_auto(año_fabricación_vehículo) <= MÁXIMO_ANTIGÜEDAD:
                for fila in range(0, self.filas):
                    for columna in range(0, self.columnas_filas):
                        puestos_verificados_matriz += 1
                
                        if self.parqueadero[fila][columna] is None:
                            if self.calcular_costo_puesto(self.letras_filas[fila], columna) == precio:
                          
                                if conductor not in self.registro_conductores:
                                    self.registro_conductores.append(conductor)
                                self.asignar_vehículo(marca_vehículo, matrícula_vehículo, año_fabricación_vehículo, documento_identidad_del_conductor)
                                self.parqueadero[fila][columna] = self.registro_vehículos[((len(self.registro_vehículos))-1)]
                                self.parqueadero[fila][columna].puesto_asignado = (self.letras_filas[fila], columna+1)
                                self.determinar_hora_ingreso_vehículo(matrícula_vehículo)                                
                                return (self.letras_filas[fila], columna+1)
                        
                if puestos_verificados_matriz == self.cantidad_puestos_parqueadero:
                    raise ValueError("No se encontró puestos disponibles con ese precio")
            else:
                raise ValueError("El auto no debe tener más de 10 años de antigüedad")
        else:
            raise ValueError("El conductor debe ser mayor de edad")
        return asignar_puesto
    
    #--------------------------------- HISTORIA USUARIO #3 -------------------------------------------
        
    def mostrar_puestos_ocupados(self):
        ocupado = [["Disponible" for _ in range(self.filas)] for _ in range(self.columnas_filas)]

        for fila in range(0, self.filas):
            for columna in range(0, self.columnas_filas):
                if self.parqueadero[fila][columna] is not None:
                    ocupado[fila][columna] = "Ocupado"
        return ocupado
    
    def imprimir_matriz_cuadrada(self):
        matriz = self.mostrar_puestos_ocupados()

        for fila in matriz:
            print(" ".join(f"{elemento:10}" for elemento in fila))
    
    #--------------------------------- HISTORIA USUARIO #4 -------------------------------------------
            
                  
    def determinar_vehículo_en_casilla(self, letra_fila:str, columna:int):
        if len(letra_fila.strip()) == 0: 
            raise ValueError("La cadena la letra de la fila no puede estar vacía")
        
        if letra_fila not in self.letras_filas: 
            raise ValueError("La letra de la fila debe estar en el rango estipulado")
        
        if columna not in range(1, (self.columnas_filas +1)):
            raise ValueError("La columna ingresada debe estar entre el rango estipulado")
        
        vehículo_en_casilla = None
        índice_fila = self.letras_filas.index(letra_fila)
        índice_columna = columna - 1
        conductor_vehículo_en_casilla = None

        if self.parqueadero[índice_fila][índice_columna] is not None: 
            vehículo_en_casilla = self.parqueadero[índice_fila][índice_columna]

            for conductor in self.registro_conductores:
                if conductor.documento_identidad_conductor == vehículo_en_casilla.dueño_del_vehículo: 
                    conductor_vehículo_en_casilla = conductor

        return (vehículo_en_casilla, conductor_vehículo_en_casilla)
    
    def determinar_ubicación_vehículo(self, matrícula_vehículo : str): 
        if len(matrícula_vehículo.strip()) == 0: 
            raise ValueError("la cadena con la matrícula del vehículo no puede estar vacía")
        
        for fila in range(0, self.filas):
            for columna in range(0, self.columnas_filas):
                if self.parqueadero[fila][columna] is not None:
                    if self.parqueadero[fila][columna].matrícula_vehículo == matrícula_vehículo:
                        return (self.letras_filas[fila], columna+1)
        return None
                    
    #--------------------------------- HISTORIA USUARIO #5-6 -------------------------------------------

    def determinar_hora_egreso_vehículo(self, matrícula_vehículo : str,):
        if len(matrícula_vehículo.strip()) == 0: 
            raise ValueError("la cadena con la matrícula del vehículo no puede estar vacía")
        
        for fila in range(0, self.filas):
            for columna in range(0, self.columnas_filas):
                if self.parqueadero[fila][columna] is not None:
                    if self.parqueadero[fila][columna].matrícula_vehículo == matrícula_vehículo:
                        self.parqueadero[fila][columna].hora_egreso_vehículo = datetime.now()
                        return self.parqueadero[fila][columna].hora_egreso_vehículo
    
    def determinar_salida_de_vehículo_parqueadero(self, matrícula_vehículo : str): 
        if len(matrícula_vehículo.strip()) == 0: 
            raise ValueError("la cadena con la matrícula del vehículo no puede estar vacía")
        
        for fila in range(0, self.filas):
            for columna in range(0, self.columnas_filas):
                if self.parqueadero[fila][columna] is not None:
                    if self.parqueadero[fila][columna].matrícula_vehículo == matrícula_vehículo:
                        self.parqueadero[fila][columna] = None
                        break

    def determinar_horas_vehículo_parqueadero(self, matrícula_vehículo: str):
        if len(matrícula_vehículo.strip()) == 0:
            raise ValueError("La cadena con la matrícula del vehículo no puede estar vacía")
        
        hora_salida_vehículo = self.determinar_hora_egreso_vehículo(matrícula_vehículo)
        if hora_salida_vehículo is None:
            raise ValueError("La hora de egreso del vehículo no está registrada")
        
        for fila in range(self.filas):
            for columna in range(self.columnas_filas):
                espacio = self.parqueadero[fila][columna]
                if espacio and espacio.matrícula_vehículo == matrícula_vehículo:
                    hora_ingreso_vehículo = espacio.hora_ingreso_vehículo
                    if hora_ingreso_vehículo is None:
                        raise ValueError("La hora de ingreso del vehículo no está registrada")
                    diferencia_horas = ((hora_salida_vehículo - hora_ingreso_vehículo).total_seconds() // 3600) + 1
                    return int(diferencia_horas)
        
        raise ValueError("El vehículo con la matrícula proporcionada no se encontró en el parqueadero")


    def determinar_valor_a_pagar_vehículo(self, matrícula_vehículo : str):
        if len(matrícula_vehículo.strip()) == 0: 
            raise ValueError("la cadena con la matrícula del vehículo no puede estar vacía")
        
        calcular_costo_casilla = 0
        calcular_horas_estadas_vehículo = 0
        valor_a_pagar_vehículo = 0
        for fila in range(self.filas):
            for columna in range(self.columnas_filas):
                if self.parqueadero[fila][columna] is not None:
                    if self.parqueadero[fila][columna].matrícula_vehículo == matrícula_vehículo: 
                            
                        calcular_costo_casilla = self.calcular_costo_puesto(self.parqueadero[fila][columna].puesto_asignado[0], self.parqueadero[fila][columna].puesto_asignado[1])
                        calcular_horas_estadas_vehículo = self.determinar_horas_vehículo_parqueadero(matrícula_vehículo)
                        valor_a_pagar_vehículo = (calcular_costo_casilla * calcular_horas_estadas_vehículo)
                        self.parqueadero[fila][columna].valor_a_pagar = valor_a_pagar_vehículo
                        self.determinar_salida_de_vehículo_parqueadero(matrícula_vehículo)

                        return valor_a_pagar_vehículo

    #--------------------------------- HISTORIA USUARIO #7 -------------------------------------------

    def puestos_vendidos(self): 
        puestos_vendidos = []

        for vehículo in self.registro_vehículos:
            if vehículo.hora_egreso_vehículo != 0:
                puesto = vehículo.puesto_asignado
                valor_total_pago_puesto = vehículo.valor_a_pagar
                puestos_vendidos.append((puesto, valor_total_pago_puesto))

        return puestos_vendidos

    def determinar_dinero_ingresado(self): 
        dinero_total_ingresado = 0 
        registro_puestos_vendidos = self.puestos_vendidos()
        for casilla in range(0, len(registro_puestos_vendidos)): 
            dinero_total_ingresado += registro_puestos_vendidos[casilla][1]
        return dinero_total_ingresado
    
    def determinar_cantidad_vehículos_ingresados(self): 
        matrículas_registradas = []
        for vehículo in self.registro_vehículos:
            if vehículo.matrícula_vehículo not in matrículas_registradas:
                matrículas_registradas.append(vehículo.matrícula_vehículo)
    
        cantidad_vehículos_ingresados = int(len(matrículas_registradas))
        return cantidad_vehículos_ingresados
    
    def determinar_cantidad_puestos_utilizados(self): 
        total_puestos_utilizados = 0 
        registro_puestos_vendidos = self.puestos_vendidos()
        total_puestos_utilizados = int(len(registro_puestos_vendidos))
        return total_puestos_utilizados 
    
        #--------------------------------- HISTORIA USUARIO #8 -------------------------------------------
    def determinar_cantidad_zonas_parqueaderos(self): 
        zonas_parqueaderos_precios = {}
        precio_máximo = int(self.determinar_precio_máximo_puesto_parqueadero())
        precio_mínimo = int(self.determinar_precio_mínimo_puesto_parqueadero())
        cantidad_zonas_parqueadero = int(precio_máximo/precio_mínimo)

        for zona in range(1, cantidad_zonas_parqueadero+1):
            zonas_parqueaderos_precios.setdefault(f"Zona {zona}", zona*precio_mínimo)
        return zonas_parqueaderos_precios
    
    def determinar_zona_más_utilizada(self): 
        precio_máximo = self.determinar_precio_máximo_puesto_parqueadero()
        precio_mínimo = self.determinar_precio_mínimo_puesto_parqueadero()
        cantidad_zonas_parqueadero = int(precio_máximo/precio_mínimo)

        zonas = [0 for _ in range(cantidad_zonas_parqueadero)]
        if len(self.registro_vehículos) == 0:
            return None
        else:
            for vehículos in self.registro_vehículos:
                zonas[int(((self.calcular_costo_puesto(vehículos.puesto_asignado[0], vehículos.puesto_asignado[1]))/precio_mínimo)-1)]+=1
            zona_mayor = 0

            for zona in range(int(cantidad_zonas_parqueadero-1)):
                if zonas[zona_mayor] < zonas[zona+1]:
                    zona_mayor = zona+1
        return (zona_mayor+1)*precio_mínimo

    def determinar_tasa_ocupación(self): 
        cantidad_puestos_ocupados = 0
        tasa_ocupación = 0
        cantidad_puestos_parqueadero = self.cantidad_puestos_parqueadero

        for fila in range(0, self.filas):
            for columna in range(0, self.columnas_filas):
                if self.parqueadero[fila][columna] is not None:
                    cantidad_puestos_ocupados += 1
        
        tasa_ocupación = (cantidad_puestos_ocupados / cantidad_puestos_parqueadero) * 100

        return round(tasa_ocupación, 2)
    
        #--------------------------------- HISTORIA USUARIO #9 -------------------------------------------

    def determinar_tasa_ocupación_hombres(self):
        total_conductores = 0
        conductores_masculinos = 0
        
        for fila in range(self.filas):
            for columna in range(self.columnas_filas):
                if self.parqueadero[fila][columna] is not None:
                    documento = self.parqueadero[fila][columna].dueño_del_vehículo
                
                    for conductor in self.registro_conductores:
                        if conductor.documento_identidad_conductor == documento:
                            total_conductores += 1
                            if conductor.sexo_conductor == "M":
                                conductores_masculinos += 1
                            break  
        if total_conductores == 0:
            return 0
        
        tasa_ocupacion_hombres_parqueadero = (conductores_masculinos / total_conductores) * 100

        return round(tasa_ocupacion_hombres_parqueadero, 2)

    def determinar_tasa_ocupación_mujeres(self): 
        lista_sexo_biológico_conductores_usando_parqueadero = []
        contador_sexo_femenino_en_conductores = 0
        tasa_ocupación_mujeres_parqueadero = 0
        for fila in range(0, self.filas):
            for columna in range(0, self.columnas_filas):
                if self.parqueadero[fila][columna] is not None:
                    for conductor in self.registro_conductores: 
                        if self.parqueadero[fila][columna].dueño_del_vehículo == conductor.documento_identidad_conductor:
                            lista_sexo_biológico_conductores_usando_parqueadero.append(conductor.sexo_conductor) 
        if len(lista_sexo_biológico_conductores_usando_parqueadero) == 0:
            return 0
        for iteración_casilla in range(0, len(lista_sexo_biológico_conductores_usando_parqueadero)):
           if lista_sexo_biológico_conductores_usando_parqueadero[iteración_casilla] == "F":
               contador_sexo_femenino_en_conductores += 1

        tasa_ocupación_mujeres_parqueadero = (contador_sexo_femenino_en_conductores/len(lista_sexo_biológico_conductores_usando_parqueadero))*100

        return round(tasa_ocupación_mujeres_parqueadero, 2)

    
    #--------------------------------- HISTORIA USUARIO #10 -------------------------------------------
    
    def determinar_porcentaje_de_vehículos_por_marca(self):
        total_vehículos_parqueados = 0
        cantidad_por_marcas = {}
        for vehículo in self.registro_vehículos:
            if vehículo.hora_egreso_vehículo is None:
                marca = vehículo.marca_vehículo
                if marca not in cantidad_por_marcas:
                    cantidad_por_marcas[marca] = 0
                cantidad_por_marcas[marca] += 1
                total_vehículos_parqueados += 1
        

        porcentajes_por_marca = {}
        for marca, cantidad in cantidad_por_marcas.items():
            porcentajes_por_marca[marca] = (cantidad / total_vehículos_parqueados) * 100

        return porcentajes_por_marca
    
    def obtener_porcentaje_por_marca(self, marca_vehículo : str):
        if len(marca_vehículo.strip())  == 0: 
            raise ValueError("La cadena con la marca del vehículo no puede estar vacía") 
        
        porcentajes = self.determinar_porcentaje_de_vehículos_por_marca()
        return porcentajes.get(marca_vehículo, 0)
    
    def determinar_porcentaje_de_vehículos_por_año_fabricación(self):
        total_vehículos_parqueados = 0
        cantidad_por_años = {}
        for vehículo in self.registro_vehículos:
            if vehículo.hora_egreso_vehículo is None:
                año_fabricación = vehículo.año_fabricación_vehículo
                if año_fabricación not in cantidad_por_años:
                    cantidad_por_años[año_fabricación] = 0
                cantidad_por_años[año_fabricación] += 1
                total_vehículos_parqueados += 1
        

        porcentajes_por_años = {}
        for año_fabricación, cantidad in cantidad_por_años.items():
            porcentajes_por_años[año_fabricación] = (cantidad / total_vehículos_parqueados) * 100

        return porcentajes_por_años