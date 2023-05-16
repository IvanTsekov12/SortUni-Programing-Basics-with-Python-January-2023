import pyqrcode
import png
from pyqrcode import QRCode

address = 'https://www.youtube.com/watch?v=WUQxF2N7L64'
url = pyqrcode.create(address)
url.png('qrcode.png', scale=8)