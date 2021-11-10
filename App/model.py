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
from datetime import datetime as dt
import time
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.ADT import orderedmap as om
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import mergesort as mg
import datetime 

assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def newAnalyzer():
    
    
    analyzer = {'UFO_sightings': None,
                'ByCity': None,
                'ByHour': None,
                'ByZone': None,
                "Duration": None,
                '4': None,
                '5': None,
                '6': None
                        }


    analyzer['UFO_sightings']=lt.newList(datastructure='ARRAY_LIST')

    analyzer["Datos"] = lt.newList('ARRAY_LIST')

    analyzer['ByCity']=mp.newMap(16000, maptype='PROBING',loadfactor=0.5,)

    analyzer['ByHour']=om.newMap(omaptype='RBT')

    analyzer['ByZone']=om.newMap(omaptype='RBT')

    analyzer["Duration"]=om.newMap(omaptype="RBT",
                                comparefunction=compareDuration)
    
    analyzer['byCity'] = mp.newMap(50000,maptype="CHAINING",loadfactor=5)

    analyzer['byDuration'] = om.newMap(omaptype='RBT',
                                      comparefunction=compareDuration)

    analyzer['byDate'] = om.newMap(omaptype='RBT',
                                      comparefunction=compareDates) 
    


    return analyzer

# Funciones para agregar informacion al catalogo

def addSighting(analyzer,sighting):

    lt.addLast(analyzer['UFO_sightings'],sighting)
    #REQ1
    addtomapREQ1(analyzer['ByCity'],sighting['city'],sighting)
    #REQ2
    addtomapREQ2(analyzer, sighting)
    #REQ3
    Date=datetime.datetime.strptime(sighting['datetime'][11:],"%H:%M:%S")
    addtomapREQ3(analyzer['ByHour'],Date,sighting)
    #REQ5
    lon=round(float(sighting['longitude']),2)
    addtomapREQ5(analyzer['ByZone'],lon,sighting)



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
            Date=datetime.datetime.strptime(object['datetime'],"%Y-%m-%d %H:%M:%S")
            om.put(BRT,Date,object)
            mp.put(map,key,BRT)
            #print(mp.get(catalog['BeginDate'],artist['BeginDate']))
            
    else: 
        BRT=om.newMap(omaptype='RBT')
        Date=datetime.datetime.strptime(object['datetime'],"%Y-%m-%d %H:%M:%S")
        om.put(BRT,Date,object)
        mp.put(map,key,BRT)
#######
def addtomapREQ2(analyzer, object):

    datos ={}
    dt=object["datetime"]
    if dt=="":
        dt="0001-01-01 00:00:01"

    datos["Date&Hour"]= datetime.datetime.strptime(dt,'%Y-%m-%d %H:%M:%S')
    datos["city"]= object["city"]
    datos["state"]= object["state"]
    datos["country"]= object["country"]
    datos["stct"]= (datos["city"]) +"-"+ datos["country"]
    datos["shape"]= object["shape"]
    seconds= object["duration (seconds)"]

    if  seconds=="":
         seconds=0
    datos["durationseconds"]= float(seconds)
    datos["duration"]= object["duration (hours/min)"]
    datos["date"]= datetime.datetime.strptime(object["date posted"],'%Y-%m-%d %H:%M:%S')  

    lt.addLast(analyzer["Datos"], datos)
    byCity(analyzer['byCity'],datos["city"],datos["Date&Hour"], datos)
    byDuration(analyzer["byDuration"], datos)
    byDate(analyzer["byDate"],datos)

    return analyzer

#######
def addtomapREQ3(map,key,object):

    if om.contains(map,key):
    
            BRT=om.get(map,key)['value']
            Date=datetime.datetime.strptime(object['datetime'],"%Y-%m-%d %H:%M:%S")
            om.put(BRT,Date,object)
            om.put(map,key,BRT)
            #print(mp.get(catalog['BeginDate'],artist['BeginDate']))
            
    else: 
        BRT=om.newMap(omaptype='RBT')
        Date=datetime.datetime.strptime(object['datetime'],"%Y-%m-%d %H:%M:%S")
        om.put(BRT,Date,object)
        om.put(map,key,BRT)
#######
def addtomapREQ5(map,key,object):

    if om.contains(map,key):
    
            BRT=om.get(map,key)['value']
            lat=round(float(object['latitude']),2)
            #om.put(BRT,lat,object)
            addtoOrdmap(BRT,lat,object)
            om.put(map,key,BRT)
            #print(mp.get(catalog['BeginDate'],artist['BeginDate']))
            
    else: 
        BRT=om.newMap(omaptype='RBT')
        lat=round(float(object['latitude']),2)
        #om.put(BRT,lat,object)
        addtoOrdmap(BRT,lat,object)
        om.put(map,key,BRT)



def byCity(map,city,date, object):

    if mp.contains(map,city)==False:
        mapDate= om.newMap(omaptype='RBT',
                            comparefunction=compareDates)

        a=lt.newList("ARRAY_LIST")
        lt.addLast(a,object)

        om.put(mapDate,date,a)
        mp.put(map,city,mapDate)

    else:

        mapDate2= mp.get(map,city)["value"]
        addMap(mapDate2,date,object)
        mp.put(map,city,mapDate2)

    return map

def byDuration(map, object):

    duration = object["durationseconds"]
    x= object["stct"]

    if om.contains(map,duration)==False:
        mapCity= om.newMap(omaptype='RBT',comparefunction=compareCity)
        help=lt.newList("ARRAY_LIST")
        lt.addLast(help,object)
        om.put(mapCity,x,help)
        om.put(map,duration,mapCity)

    else:
        mapaExistenteCiudad= om.get(map,duration)["value"]
        addMap(mapaExistenteCiudad,x,object)
        om.put(map,duration,mapaExistenteCiudad)

    return map

def byDate(map, object):

    DateHour=object["Date&Hour"]
    Date=datetime.date(DateHour.year,DateHour.month,DateHour.day)
    time=(DateHour.hour,DateHour.minute)

    if om.contains(map,Date)==False:
        mapTime= om.newMap(omaptype='RBT',comparefunction=compareTime)
        o=lt.newList("ARRAY_LIST")
        lt.addLast(o,object)
        om.put(mapTime,time,o)
        om.put(map,Date,mapTime)
    else:
        mapTime2= om.get(map,Date)["value"]
        addMap(mapTime2,time,object)
        om.put(map,Date,mapTime2)

    return map



def addMap(map, key, object):

    if om.contains(map,key)==False:
        b=lt.newList("ARRAY_LIST")
        lt.addLast(b,object)
        om.put(map,key,b)

    else:
        result=om.get(map,key)
        c=me.getValue(result)
        lt.addLast(c,object)
        om.put(map,key,c)
    

# Funciones de consulta

######### REQ1 #########

def SiByCity(analyzer,city):

    start = time.process_time_ns()
    
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

    stop = time.process_time_ns()

    sgs = (stop-start)/1000000000
    print('Time',sgs) 

    return ans

def SiByCity2(analyzer,city):

    if om.get(analyzer['ByCity'],city) == None:
        return 0

    else:
        SiCity=om.get(analyzer['ByCity'],city)['value']
        mg.sort(SiCity,cmpSightingByDate)
    
    return SiCity


######### REQ2 #########

def countbyDuration(analyzer, min, max):

    resultados= lt.newList("ARRAY_LIST")
   
    mapReq2 = om.values(analyzer["byDuration"],min,max)
    
    for z in lt.iterator(mapReq2):
        a= om.valueSet(z)
        for i in lt.iterator(a):
            for i in lt.iterator(i):
                lt.addLast(resultados,i)
    
    return resultados

######### REQ3 #########

def SiByHM(analyzer,Hmin,Hmax):

    start = time.process_time_ns()

    Hmin=datetime.datetime.strptime(Hmin,"%H:%M:%S")
    Hmax=datetime.datetime.strptime(Hmax,"%H:%M:%S")

    DatesIN=om.keys(analyzer['ByHour'],Hmin,Hmax)

    
    size=lt.size(DatesIN)  
    Si=lt.newList()

    for pos in range(1,size+1) :
        SisbyDate=om.get(analyzer['ByHour'],lt.getElement(DatesIN,pos))['value']
        Size=lt.size(SisbyDate)
        #Keys=om.keySet(SisbyDate)
        for i in range(1,Size+1):
            #key=lt.getElement(Keys,i)
            lt.addLast(Si,lt.getElement(SisbyDate,i))

    stop = time.process_time_ns()

    sgs = (stop-start)/1000000000
    print('Time',sgs) 

    return Si

def SiByHM2(analyzer,Hmin,Hmax):

    Hmin=datetime.datetime.strptime(Hmin,"%H:%M:%S")
    Hmax=datetime.datetime.strptime(Hmax,"%H:%M:%S")

    DatesIN=om.keys(analyzer['ByHour'],Hmin,Hmax)

    
    size=lt.size(DatesIN)  
    Si=lt.newList()

    for pos in range(1,size+1) :
        SisbyDate=om.get(analyzer['ByHour'],lt.getElement(DatesIN,pos))['value']
        Size=om.size(SisbyDate)
        Keys=om.keySet(SisbyDate)
        for i in range(1,Size+1):
            key=lt.getElement(Keys,i)
            lt.addLast(Si,om.get(SisbyDate,key)['value'])

    return Si

#req4
def byDateReq4(analyzer,min,max):

    DateMin= datetime.datetime.strptime(min,'%Y-%m-%d')
    MinDate=datetime.date(DateMin.year,DateMin.month,DateMin.day)

    DateMax= datetime.datetime.strptime(max,'%Y-%m-%d')
    MaxDate=datetime.date(DateMax.year,DateMax.month,DateMax.day)

    DateAnalyzer=analyzer["byDate"]
    result= lt.newList("ARRAY_LIST")
    op = om.values(DateAnalyzer,MinDate,MaxDate)

    if lt.isEmpty(op)==False:
        for cd in lt.iterator(op):
            datos= om.valueSet(cd)
            for byDatos in lt.iterator(datos):
                for registro in lt.iterator(byDatos):
                    lt.addLast(result,registro)
    return result

######### REQ 5 #########

def SiByZone(analyzer,Lomin,Lomax,Lamin,Lamax):

    start = time.process_time_ns()

    Lomin=float(Lomin)
    Lomax=float(Lomax)
    Lamin=float(Lamin)
    Lamax=float(Lamax)


    DatesInlo=om.keys(analyzer['ByZone'],Lomin,Lomax)

    size=lt.size(DatesInlo)  
    Si=lt.newList()
    
    for pos in range(1,size+1) :
        Sisbylo=om.get(analyzer['ByZone'],lt.getElement(DatesInlo,pos))['value']
        Keysla=om.keys(Sisbylo,Lamin,Lamax)
        Size=lt.size(Keysla)

        for i in range(1,Size+1):
            key=lt.getElement(Keysla,i)
            #lt.addLast(Si,om.get(Sisbylo,key)['value'])
            list=om.get(Sisbylo,key)['value']
            listsize=lt.size(list)
            if listsize == 1:
                lt.addLast(Si,lt.getElement(list,1))
            else:
                for i in range(1,listsize+1):
                    lt.addLast(Si,lt.getElement(list,i))

    mg.sort(Si,cmpSightingByLatitude)

    stop = time.process_time_ns()

    sgs = (stop-start)/1000000000
    print('Time',sgs) 

    return Si


# Funciones utilizadas para comparar elementos dentro de una lista

#FUNCIONES DE COMPARACÍON

def compareDates(date1, date2):
   
    if (date1 == date2):
        return 0
    elif (date1 > date2):
        return 1
    else:
        return -1

# Funciones de ordenamiento

def cmpSightingByDate(Si1,Si2):

    Si1=datetime.datetime.strptime(Si1['datetime'],"%Y-%m-%d %H:%M:%S")
    Si2=datetime.datetime.strptime(Si2['datetime'],"%Y-%m-%d %H:%M:%S")
    
    if Si1< Si2:
        return True
    else:
        return False

def compareDuration(duracion1,duracion2):
    if (duracion1 == duracion2):
        return 0
    elif (duracion1 > duracion2):
        return 1
    else:
        return -1


def compareTime(d1,d2):
 
    if (d1 == d2):
        return 0
    elif (d1 > d2):
        return 1
    else:
        return -1

def compareCity(City1,City2):

    if (City1 == City2):
        return 0
    elif (City1 > City2):
        return 1
    else:
        return -1


##### REQ5 #####
def cmpSightingByLatitude(Si1,Si2):
    
    if Si1['latitude']< Si2['latitude']:
        return True
    else:
        return False