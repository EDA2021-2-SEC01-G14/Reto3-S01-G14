"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
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
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

from datetime import datetime
import time
import config as cf
import sys
import controller
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.ADT import orderedmap as om
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""
def printload(analyzer):

    listSi=analyzer['UFO_sightings']

    for si in range(1,6):
        print(si) 
        si=lt.getElement(listSi,si)

        print("datetime: "+si["datetime"]+' | '+"city: "+si["city"]+' | '+"state: "+si["state"]+' | '+"country: "+si["country"]+' | '+
        "shape: "+si["shape"]+' | '+"duration(seg): "+si["duration (seconds)"]+' | '+"duration(h/m): "+si["duration (hours/min)"]+' | '+
        "comments: "+si["comments"]+' | '+"date posted: "+si["date posted"]+' | '+"latitude: "+si["latitude"]+' | '+"longitude: "+si["longitude"])
        
    print('\n\n')
    size=lt.size(listSi)
    
    for si in range(size-4,size+1):
        print(si) 
        si=lt.getElement(listSi,si)   

        print("datetime: "+si["datetime"]+' | '+"city: "+si["city"]+' | '+"state: "+si["state"]+' | '+"country: "+si["country"]+' | '+
        "shape: "+si["shape"]+' | '+"duration(seg): "+si["duration (seconds)"]+' | '+"duration(h/m): "+si["duration (hours/min)"]+' | '+
        "comments: "+si["comments"]+' | '+"date posted: "+si["date posted"]+' | '+"latitude: "+si["latitude"]+' | '+"longitude: "+si["longitude"])
        



    pass

######### REQ1 #########
def printByCity(analyzer,list,city):

    print('There are',mp.size(analyzer['ByCity']), 'different cities with UFO sightings...')
        
    if list == 0:
        print('The city do not have sightings')
    
    else:

        size=lt.size(list)
        print('\nThere are',om.size(mp.get(analyzer['ByCity'],city)['value']),'sighting(s) at the: '+city+' city.')
    
        if size >= 6:
            print('The first 3 and last 3 UFO sightings in the city area\n')
            for i in range(1,4):
                si=lt.getElement(list,i)
                print("datetime: "+si["datetime"]+' | '+"city: "+si["city"]+' | '+"state: "+si["state"]+' | '+"country: "+si["country"]+' | '+
                "duration(seg): "+si["duration (seconds)"]+' | '+"shape: "+si["shape"])

            print('\n')
            for i in range(size-2,size+1):
                si=lt.getElement(list,i)
                print("datetime: "+si["datetime"]+' | '+"city: "+si["city"]+' | '+"state: "+si["state"]+' | '+"country: "+si["country"]+' | '+
                "duration(seg): "+si["duration (seconds)"]+' | '+"shape: "+si["shape"])
        else:
            i=1
            
            for i in range(1,size+1):
                si=lt.getElement(list,i)
                print("datetime: "+si["datetime"]+' | '+"city: "+si["city"]+' | '+"state: "+si["state"]+' | '+"country: "+si["country"]+' | '+
                "duration(seg): "+si["duration (seconds)"]+' | '+"shape: "+si["shape"])
                
                i+=1

######### REQ3 #########                
def printByHour(analyzer,list):

    print('There are',om.size(analyzer['ByHour']), 'UFO sightings with different times [HH:MM:SS]...')
    print('The latest sighting is: ')
    latest=(datetime.strftime(om.maxKey(analyzer['ByHour']),"%Y-%m-%d %H:%M:%S"))[11:]
    print(latest,'==',lt.size(om.get(analyzer['ByHour'],om.maxKey(analyzer['ByHour']))['value']))

    size=lt.size(list)
    print('There are',size,'UFO sightings between the range')
    
    if size >= 6:
            print('The first 3 and last 3 UFO sightings in the city area\n')
            for i in range(1,4):
                si=lt.getElement(list,i)
                print("datetime: "+si["datetime"]+' | '+"time: "+si["datetime"][11:]+' | '+"city: "+si["city"]+' | '+"state: "+si["state"]+' | '+"country: "+si["country"]+' | '+
                "duration(seg): "+si["duration (seconds)"]+' | '+"shape: "+si["shape"])

            print('\n')
            for i in range(size-2,size+1):
                si=lt.getElement(list,i)
                print("datetime: "+si["datetime"]+' | '+"time: "+si["datetime"][11:]+' | '+"city: "+si["city"]+' | '+"state: "+si["state"]+' | '+"country: "+si["country"]+' | '+
                "duration(seg): "+si["duration (seconds)"]+' | '+"shape: "+si["shape"])
    else:
        i=1
        for i in range(1,size+1):
            si=lt.getElement(list,i)
            print("datetime: "+si["datetime"]+' | '+"city: "+si["city"]+' | '+"state: "+si["state"]+' | '+"country: "+si["country"]+' | '+
           "duration(seg): "+si["duration (seconds)"]+' | '+"shape: "+si["shape"])
                
            i+=1

######### REQ5 #########
def printByZone(list):


    size=lt.size(list)
    print('There are',size,'UFO sightings in the current zone')

    if size >= 10:
            print('The first 5 and last 5 UFO sightings in the city area\n')
            for i in range(1,6):
                si=lt.getElement(list,i)
                print("datetime: "+si["datetime"]+' | '+"city: "+si["city"]+' | '+"state: "+si["state"]+' | '+"country: "+si["country"]+' | '+
                "duration(seg): "+si["duration (seconds)"]+' | '+"shape: "+si["shape"]+' | '+"latitude: "+si["latitude"]+' | '+"longitude: "+si["longitude"])

            print('\n')
            for i in range(size-4,size+1):
                si=lt.getElement(list,i)
                print("datetime: "+si["datetime"]+' | '+"city: "+si["city"]+' | '+"state: "+si["state"]+' | '+"country: "+si["country"]+' | '+
                "duration(seg): "+si["duration (seconds)"]+' | '+"shape: "+si["shape"]+' | '+"latitude: "+si["latitude"]+' | '+"longitude: "+si["longitude"])
    else:
        i=1
        for i in range(1,size+1):
            si=lt.getElement(list,i)
            print("datetime: "+si["datetime"]+' | '+"city: "+si["city"]+' | '+"state: "+si["state"]+' | '+"country: "+si["country"]+' | '+
           "duration(seg): "+si["duration (seconds)"]+' | '+"shape: "+si["shape"]+' | '+"latitude: "+si["latitude"]+' | '+"longitude: "+si["longitude"])
                
            i+=1


def printMenu():
    print("_________________________________________________________")
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2-  Contar los avistamientos en una ciudad")
    print("3-  Contar los avistamientos por duración")
    print("4-  Contar avistamientos por Hora/Minutos del día")
    print("5-  Contar los avistamientos en un rango de fechas")
    print("6-  Contar los avistamientos de una Zona Geográfica")
    print("7-  Visualizar los avistamientos de una zona geográfica.")
    print("8-  Salir")

analyzer = None
x=True
"""
Menu principal
"""
while x:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')


    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")

        start = time.process_time_ns()

        analyzer=controller.initiateAnalyzer()
        controller.loadData(analyzer)

        stop = time.process_time_ns()
        sgs = (stop-start)/1000000000
        print('Time',sgs) 

        printload(analyzer)
      
######### REQ1 #########
    elif int(inputs[0]) == 2:
        city=str(input('Ingrese una ciudad: '))
        list=controller.SiByCity(analyzer,city)
        printByCity(analyzer,list,city)
        pass

    elif int(inputs[0]) == 3:
        pass


######### REQ3 #########
    elif int(inputs[0]) == 4:
        Hmin=str(input('Límite inferior en formato (HH:MM:SS): '))
        Hmax=str(input('Límite superiror en formato (HH:MM:SS): '))
        list=controller.SiByHM(analyzer,Hmin,Hmax)
        printByHour(analyzer,list)
        pass


    elif int(inputs[0]) == 5:
        pass


######### REQ5 #########
    elif int(inputs[0]) == 6:
        Lomin=str(input('Límite minimo en Longitud : '))
        Lomax=str(input('Límite maximo en Longitud : '))
        Lamin=str(input('Límite minimo en Latitud : '))
        Lamax=str(input('Límite maximo en Latitud : '))

        list=controller.SiByZone(analyzer,Lomin,Lomax,Lamin,Lamax)
        printByZone(list)
        pass




    elif int(inputs[0]) == 7:
        x=False
        pass

    else:
        sys.exit(0)
sys.exit(0)
