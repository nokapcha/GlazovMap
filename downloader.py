import urllib, urllib.request
#https://vec01.maps.yandex.net/tiles?l=map&v=4.130.1&x=42346&y=19746&z=16&scale=1&lang=ru_RU
for i in range(42340, 42360):
    for j in range(19740, 19760):
        testfile = urllib.request.URLopener()
        testfile.retrieve("https://vec01.maps.yandex.net/tiles?l=map&v=4.130.1&x=" + str(i) + "&y=" + str(j) + "&z=16&scale=1&lang=ru_RU" , str(i) + "." + str(j) + ".png")
