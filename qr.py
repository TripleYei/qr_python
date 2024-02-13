import pyqrcode
import png
from pyqrcode import QRCode


print("Generador de código QR.")

msg = input("Escribe un mensaje/URL etc para crear su código QR: ")

code = pyqrcode.create(msg)

code.png("QRCODE.png", scale=5)

print("QR generado correctamente.")