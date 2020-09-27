# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 11:16:44 2020

@author: Martha Ines Juarez Cabrera
"""
#GENERAR DOS LISTAS:EXPORTACIONES E IMPORTACIONES
import csv

lista_exportaciones=[]
lista_importaciones=[]


with open("synergy_logistics_database.csv","r") as archivo_csv:
    lector=csv.reader(archivo_csv)
    
 
    for linea in lector:
       if linea[1]=="direction":
           continue
       if linea[1]=="Exports":
           lista_exportaciones.append(linea)
       else:
           lista_importaciones.append(linea)
    
#################################################################    
#VENTAS TOTALES DE EXPORTACIONES

ventas_exp=0
for venta in lista_exportaciones:
    ventas_exp+=int(venta[9]) 
##################################################################

#VENTAS TOTALES DE IMPORTACIONES
ventas_imp=0
for venta in lista_importaciones:
    ventas_imp+=int(venta[9])
#################################################################
#GENERAR FUNCION DE RUTAS 

def rutas(lista_datos):
    contador=0
    suma=0
    total_ventas=0
    porcentaje=0
    rutas_contadas=[]
    conteo_rutas=[]

    if lista_datos==lista_exportaciones:
        total_ventas=ventas_exp
         
    if lista_datos==lista_importaciones:
        total_ventas=ventas_imp
        
    for ruta in lista_datos:
        ruta_actual=[ruta[2],ruta[3]]
       # total_ventas+=int(ruta[9])
        
        if ruta_actual not in rutas_contadas:
            for elemento in lista_datos:
                if ruta_actual==[elemento[2],elemento[3]]:
                    contador+=1
                    suma+=int(elemento[9])
            porcentaje=int(100*suma/total_ventas)
            rutas_contadas.append(ruta_actual)
            conteo_rutas.append([ruta[2],ruta[3],contador,suma,porcentaje])
            contador=0
            suma=0
    
    conteo_rutas.sort(reverse=True, key= lambda x:x[3] )
    
    for ruta in conteo_rutas[0:10]:
        print(ruta)
  #conteo_rutas=[origin,destination,#rutas realizadas, total de ventas, porcentaje de ventas]

#################################################################
#GENERAR FUNCION DE MEDIOS DE TRANSPORTE

def transport(lista_datos):
    contador=0
    suma=0
    rutas_contadas=[]
    conteo_transport=[]
    
    for ruta in lista_datos:
        ruta_actual=ruta[7]
        
        if ruta_actual not in rutas_contadas:
            for elemento in lista_datos:
                if ruta_actual==elemento[7]:
                    contador+=1
                    suma+=int(elemento[9])
            rutas_contadas.append(ruta_actual)
            conteo_transport.append([ruta[7],contador,suma])
            contador=0
    conteo_transport.sort(reverse=True, key= lambda x:x[2] )
    
    for ruta in conteo_transport:
        print(ruta)
 #conteo_transport=[transport,#veces que se utilizo el transport, total de ventas por transporte]      

#################################################################        

#GENERAR FUNCION QUE ME DIGA LOS PAISES QUE GENERAN MAS INGRESOS

def ingresos(lista_datos):

    suma=0
    porcentaje=0
    cuenta=0
    rutas_contadas=[]
    conteo_ingresos=[]
    
    if lista_datos==lista_exportaciones:
        total_ventas=ventas_exp
         
    if lista_datos==lista_importaciones:
        total_ventas=ventas_imp
    
    for ruta in lista_datos:
        ruta_actual=ruta[2]
        
        if ruta_actual not in rutas_contadas:
            for elemento in lista_datos:
                if ruta_actual==elemento[2]:
                    #contador+=1
                    suma+=int(elemento[9])
            porcentaje=int(100*suma/total_ventas)
            rutas_contadas.append(ruta_actual)
            conteo_ingresos.append([ruta[2],suma,porcentaje])
            suma=0
    conteo_ingresos.sort(reverse=True, key= lambda x:x[1] )
    
    for ruta in conteo_ingresos:
        if cuenta<80:
          print(ruta)
          cuenta+=int(ruta[2])


#conteo_ingresos=[pais origen, total de ingresos, porcentaje de ingresos]

#################################################################

#rutas(lista_importaciones)    
#transport(lista_importaciones)
contador=0

print("Bienvenido")

while contador==0:
    
    opcion=int(input("Elige una de las siguientes opciones para analizar: \n1-Exportaciones \n2-Importaciones \n -->"))

    if opcion==1:
        print("\nEstos son los datos de las exportaciones:\n")
        print("\n10 rutas más demandadas de acuerdo al flujo:\n")
        rutas(lista_exportaciones)
        print("\nAnálisis de los medios de transporte:\n")
        transport(lista_exportaciones)
        print("\nPaíses que generan el 80% de las exportaciones\n")
        ingresos(lista_exportaciones)
        contador=1
        
    elif opcion==2:
        print("\nEstos son los datos de las importaciones:\n")
        print("\n10 rutas más demandadas de acuerdo al flujo:\n")
        rutas(lista_importaciones)
        print("\nAnálisis de los medios de transporte:\n")
        transport(lista_importaciones)
        print("\nPaíses que generan el 80% de las importaciones\n")
        ingresos(lista_importaciones)
        contador=1
       
    else:
        print("\nIntenta de nuevo\n")
        












