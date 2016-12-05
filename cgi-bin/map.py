#!/usr/bin/env python3
import cgi
import sys
import codecs
import os

form = cgi.FieldStorage()
filt = form.getlist("obj")
targetID = []
for i in filt:
    targetID.append(int(i))

filt = form.getlist("poly")
for i in filt:
    targetID.append(int(i))

if targetID == []:
    targetID = list(range(0,100))
#sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
#targetID = list(range(0,100))#get from url
MapScript = """
ymaps.ready(function () {
    var myMap = new ymaps.Map('map', {
            center: [58.140429, 52.674267],
            zoom: 14,
            controls: []
        }, {
            searchControlProvider: 'yandex#search'
        })
"""#Start script



def getJSmark(Mid, x,y,text,ico):
    text = text.replace("'",r"\'")
    #text = text.replace(r"\n","\n")
    s = ",\n myPlacemark" + str(Mid) + " = new ymaps.Placemark([" + str(x) + ", " + str(y) + "], {\n" 
    #s += "hintContent: '" + text + "',\n"
    s += "balloonContent: '" + text + "'\n" 
    s += "}, {\n" 
    s += "iconLayout: 'default#image',\n"
    s += "iconImageHref: '/images/" + ico + "',\n"
    s += "iconImageSize: [32, 32],\n"
    s += "iconImageOffset: [-16, -16]\n})"
    return s

#Open&Get std marks
def getObjects():
    global targetID
    importFiles = []
    #Main file of mark objects
    obj = open("objects/objects.txt", 'r')
    objs = obj.readlines()
    obj.close()
    for line in objs:
        if line == "\n":
            continue
        data = line.split()
        #Check dataType in target IDs
        if int(data[0]) in targetID:
            #Add
            importFiles.append((data[1],data[2]))
    return importFiles

#Add marks to script
def getMarks():
    global MapScript
    importFiles = getObjects()
    importPoints = []
    for i in importFiles:
        obj = open("objects/" + i[0], 'r')
        objs = obj.readlines()
        obj.close()
        for j in objs:
            data = j.split()
            importPoints.append(int(data[0]))
            MapScript += getJSmark(int(data[0]), float(data[1]), float(data[2]), " ".join(data[3:]), i[1]) + "\n"
        
    MapScript += ";"
    for i in importPoints:
        MapScript += "myMap.geoObjects.add(myPlacemark" + str(i) + ");\n"


def getJSpoly(Mid, points, text, backColor, MainColor, alpha, bold):
    text = text.replace("'",r"\'")
    text = text.replace('"',r'\"')
    s = "\n myGeoObject" + str(Mid) + """ = new ymaps.GeoObject({geometry: {type: "Polygon",coordinates: [["""
    s += points + ',\n'
    s += """]],fillRule: "nonZero"},properties: {balloonContent:" """
    s += text + """ "\n  }}, {fillColor:"""
    if backColor == "std":
        s += "'#00FF00',\n"
    else:
        s += "'" + backColor + "',\n"
        
    if MainColor == "std":
        s += "strokeColor: '#0000FF',\n"
    else:
        s += "strokeColor: '" + MainColor + "',\n"
        
    if alpha == "std":
        s += "opacity: 0.5,\n"
    else:
        s += "opacity: " + alpha + ",\n"
        
    if bold == "std":
        s += "strokeWidth: 5,\n"
    else:
        s += "opacity:" + bold + ",\n"
    s += "}),"
    return s

#Open&Get std poly
def getPolyFiles():
    global targetID
    importFiles = []
    #Main file of mark objects
    obj = open("polygon/polygon.txt", 'r')
    objs = obj.readlines()
    obj.close()
    for line in objs:
        if line == "\n":
            continue
        data = line.split()
        #Check dataType in target IDs
        if int(data[0]) in targetID:
            #Add
            importFiles.append((data[1]))
    return importFiles

#Add marks to script
def getPoly():
    global MapScript
    importFiles = getPolyFiles()
    importPoints = []
    for i in importFiles:
        obj = open("polygon/" + i, 'r')
        objs = obj.readlines()
        obj.close()
        for j in objs:
            data = j.split()
            importPoints.append(int(data[0]))
            MapScript += getJSpoly(data[0], data[1], " ".join(data[6:]), data[2],data[3],data[4],data[5]) + "\n"
        
    MapScript = MapScript[:-2] + ";"
    for i in importPoints:
        MapScript += "myMap.geoObjects.add(myGeoObject" + str(i) + ");\n"
    #Finalization
    #MapScript += "});"

def getFiltersObj():
    global targetID
    importFiles = []
    #Main file of mark objects
    obj = open("objects/objects.txt", 'r')
    objs = obj.readlines()
    obj.close()
    s = ""
    for i in objs:
        data = i.split()
        if i == '\n':
            continue
        if int(data[0]) in targetID:
            s += '<input type="checkbox" name="obj" value = "' + data[0] + '" checked>' + data[3] + "<Br>" + "\n"
        else:
            s += '<input type="checkbox" name="obj" value = "' + data[0] + '">' + data[3] + "<Br>" + "\n"
    return s

def getFiltersPoly():
    global targetID
    importFiles = []
    #Main file of mark objects
    obj = open("polygon/polygon.txt", 'r')
    objs = obj.readlines()
    obj.close()
    s = ""
    for i in objs:
        data = i.split()
        if i == '\n':
            continue
        if int(data[0]) in targetID:
            s += '<input type="checkbox" name="poly" value = "' + data[0] + '" checked>' + data[2] + "<Br>" + "\n"
        else:
            s += '<input type="checkbox" name="poly" value = "' + data[0] + '">' + data[2] + "<Br>" + "\n"
    return s
getMarks()
getPoly()
#Finalization
MapScript += "});"
#sys.exit(0)     
print("Content-type: text/html\n")

print("""
<!DOCTYPE html>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset="utf-8" />
    <title>Карта Глазова с метками</title>
    <link rel="shortcut icon" href="../images/ico.ico" type="image/x-icon">
    <!-- Если вы используете API локально, то в URL ресурса необходимо указывать протокол в стандартном виде (http://...)-->
    <script src="//api-maps.yandex.ru/2.1/?lang=en_RU" type="text/javascript"></script>
    
    <script type="text/javascript">
""")
print(MapScript)
print("""
      

    </script>

	<style>
        html, body {
            width: 100%;
            height: 100%;
            padding: 0;
            margin: 0;
        }
        #map {
            width: 80%;
            height: 100%;
            padding: 0;
            margin: 0;
            float:left;
        }
        #text{
            width: 18%;
            height: 98% - 5px;
            padding: 1%;
            margin: 0;
            float:right;
        }
        #footer {
            position: fixed;
            bottom:0;
            padding: 5px; 
            background: #FFFFFF;
            color: #000000; 
            width: 100%;
       }

    </style>
</head>
<body>


<div id="map" ></div>
<div id="text" >
<br>
     <form action="map.py">
      <p><b>Choose the objects</b><Br>""")
print(getFiltersObj())
print("<p><b>Choose the polygone</b><Br>")
print(getFiltersPoly())
print("""
      </p>
      <p><input type="submit" value="Submit"></p>
     </form>
    <div id="footer">
       
       <a href="https://github.com/AsciiShell/GlazovMap">Repository on GitHub</a>
    </div>
</div>

</body>
</html>
""")
