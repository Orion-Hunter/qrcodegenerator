import os
import sys
import pyqrcode

class QRCodeGenerator: 
    def __init__(self, links):
        if not os.path.exists("./codes"):
            os.mkdir("codes")
        self.links = links
           
    def gerarQrCodes(self):
        for r in self.links:
            url = pyqrcode.create(r)
            url.png("./codes/"+r[50:len(r)-2]+".png", scale=20)
        