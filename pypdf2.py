import PyPDF2
 
# reader nomli obyekt yaratib olamiz
reader = PyPDF2.PdfReader('Jane Eyre.pdf')
 
# Bu pdf faylining sahifalar sonini saqlaydi
x = len(reader.pages)
 
# tanlangan sahifalar sonini tanlaydigan o'zgaruvchini yaratish
pageobj = reader.pages[x-1]
 
# pdf fayldan olingan matnlar to'plami
text = pageobj.extract_text()

#olingan matnni ko'rsatilgan faylga yozib ketish
file = open(r"D:\\Python\\temp.txt", "a")
file.writelines(text)
