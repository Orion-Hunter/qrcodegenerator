import os
import pyqrcode
import sys

if  not os.path.exists("./codes"):
    os.mkdir("codes")


f = open("./links.txt", "r")

for r in f:
    url = pyqrcode.create(r)
    url.png("./codes/"+r[50:len(r)-2]+".png", scale=20)
