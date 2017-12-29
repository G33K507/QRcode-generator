import pyqrcode
import png

string = raw_input("Please enter something: ")

img = pyqrcode.create(string)
img.show(img)
