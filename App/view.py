"""
 * Copyright 2020, Departamento de sistemas y Computación
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """

import sys
import config
from DISClib.ADT import list as lt
from App import controller
assert config

"""
La vista se encarga de la interacción con el usuario.
Presenta el menu de opciones  y  por cada seleccion
hace la solicitud al controlador para ejecutar la
operación seleccionada.
"""

# ___________________________________________________
#  Ruta a los archivos
# ___________________________________________________


accidentsfile = "us_accidents_small.csv"
cont = None

# ___________________________________________________
#  funciones extra
# ___________________________________________________

def printMoreAccidentsOnDate(accidents):
    total=0
    dates=[]
    moreReportedDate:""
    for accidentes in range(1, lt.size(accidents)):
        keyDate = lt.getElement(accidents,accidentes)
        tota=lt.size(keyDate["AccidentList"])
        dates.append(tota)
        total+=tota
    moreCommonDate=max(dates)
    for accidentes in range(1, lt.size(accidents)):
        keyDate=lt.getElement(accidents,accidentes)
        moreCommon= lt.size(keyDate["AccidentList"])
        if moreCommonDate==moreCommon:
            moreReportedDate==keyDate["Date"]
    print("Total de accidentes antes de la fecha: " + total + "y la fecha con mas accidentes fue : " + moreReportedDate )        

def printAccidentsByHour(analyzer, initialHour, finalHour):
    accidents=controller.getAccidentsByHour(analyzer, initialHour, finalHour)
    s1= accidents[1]
    s2= accidents[2]
    s3= accidents[3]
    s4= accidents[4]
    suma=accidents[0]
    print("Accidentes en el rango de horas: " + suma )
    print("Accidentes de severidad 1: "+ s1)
    print("Accidentes de severidad 1: "+ s2)
    print("Accidentes de severidad 1: "+ s3)
    print("Accidentes de severidad 1: "+ s4)
    print("porcentaje de severidad 1 comparado con el total de casos; "+ round((s1/suma)*100))
    print("porcentaje de severidad 2 comparado con el total de casos; "+ round((s2/suma)*100))
    print("porcentaje de severidad 3 comparado con el total de casos; "+ round((s3/suma)*100))
    print("porcentaje de severidad 4 comparado con el total de casos; "+ round((s4/suma)*100))


# ___________________________________________________
#  Menu principal
# ___________________________________________________


def printMenu():
    print("\n")
    print("*******************************************")
    print("Bienvenido")
    print("1- Inicializar Analizador")
    print("2- Cargar información de accidentes")
    print("3- Requerimiento 3: Conocer accidentes en una fecha")
    print("4- Requerimento 2: Conocer los accidentes anteriores a una fecha")
    print("5- Requqerimiento 5(grupal): Conocer los accidentes por rangos de hora")
    print("0- Salir")
    print("*******************************************")


"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n>')

    if int(inputs[0]) == 1:
        print("\nInicializando....")
        # cont es el controlador que se usará de acá en adelante
        cont = controller.init()

    elif int(inputs[0]) == 2:
        print("\nCargando información de accidentes ....")
        controller.loadData(cont, accidentsfile)
        print("Accidentes cargados: " + str(controller.accidentsSize(cont)))
        print("Altura del árbol: " + str(controller.indexHeight(cont)))
        print("Elementos en el árbol: " + str(controller.indexSize(cont)))
        print("Menor llave: " + str(controller.minKey(cont)))
        print("Mayor llave: " + str(controller.maxKey(cont)))

    elif int(inputs[0]) == 3:
        print("\nBuscando accidentes en un rango de fechas: ")
        initialDate = input("Fecha (YYYY-MM-DD): ")
        severity = input("Severidad: ")
        numAccidents = controller.getAccidentsByRangeSeverity(cont, initialDate, severity)

        print("\nTotal de accidentes con severidad: "+ severity + " en esa fecha: " + str(numAccidents))


    elif int(inputs[0]) == 4:
        print("\nRequerimiento No 2 del reto 3: ")
        fecha = input("Introduzca fecha en formato YYYY-MM-DD: ")
        accidents= controller.getAccidentsBeforeDate(cont, fecha)
        if accidents != None:
           printMoreAccidentsOnDate(accidents)
        if accidents == None:
            print("No se encontraron accidentes antes de la fecha dada")
    
    elif int(inputs[0])== 5:
        print("\nRequerimiento No 5 del reto 3: ")
        initialHour: input("introduzca la hora inicial: ")
        finalHour: input("introduzc la hora final: ")
        printAccidentsByHour(cont,initialHour,finalHour)

    elif int(inputs[0]) == 6:
        initialDate = input("Fecha inicial (YYYY-MM-DD): ")
        finalDate = input("Fecha final (YYYY-MM-DD): ")
        print("")

    else:
        sys.exit(0)
sys.exit(0)
