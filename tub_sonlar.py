# -*- coding: utf-8 -*-
"""
@Muallif: Erali Abdinazarov 13/11/2021
"""
N = int(input(">>>"))
#k=int(input())        # k ni kiritish
l=1                 
P=[]                  # P tizim qatori bo`shliqqa teng
P.append(2)           # P tizim qatoriga 2 tub sonini qo`shish                 
for i in range(3,N):  # i 3 dan N gacha asosiy cikl 
    bool=True         # i ning tub sonligi "rost"
    for j in range(2,i-1):   
       if i%j==0:     # barcha i/j larni qoldiqsiz bo`linishini tekshirish
           bool=False # i ning tub sonligi "yolg`on"
    if bool:          # agar mantiqiy ifoda "rost" bo`lsa
       l=l+1          # tub sonlar 1 ga ortdi
       P.append(i)    # P tizim qatoriga i tub sonni qo`shish 
print(f"Tub sonlar ro'yxati:\n{P}")
print(f"Soni: {l} ta")


    
   
