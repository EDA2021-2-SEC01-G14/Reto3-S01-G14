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


from DISClib.ADT.indexminpq import size
import config as cf
import copy
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

    analyzer['ByCity']=mp.newMap(16000, maptype='PROBING',loadfactor=0.5,)

    return analyzer

# Funciones para agregar informacion al catalogo

def addSighting(analyzer,sighting):

    lt.addLast(analyzer['UFO_sightings'],sighting)
    addtomapREQ1(analyzer['ByCity'],sighting['city'],sighting)
    



# Funciones para creacion de datos
def addtomap(map,key,object):

    if mp.contains(map,key):
    
            entry=mp.get(map,key)
            list=entry['value']
            lt.addLast(list,object)
            mp.put(map,key,list)
            #print(mp.get(catalog['BeginDate'],artist['BeginDate']))
            
    else: 
        list=lt.newList()
        lt.addLast(list,object)
        mp.put(map,key,list)
#######
def addtoOrdmap(map,key,object):

    if om.contains(map,key):
    
            entry=om.get(map,key)
            list=entry['value']
            lt.addLast(list,object)
            om.put(map,key,list)
            #print(mp.get(catalog['BeginDate'],artist['BeginDate']))
            
    else: 
        list=lt.newList(datastructure='ARRAY_LIST')
        lt.addLast(list,object)
        om.put(map,key,list)
#######
def addtomapREQ1(map,key,object):

    if mp.contains(map,key):
    
            BRT=mp.get(map,key)['value']
            Date=datetime.strptime(object['datetime'],"%Y-%m-%d %H:%M:%S")
            om.put(BRT,Date,object)
            mp.put(map,key,BRT)
            #print(mp.get(catalog['BeginDate'],artist['BeginDate']))
            
    else: 
        BRT=om.newMap(omaptype='RBT')
        Date=datetime.strptime(object['datetime'],"%Y-%m-%d %H:%M:%S")
        om.put(BRT,Date,object)
        mp.put(map,key,BRT)


# Funciones de consulta
######### REQ1 #########

def SiByCity(analyzer,city):
    
    if mp.get(analyzer['ByCity'],city) == None:
        return 0
    else:
        SiCity=copy.deepcopy(mp.get(analyzer['ByCity'],city)['value'])
        ans=lt.newList()
        size=om.size(SiCity)

        if size > 6:
            si=0   
            while si < 6:
                if si < 3:
                    min=om.minKey(SiCity)
                    lt.addLast(ans,om.get(SiCity,min)['value'])
                    om.deleteMin(SiCity)
                else:
                    max=om.maxKey(SiCity)
                    lt.addLast(ans,om.get(SiCity,max)['value'])
                    om.deleteMax(SiCity)
                si+=1
        else:
            dates=om.keySet(SiCity)
            for si in range(1,size+1):
                key=lt.getElement(dates,si)
                lt.addLast(ans,om.get(SiCity,key)['value'])

        mg.sort(ans,cmpSightingByDate)

    return ans

def SiByCity2(analyzer,city):

    if om.get(analyzer['ByCity'],city) == None:
        return 0

    else:
        SiCity=om.get(analyzer['ByCity'],city)['value']
        mg.sort(SiCity,cmpSightingByDate)
    
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
