from pyzbar.pyzbar import decode
from PIL import Image 

a = decode(Image.open("QR.png"))
print(a[0].data.decode())
