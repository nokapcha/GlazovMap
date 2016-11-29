#!/usr/bin/env python3
import cgi
import sys
import codecs
import os
def getJSmark(Mid, x,y,text,ico):
    s = ",\n myPlacemark" + str(Mid) + " = new ymaps.Placemark([" + str(x) + ", " + str(y) + "], {\n" 
    s += "hintContent: '" + text[:-1] + "',\n"
    s += "balloonContent: ''\n" 
    s += "}, {\n" 
    s += "iconLayout: 'default#image',\n"
    s += "iconImageHref: '/images/" + ico + "',\n"
    s += "iconImageSize: [32, 32],\n"
    s += "iconImageOffset: [-16, -16]\n})"
    return s

sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())


targetID = list(range(0,100))#get from url
obj = open("objects/objects.txt", 'r')
objs = obj.readlines()
obj.close()
importFiles = []
importPoints = []
MapScript = """
ymaps.ready(function () {
    var myMap = new ymaps.Map('map', {
            center: [58.140429, 52.674267],
            zoom: 14
        }, {
            searchControlProvider: 'yandex#search'
        })
"""
for line in objs:
    if line == "\n":
        continue
    data = line.split()
    if int(data[0]) in targetID:
        #Add
        importFiles.append((data[1],data[2]))


####################################
for i in importFiles:
    obj = open("objects/" + i[0], 'r')
    objs = obj.readlines()
    for j in objs:
        data = j.split('$')
        importPoints.append(int(data[0]))
        MapScript += getJSmark(int(data[0]), float(data[1]), float(data[2]), data[3], i[1]) + "\n"
    obj.close()
MapScript += ";"
for i in importPoints:
    MapScript += "myMap.geoObjects.add(myPlacemark" + str(i) + ");\n"
MapScript += "});"
#sys.exit(0)     
print("Content-type: text/html\n")

print("""
<!DOCTYPE html>
<html>
<head>
    <title>Карта Глазова с метками</title>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <!-- Если вы используете API локально, то в URL ресурса необходимо указывать протокол в стандартном виде (http://...)-->
    <script src="//api-maps.yandex.ru/2.1/?lang=ru_RU" type="text/javascript"></script>
    
    <script type="text/javascript">
""")
print(MapScript)
print("""
      

    </script>

	<style>
        html, body, #map {
            width: 90%; height: 100%; padding: 0; margin: 0;
        }
    </style>
</head>
<body>

<div style="width:10%; float:left"> <p>Что-то работает</p> </div>
<div id="map" style="width:100% ;float:right"></div>
</body>
</html>
""")
