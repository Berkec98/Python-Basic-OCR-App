from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

ocr=pytesseract.image_to_string(Image.open('kimlik2.jpg'), lang="tur")
ad = (ocr[56:67])
soyad = (ocr[39:51])
cinsiyet=(ocr[69:70])
dogum=(ocr[71:81])
gecerlilik=(ocr[83:93])
serino=(ocr[95:105])
tckimlik=(ocr[113:120])
deneme = (ocr[0:34])

print(deneme)
print("İsim: " + ad)
print("Soyisim: " + soyad)
if (cinsiyet == "K"):
    print("Cinsiyet: "+cinsiyet+"ADIN")
else:
    print("Cinsiyet: "+cinsiyet+"RKEK")

print("Doğum Tarihi: " + dogum)
print("Geçerlilik Tarihi: " + gecerlilik)
print("Seri Numarası: " + serino)
print("TC Kimlik Numarası: " + tckimlik)





