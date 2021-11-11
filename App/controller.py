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
 """

import config as cf
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo 

def initiateAnalyzer():

    return model.newAnalyzer()

# Funciones para la carga de datos

def loadData(analyzer):


    sightingsfile = cf.data_dir + 'UFOS-utf8-large.csv'
    input_file = csv.DictReader(open(sightingsfile, encoding="utf-8"),
                                delimiter=",")
    for sighting in input_file:
        model.addSighting(analyzer,sighting)
    return analyzer

# Funciones de Consulta

######### REQ1 #########

def SiByCity(analyzer,city):
    return model.SiByCity(analyzer,city)

######### REQ2 #########
def countbyDuration(analyzer, min, max):
    return model.countbyDuration(analyzer, min, max)

######### REQ3 #########

def SiByHM(analyzer,Hmin,Hmax):
    return model.SiByHM(analyzer,Hmin,Hmax)

######### REQ4 #########
def byDateReq4(analyzer,min,max):
    registros=model.byDateReq4(analyzer,min,max)
    return registros

######### REQ5 #########

def SiByZone(analyzer,Lomin,Lomax,Lamin,Lamax):
    return model.SiByZone(analyzer,Lomin,Lomax,Lamin,Lamax)

# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo
