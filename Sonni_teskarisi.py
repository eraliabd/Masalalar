# Oddiy usulda yechilishi.
n = int(input("son: "))
k=""
for i in range(n):
    a = n%10
    k += str(a)
    n = n//10
    if n==0:
        break
print(int(k))

# Funksiya ko'rinshi.
def Teskari(n):
    k=""  #Bo'sh string yaratib olamiz
    for i in range(n):
        a = n%10 #oxiridagi sonni qirqib oladi
        k += str(a) #k ga qo'shib boradi
        n = n//10 
        if n==0:
            break #agar n tugab qolsa ya'ni nolga teng bo'lib qolsa tskil to'xta degani
    print(k)
n = int(input("son: "))
Teskari(n)
