from module.generator import QRCodeGenerator

if __name__ == '__main__':
    f = open("./links.txt", "r")
    QRCodeGen = QRCodeGenerator(f)
    QRCodeGen.gerarQrCodes()
    
