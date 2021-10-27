"""
 * Copyright 2020, Departamento de sistemas y Computación,
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
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from datetime import datetime
import time
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.ADT import orderedmap as om
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import mergesort as mg
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def newAnalyzer():
    
    
    analyzer = {'UFO_sightings': None,
                'ByCity': None,
                '2': None,
                '3': None,
                '4': None,
                '5': None,
                '6': None
                        }


    analyzer['UFO_sightings']=lt.newList(datastructure='ARRAY_LIST')

    analyzer['ByCity']=om.newMap(omaptype='RBT')

    return analyzer

# Funciones para agregar informacion al catalogo

def addSighting(analyzer,sighting):

    lt.addLast(analyzer['UFO_sightings'],sighting)
    addtoOrdmap(analyzer['ByCity'],sighting['city'],sighting)
    



# Funciones para creacion de datos
def addtomap(map,key,object):

    if mp.contains(map,key):

        if type(mp.get(map,key)['value']) == type(object):    
            l=lt.newList(datastructure='ARRAY_LIST')
            lt.addLast(l,mp.get(map,key)['value'])
            lt.addLast(l,object)
            mp.put(map,key,l)
            
        else:     
            entry=mp.get(map,key)
            list=entry['value']
            
            lt.addLast(list,object)
            #print(mp.get(catalog['BeginDate'],artist['BeginDate']))
            
    else: 
        mp.put(map,key,object)
#######
def addtoOrdmap(map,key,object):

    if om.contains(map,key):

        if type(om.get(map,key)['value']) == type(object):    
            l=lt.newList(datastructure='ARRAY_LIST')
            lt.addLast(l,om.get(map,key)['value'])
            lt.addLast(l,object)
            om.put(map,key,l)
            
        else:     
            entry=om.get(map,key)
            list=entry['value']
            
            lt.addLast(list,object)
            #print(mp.get(catalog['BeginDate'],artist['BeginDate']))
            
    else: 
        om.put(map,key,object)



# Funciones de consulta
######### REQ1 #########
def SiByCity(analyzer,city):
    
    if om.get(analyzer['ByCity'],city) == None:
        return 0

    elif type(om.get(analyzer['ByCity'],city)['value']) != type(lt.getElement(analyzer['UFO_sightings'],1)):

        SiCity=om.get(analyzer['ByCity'],city)['value']
        mg.sort(SiCity,cmpSightingByDate)
    else:
        SiCity=om.get(analyzer['ByCity'],city)['value']

    return SiCity


# Funciones utilizadas para comparar elementos dentro de una lista

#FUNCIONES DE COMPARACÍON

def compareDates(date1, date2):
    """
    Compara dos fechas
    """
    if (date1 == date2):
        return 0
    elif (date1 > date2):
        return 1
    else:
        return -1

# Funciones de ordenamiento

def cmpSightingByDate(Si1,Si2):

    Si1=datetime.strptime(Si1['datetime'],"%Y-%m-%d %H:%M:%S")
    Si2=datetime.strptime(Si2['datetime'],"%Y-%m-%d %H:%M:%S")
    
    if Si1< Si2:
        return True
    else:
        return False
