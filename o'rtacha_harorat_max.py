# -*- coding: utf-8 -*-
"""
Muallif: Abdinazarov Erali 26.01.2022
Masala: [1:365] m-oy
    Kabisa bo'lmagan biror bir yilning har bir kunining haroratini bildiruvchi t vektor bo'yicha, 
    o'rtacha oylik harorati eng katta bo'lgan oyning nomi m aniqlansin.
"""

m = []
oylar = ['yanvar','fevral','mart','aprel','may','iyun','iyul','avgust','sentyabr','oktyabr','noyabr','dekabr']
while True:
    year = int(input("Biron yilni kiriting: "))
    if (year%4==0 and year%100!=0) or year%400==0:
        print(f"{year}-yil, Kabisa yili, qaytadan urinib ko'ring.") 
        continue
    else:
      print(f"{year}-yil, Kabisa yili emas!")
      for i in oylar:
          t = list(map(int, input(f"{i.title()} oyining kunlik haroratlari: ").split()))
          if i=='fevral':
              t1 = sum(t)//28
          elif i=='aprel' and i=='iyun' and i=='sentyabr' and i=='noyabr':
              t1 = sum(t)//30
          else:
              t1 = sum(t)//31
          m.append(t1)
      
      break

for i in range(12):
    if m[i]==max(m):
        for j in range(12):
            if j==i:
                print("m =",oylar[j])
