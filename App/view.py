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

def printByCity(analyzer,list,city):
        
    if list == 0:
        print('The city do not have sightings')
    elif type(list) == type(lt.getElement(analyzer['UFO_sightings'],1)):
        print('\nThere is 1 sightings at the: '+city+' city.')
        si=list
        print("datetime: "+si["datetime"]+' | '+"city: "+si["city"]+' | '+"state: "+si["state"]+' | '+"country: "+si["country"]+' | '+
                "duration(seg): "+si["duration (seconds)"]+' | '+"shape: "+si["shape"])
    else:
        print('\nThere are',lt.size(list),'sightings at the: '+city+' city.')
        size=lt.size(list)
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
            
            for si in list['elements']:
                print("datetime: "+si["datetime"]+' | '+"city: "+si["city"]+' | '+"state: "+si["state"]+' | '+"country: "+si["country"]+' | '+
                "duration(seg): "+si["duration (seconds)"]+' | '+"shape: "+si["shape"])
                if i == 3:
                    print('\n')
                i+=1
                





def printMenu():
    print("______________________________________________")
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

        analyzer=controller.initiateAnalyzer()
        controller.loadData(analyzer)
        printload(analyzer)
      

        print(om.get(analyzer['ByCity'],'tampa'))

    elif int(inputs[0]) == 2:
        city=str(input('Ingrese una ciudad: '))
        list=controller.SiByCity(analyzer,city)
        printByCity(analyzer,list,city)
        pass

    elif int(inputs[0]) == 3:
        pass

    elif int(inputs[0]) == 4:
        pass

    elif int(inputs[0]) == 5:
        pass

    elif int(inputs[0]) == 6:
        pass

    elif int(inputs[0]) == 7:
        x=False
        pass

    else:
        sys.exit(0)
sys.exit(0)
