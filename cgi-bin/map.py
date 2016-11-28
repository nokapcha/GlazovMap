#!/usr/bin/env python3
import cgi
import sys
import codecs

sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
#obj = open("../objects/objects.txt", 'r')
#objs = 
           
           
print("Content-type: text/html\n")

print("""
<!DOCTYPE html>
<html>
<head>
    <title>Примеры. Задание собственного изображения для метки</title>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <!-- Если вы используете API локально, то в URL ресурса необходимо указывать протокол в стандартном виде (http://...)-->
    <script src="//api-maps.yandex.ru/2.1/?lang=ru_RU" type="text/javascript"></script>
    
    <script type="text/javascript">
    
ymaps.ready(function () {
    var myMap = new ymaps.Map('map', {
            center: [58.140429, 52.674267],
            zoom: 14
        }, {
            searchControlProvider: 

'yandex#search'
        }),
        myPlacemark = new ymaps.Placemark([58.141135, 52.643068], {
            hintContent: 'ГОРОД',
            balloonContent: 'Это красивая метка'
 

       }, {
            // Опции.
            // Необходимо указать данный тип макета.
            iconLayout: 'default#image',
            // Своё изображение иконки метки.
      

      iconImageHref: '/images/schools.png',
            // Размеры метки.
            iconImageSize: [30, 42],
            // Смещение левого верхнего угла иконки относительно
     

       // её "ножки" (точки привязки).
            iconImageOffset: [-3, -42]
        });

    myMap.geoObjects.add(myPlacemark);
});

    </script>

	<style>
        html, body, #map {
            width: 90%; height: 100%; padding: 0; margin: 0;
        }
    </style>
</head>
<body>

<div style="width:10%; float:left"> <p>TEXTTEXT</p> </div>
<div id="map" style="width:100% ;float:right"></div>
</body>
</html>
""")
