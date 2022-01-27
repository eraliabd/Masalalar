""" Muallif: Abdinazarov Erali
    10-01-2022
    Hodimni ro'yxatga olish dasturi
"""
import re

kirit = "....... HODIMLAR RO'YXATI .......\n"
kirit += ">>> Hodimlar ro'yxatini ko'rish uchun 1 ni bosing\n"
kirit += ">>> Yangi hodim kiritish uchun 2 ni bosing\n"
kirit += ">>> Tizimdan chiqish uchun (q) ni bosing\n>>>"

hodim1 = {
    'ism':'Alijon',
   'familiya':'Valiyev',
   'yoshi':22,
   'lavozim':'Dasturchi',
   'oylik':'$1200',
   'email':'alijonvaliyev@gmail.com',
   'login':'1112Az',
   'parol':'A1112@#$%es'}

hodim2 = {
    'ism':'Valijon',
   'familiya':'Aliyev',
   'yoshi':25,
   'lavozim':'Dasturchi',
   'oylik':'$1000',
   'email':'valijonaliyev@gmail.com',
   'login':'2223Sd',
   'parol':'E2223@#$%aw'}
hodimlar = [hodim1,hodim2]

while True:
    qiymat = input(kirit)
    if qiymat == '1':
        print("\n---- Hodimlar ro'yxati ----")
        for info in hodimlar:
            print(f"Ismi: {info['ism']}\nFamiliyasi: {info['familiya']}\n"
                  f"Yoshi: {info['yoshi']}\nLavozimi: {info['lavozim']}\n"
                  f"Oyligi: {info['oylik']}\nE-mail: {info['email']}\n"
                  f"Login: {info['login']}\nParol: {info['parol']}")
            print("................................\n")
        menyu = "Bosh bo'limga qaytish uchun 0 ni bosing\n>>>"
        input(menyu)
        if menyu == '0':
            continue
    if qiymat == 'q':
        break

    if qiymat == '2':
        print("----Yangi hodim qo'shish")
        hodim = {}
        hodim['ism'] = input("Hodimning ismi >>> ")
        hodim['familiya'] = input("Hodimning familiyasi >>> ")
        hodim['yoshi'] = int(input("Hodimning yoshi >>> "))
        hodim['lavozim'] = input("Hodimning lavozimi >>> ")
        hodim['oylik'] = input("Hodimning oyligi >>> ")
        
        andoza = '[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+'
        matn = "Email kiriting:  "
        
        while True:
            hodim['email'] = input(matn)
            email = hodim['email'] 
            if re.match(andoza,email):
                print("Email to'g'ri kiritildi.")
                break
            else:
                print("Email talabga javob bermaydi.")
        
        hodim['login'] = input("Login kiriting: ")
        
        andoza1 = '^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$'
        prl = "Parol kiriting: "
        prl += "(kamida 8 ta belgidan iborat, 1 ta lotin bosh va 1 ta kichik harf, "
        prl += "1 ta son va 1 ta maxsus belgi bo'lishi kerak)\nParol: "
        
        while True:
            hodim['parol'] = input(prl)
            password = hodim['parol']
            if re.match(andoza1,password):
                print("Parol to'g'ri kiritildi!\n")
                break
            else:
                print("Parol talabga javob bermaydi. Yana kiritib ko'ring-->")
                
        hodimlar.append(hodim)
        print("Hodim ro'yxatga muvaffaqiyatli qo'shildi!")
        
        menyu = "Bosh bo'limga qaytish uchun 0 ni bosing\n>>>"
        input(menyu)
