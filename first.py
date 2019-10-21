'''import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd="C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"
img=Image.open('test4.jpg')enjoy
result=pytesseract.image_to_string(img)
print(result)'''
from PIL import Image
import PIL.Image

from pytesseract import image_to_string
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'
TESSDATA_PREFIX = 'C:/Program Files (x86)/Tesseract-OCR'
output = pytesseract.image_to_string(PIL.Image.open('fp.jpg').convert("RGB"), lang='eng')
#print(output)
with open("nresult.txt",mode="w") as file:
    file.write(output)
