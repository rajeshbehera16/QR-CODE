import pyqrcode
import png
from pyqrcode import QRCode
s="www.netflix.com"
url=pyqrcode.create(s)
url.svg("netflix.svg", scale=8)
url.png("netflix.png", scale=6)