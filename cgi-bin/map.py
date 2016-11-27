#!/usr/bin/env python3
import cgi
import sys
import codecs

sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
print("Content-type: text/html\n")
cssf = open('cgi-bin/tooltip.css','r')
css = cssf.readlines()
print("""<!DOCTYPE html>
<html>
 <head>
  <meta charset="utf-8">
  <title>Glazov map</title>
   <style type="text/css">""")
for i in css:
    print(i)
print("""
  </style>

   </head>
 <body>
  <p>Текст</p>
  
  <div class="tooltip">
  <img src="/schools.png">
  <span class="tooltiptext">Макулатура</span>
</div>

<div class="tooltip">Hover over me
  <span class="tooltiptext">Tooltip text</span>
</div>
 </body>
</html>""")
