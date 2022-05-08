# "Matn kiritiladi va n soni kiritiladi matndagi n indexga to'g'ri keladigan harfni o'chirib tashlaydi."

def missing_char(str, n):
    s = []
    t = ""
    for i in range(len(str)):
        s.append(str[i])
    for j in range(len(s)):
        if j==n:
            s.remove(s[j])
    for k in s:
        t += k
    print(t)
n = int(input("Son kiriting: "))
string = input("Matn kiriting: ")
missing_char(string, n)

# string = "hello"
# n = 2
# Natija: helo
