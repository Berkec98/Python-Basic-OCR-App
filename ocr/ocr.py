from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

ocr=pytesseract.image_to_string(Image.open('kimlik.jpg'), lang="tur")
giris = (ocr[2:34])
soyad = (ocr[101:110])
ad= (ocr[128:137])
cinsiyet=(ocr[175:178])
dogum=(ocr[164:172])
uyruk=(ocr[218:225])
serino=(ocr[206:215])
tckimlik=(ocr[89:100])

print(giris)
print ("İsim: " + ad)
print("Soyisim: " + soyad)
print("TC Kimlik No: " + tckimlik)
print ("Doğum tarihi: " + dogum[0] + dogum[1] + "." + dogum[2] + dogum[3] + "." + dogum[4] + dogum[5]+ dogum[6]+ dogum[7])
if (cinsiyet == "K/F"):
    print("Cinsiyet: KADIN")
else:
    print("Cinsiyet: ERKEK")
print("Seri Numarası: " + serino)
print("Uyruk: " + uyruk)

