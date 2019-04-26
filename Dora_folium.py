# -*- coding: utf-8 -*-
"""
Created on Sun Dec 09 14:10:08 2018

@author: gluis
"""

#Importamos la libreria de folium
import folium
#Aqui creanos y seleccionamos la vista del mapa con coordenadas sercas del area recrestiva 
mapa = folium.Map(location=[ 12.1,-100.9],zoom_start=50) 
Vertice1 = folium.Marker(location=(12.1, -100.9),
                         icon=folium.Icon(color="blue")) 
Vertice2 = folium.Marker(location=(12.4, -102.2),
                         icon=folium.Icon(color="blue")) 
Vertice3 = folium.Marker(location=(12.8, -103.5),
                         icon=folium.Icon(color="blue"))
Vertice4 = folium.Marker(location=(13.2, -104.9),
                         icon=folium.Icon(color="blue"))
Vertice5 = folium.Marker(location=(13.6, -106.3),
                         icon=folium.Icon(color="blue"))
Vertice6 = folium.Marker(location=(14.0, -107.1),
                         icon=folium.Icon(color="blue"))
Vertice7 = folium.Marker(location=(14.4, -120.5),
                         icon=folium.Icon(color="blue"))
Vertice8 = folium.Marker(location=(14.4, -119.4),
                         icon=folium.Icon(color="blue"))
Vertice9 = folium.Marker(location=(14.4, -118.4),
                         icon=folium.Icon(color="blue"))
Vertice10 = folium.Marker(location=(14.5, -122.6),
                         icon=folium.Icon(color="blue"))
Vertice11 = folium.Marker(location=(14.5, -121.5),
                         icon=folium.Icon(color="blue"))
Vertice12 = folium.Marker(location=(14.5, -117.5),
                         icon=folium.Icon(color="blue"))
Vertice13 = folium.Marker(location=(14.5,-108.0),
                         icon=folium.Icon(color="blue"))
Vertice14= folium.Marker(location=(14.6,-123.8),
                         icon=folium.Icon(color="blue"))
Vertice15 = folium.Marker(location=(14.6,-116.7),
                         icon=folium.Icon(color="blue"))

#Se adjuntan todos los marcadores creados al estilo del mapa
Vertice1.add_to(mapa)
Vertice2.add_to(mapa)
Vertice3.add_to(mapa)
Vertice4.add_to(mapa)
Vertice5.add_to(mapa)
Vertice6.add_to(mapa)
Vertice7.add_to(mapa)
Vertice8.add_to(mapa)
Vertice9.add_to(mapa)
Vertice10.add_to(mapa)
Vertice11.add_to(mapa)
Vertice12.add_to(mapa)
Vertice13.add_to(mapa)
Vertice14.add_to(mapa)
Vertice15.add_to(mapa)

mapa.save("Dora.html")
