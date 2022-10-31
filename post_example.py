# PYTHONDA QIZIQARLI POSTLAR

# def key_values(**kwargs):
#     for key, value in kwargs.items():
#         print(f"Key: {key}\nValue: {value}")

# key_values(first_name="Erali", last_name="Abdinazarov")

# # *args
# def func(arg1, arg2, *args):

#     print("first arg: {}".format(arg1))
#     print("second arg: {}".format(arg2))

#     for arg in args:
#         print(arg)

# func(1,2,3,4,5)

# def args_kwargs(*args, **kwargs):
#     print("args: ", args)
#     print("kwargs: ", kwargs)

# args_kwargs(1, 2, 3, first="birinchi", middle="o'rta", last="oxirgi")


# # Object *args
# class car:
#     def __init__(self, *args):
#         self.speed = args[0]
#         self.color = args[1]

#     def get_car_info(self):
#         return f"Car color: {self.color}\nCar speed: {self.speed}"

# audi = car(200, 'red')
# bmw = car(250, 'black')

# print("Audi info:")
# print(audi.get_car_info(), "\n")
# print("BMW info:")
# print(bmw.get_car_info())

# # Object **kwargs
# class car:
#     def __init__(self, **kwargs):
#         self.speed = kwargs['sp']
#         self.color = kwargs['col']

#     def get_car_info(self):
#         return f"Car color: {self.color}\nCar speed: {self.speed}"

# audi = car(sp = 200, col = 'red')
# bmw = car(sp = 250, col = 'black')

# print("Audi info:")
# print(audi.get_car_info(), "\n")
# print("BMW info:")
# print(bmw.get_car_info())

# import phonenumbers
# from phonenumbers import geocoder, carrier

# phone_number = input("Enter your Phone Number: ")
# phoneNumber = phonenumbers.parse(phone_number)
# region = geocoder.description_for_number(phoneNumber, "uz")

# print(region)

# def filter_list(list, number):
#     if number != 0:
#         for i in list:
#             if i % 2 == 1:
#                 list.remove(i)
#     else:
#         for i in list:
#             if i % 2 == 0:
#                 list.remove(i)
#     print(list)
# filter_list([1,2,3,4,5,6,7,8,9], 1)
# filter_list([1,2,3,4,5,6,7,8,9], 0)

# lambda, filter
# a = [100, 2, 8, 60, 5, 4, 3, 31, 10, 11]
# filtered = list(filter(lambda x: x % 2 == 0, a))
# print(filtered)

# def power(n):

#     return lambda a: a ** n

# lmdb = power(2)
# print(lmdb(3))

# # nonlocal
# def external_func():
#   name = "Alijon"

#   def internal_func():
#     nonlocal name
#     name = "Valijon"

#   internal_func() 

#   return name

# print("Name:",external_func())

# # global
# def global_func():
#     global name
#     name = "John Doe"
#     return name

# print(global_func())
# print(name)


# class Person:
#     def __init__(self, first_name, last_name, age):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age

#     def full_name(self):
#         return f"{self.first_name} {self.last_name}"

# person = Person("Erali", "Abdinazarov", 22)
# full = person.full_name()
# print(full)

# class Student(Person):
#     def __init__(self, first_name, last_name, age, job):
#         super().__init__(first_name, last_name, age)
#         self.job = job

#     def full_name(self):
#         return super().full_name()

#     def info(self):
#         return f"Ismim {self.first_name} {self.last_name}, yoshim {self.age} da va kasbim {self.job} 👍"

# student = Student("Erali", "Abdinazarov", 22, "Dasturchi")
# print(student.full_name())
# print(student.info())


# n ta elementga ega massiv va k butun son berilgan. Massivning har bir elementini a[k] ga
# orttiruvchi programma tuzilsin. (1 <= k <= n)

# a = list(map(int, input("n ta son kiriting: ").split()))
# k = int(input("k ni kiriting: "))

# a_k = []

# for i in a:
#     l = i + a[k]
#     a_k.append(l)
# print(a_k)

# Array 83
# a = list(map(int, input("n ta son kiriting: ").split()))
# # k = int(input("k ni kiriting: "))
# ab = []

# for i in range(len(a)):
#     ab.append(a[i])
# print(ab)

# n = int(input("Son kiriting: "))
# a = []
# for i in range(n+1):
#     a.append(int(input("a["+str(i)+"]=")))
# # print(a)
# for j in range(len(a)):
#     a.pop(j)
# print(a)

# # Bubble Sort
# import random
# import time

# nums = list(range(10))
# random.shuffle(nums)
# print(f"Tartibsiz ro'yxat: {nums}")

# start_time = time.time()
# def bubble(nums):
#     n = len(nums)
#     swaps_count = 0

#     for i in range(n - 1):
#         if nums[i] > nums[i+1]:
#             nums[i], nums[i+1] = nums[i+1], nums[i]
#             swaps_count += 1

#     return swaps_count
# bubble(nums)

# def bubble_sort(nums):
#     n = len(nums)

#     for _ in range(n-1):
#         if bubble(nums) == 0:
#             break

# bubble_sort(nums)

# end_time = time.time()
# timer = end_time - start_time
# print(f"Bubble sort algoritmiga ketgan vaqt: {timer}")

# print(f"Tartiblangan ro'yxat: {nums}")


# Selection Sort
nums = [8, 5, 6, 7, 4, 2, 3]

def select(nums, start):
    n = len(nums)
    pos = start
    for i in range(start, n):
        if nums[i] < nums[pos]:
            pos = i
    return pos

select(nums, 0)

def selection_sort(nums):
    n = len(nums)
    for i in range(n):
        pos = select(nums, i)
        nums[pos], nums[i] = nums[i], nums[pos]
        print(nums)

selection_sort(nums)

def split_and_join(line):
    line_split = line.split(' ')
    t = "-".join(line_split)
    
    print(t)

split_and_join("this is a string")

# biron harf o'rniga boshqa bir harf qo'yish
def mutate_string(string, position, character):
    string_list = list(string)
    for i in range(len(string_list)):
        if int(position) == i:
            del string_list[i]
            string_list.insert(int(position), character)
    string = ''.join(string_list)
    return string

if __name__ == '__main__':
    s = input("Matn kiriting: ")
    i, c = input("index raqam probel tashlab belgi kiriting: ").split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)


def print_formatted(number):
    if number >= 1 and number <= 99:
        for i in range(1, number+1):
            decimal = i
            octal = oct(i)
            hexadecimal = hex(i)
            binary = bin(i)

            # a = len(str(decimal))
            # b = len(octal[2:])
            # c = len(hexadecimal[2:])
            # d = len(binary[2:])

            result = "{0:>2} {1:>3} {2:>2} {3:>7}".format(decimal, octal[2:], hexadecimal[2:].title(), binary[2:])
            print(result)

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)

a, b = map(int, input().split())
middle_arifmetik = (a+b)/2
middle_geometrik = (a*b)**(1/2)
if middle_arifmetik > middle_geometrik:
    print(">")
elif middle_geometrik > middle_arifmetik:
    print("<")
else:
    print("=")

n = int(input())
s = 0
if n > 0:
    for i in range(1, n+1):
        s += i
if n < 0:
    for i in range(n, 2):
        s += i
print(s)

n = int(input())
list_sort = []
for i in range(n):
    m = int(input())
    list_sort.append(m)

def sort(list_sort):
    for i in range(len(list_sort)-1):
        if list_sort[i] > list_sort[i+1]:
            list_sort[i], list_sort[i+1] = list_sort[i+1], list_sort[i]

sort(list_sort)

def sort1(list_sort):
    for j in range(len(list_sort)-1):
        if sort(list_sort) == 0:
            break

sort1(list_sort)
for i in list_sort:
        print(i)


if __name__ == '__main__':
    s = input()
    if s.isalnum():
        print("True")
    elif s.isalpha():
        print("True")
    elif s.isdigit():
        print("True")
    elif s.islower():
        print("True")
    elif s.isupper():
        print("True")
    else:
        print("False")

    lst = list(s)
    print(lst.isalnum())
    print(lst.isalpha())
    print(lst.isdigit())
    print(lst.islower())
    print(lst.isupper())

    print(bool(re.findall("[a-zA-Z0-9+]", s)))
    print(bool(re.findall("[a-zA-Z]", s)))
    print(bool(re.findall("[a-z0-9]", s)))
    print(bool(re.findall("[a-z+]", s)))
    print(bool(re.findall("A-Z+]", s)))

import textwrap

def wrap(string, max_width):
    return textwrap.fill(string, width=max_width)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)

# Berilgan sonni teskari tartibda chiqarish
def print_digit(num):
    """
        Kod bu yerga yozing!
    """
    if num == 0:
        print(0)
        return
    while num != 0:
        digit = num % 10
        print(digit)
        num //=10
number = int(input("Sonni kiriting: "))
print_digit(num=number)

# Berilgan sonni teskari bo'lgan sonni qaytaring
def reverse_digit(num):
    """
        kodni shu yerga yozing!
    """
    result = 0
    while num != 0:
        result *= 10
        digit = num % 10
        result += digit
        num //= 10
    print(result)
number = int(input("Son kiriting: "))
reverse_digit(num=number)

def reverse_digit(num):
    """
        kodni shu yerga yozing!
    """
    result = ''
    while num != 0:
        digit = num % 10
        result += str(digit)
        num //= 10
    print(result)
number = int(input("Son kiriting: "))
reverse_digit(num=number)

# Berilgan sonni ikkilik sanoq tizimiga o'tkazish
def reverse_digit(num: int) -> str:
    """
        kodni shu yerga yozing!
    """
    result = ''
    while num != 0:
        digit = num % 2
        result += str(digit)
        num //= 2
    print(result)

    
number = int(input("Son kiriting: "))
reverse_digit(num=number)

# Berilgan son ikkining darjasi ekanini tekshiring
def reverse_digit(num: int) -> bool:
    """
    kodni shu yerga yozing!
    """
    bit_count = 0
    while num != 0:
        bit_count += num & 1
        print("bir",bit_count)
        num = num >> 1
        print("ikki", num)
    print(bit_count == 1)

    
number = int(input("Son kiriting: "))
reverse_digit(num=number)


from math import factorial
class Solution:
    def solve(self, n):
        return factorial(n)

number = int(input("Sonni kiriting: "))
solution = Solution()
result = solution.solve(number)
print(result)


# 1 dan N gacha bo'lgan toq sonlar yig'indisini toping O(1) vaqtda
def sum_of_add_number(n: int) -> int:
    """
    Kodni shu yerga yozing!
    """
    s = 0
    for i in range(1, n, 2):
        s += i
    print(s)
sum_of_add_number(10)
end_time = time.time()

# Palindrom so'zlar
def is_palindrome(word: str) -> bool:
    low, high = 0, len(word) - 1

    while low < high:
        # print(word[low], word[high])
        if word[low] != word[high]:
            return False
        low += 1
        high -= 1
    return True
print(is_palindrome("kiyik"))


if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    s=0
    for i in student_marks[query_name]:
        s+=i
    midd = s/len(student_marks[query_name])
    print(f"{midd:.2f}")


from fractions import Fraction
from functools import reduce

def product(fracs):
    t = reduce(lambda a, b: a*b, fracs) # complete this line with a reduce statement
    return t.numerator, t.denominator

if __name__ == '__main__':
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    result = product(fracs)
    print(*result)

from functools import reduce
 
lst = [1, 3, 5, 6, 2]

sum_elements = reduce(lambda a, b: a+b, lst)
print("Ro'yxat elementlarining yig'indisi:",sum_elements)

max_element = reduce(lambda a, b: a if a > b else b, lst)
print("Ro'yxatdagi eng katta element:",max_element)


from fractions import Fraction
  
print (Fraction(11, 35))
  
print (Fraction(10, 18))

print (Fraction(1, 0))

print (Fraction(1.13))


def count_substring(string, sub_string):
    k = 0
    j = len(sub_string)
    for i in range(0, len(string)):
        # print(string[i:j])
        if string[i:j] == sub_string:
            k += 1
        j += 1
    return k

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)



def swap_case(s):
    return s.swapcase()

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)



a = int(input())
b = int(input())
print(a//b)
print(a%b)
print(divmod(a, b))

a=int(input())
b=int(input())
m=int(input())
print(pow(a,b))
print(pow(a,b,m))

a=int(input())
b=int(input())
c=int(input())
d=int(input())
k = a**b+c**d
print(k)

for i in range(1,int(input())):
    print(if"{i}"*)

n=int(input())
lst=set()
for i in range(n):
    country=input()
    lst.add(country)
print(len(lst))



# Djang s3 pip install django-storage
AWS_ACCESS_KEY_ID = ''
AWS_SECRET_ACCESS_KEY = ''
AWS_STORAGE_BUCKET_NAME = ''
AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = None
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

string = input("Matn kiriting: ")
def swap_case(string):
    return string.swapcase()

result = swap_case(string)
print(result)

# test
class Test:
    def __init__(self, id1, id2):
        self.id1 = id1
        self.id2 = id2

    def test(self, other):
        if self.id1 == other:
            print("test-1: successfully")
        else:
            print("test-1: Wrong answer")

    def test2(self, other):
        if self.id2 == other:
            print("test-2: successfully")
        else:
            print("test-2: Wrong answer")

tst = Test(1, 2)
tst.test(1)
tst.test2(3)

# class, isinstance, TypeError, @classmethod and magic methods
class Clock:
    __DAY = 86400

    def __init__(self, seconds: int):
        if not isinstance(seconds, int):
            raise TypeError("Must be of type int")
        self.seconds = seconds % self.__DAY

    @classmethod
    def __verify_data(cls, other):
        if not isinstance(other, (int, Clock)):
            raise TypeError("Must be of type int")

        return other if isinstance(other, int) else other.seconds

    def __eq__(self, other):
        sc = self.__verify_data(other)
        return self.seconds == sc

    def __lt__(self, other):
        sc = self.__verify_data(other)
        return self.seconds < sc

    def __gt__(self, other):
        sc = self.__verify_data(other)
        return self.seconds > sc

    def __le__(self, other):
        sc = self.__verify_data(other)
        return self.seconds <= sc

    def __ge__(self, other):
        sc = self.__verify_data(other)
        return self.seconds >= sc

    def __ne__(self, other):
        sc = self.__verify_data(other)
        return self.seconds != sc

c1 = Clock(2000)
c2 = Clock(1000)
print(c1 == c2)
print(c1 < c2)
print(c1 > c2)
print(c1 <= c2)
print(c1 >= c2)
print(c1 != c2)

# hash object
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

p1 = Point(1, 2)
p2 = Point(1, 2)

d = {}
d[p1] = 1
d[p2] = 2
print(d)
print(p1 == p2)
print(hash(p1) != hash(p2))
print(hash(p1), hash(p2), sep="\n")

from this import d
print(d)


# __len__ , __bool__
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __len__(self):
        print("__len__")
        return self.x * self.x + self.y + self.y

    def __bool__(self):
        print("__bool__")
        return self.x == self.y

p = Point(10, 10)
# print(bool(p))
if p:
    print("p object gives True")
else:
    print("p object gives False")


    # working with class
from datetime import date
  
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
  
    # a class method to create a
    # Person object by birth year.
    @classmethod
    def fromBirthYear(cls, name, year):
        return cls(name, date.today().year - year)
  
    # a static method to check if a
    # Person is adult or not.
    @staticmethod
    def isAdult(age):
        return age > 18
    
    def get_age(self):
        return self.fromBirthYear("Erali", 22)
  
person1 = Person('mayank', 21)
person2 = Person.fromBirthYear('mayank', 1996)
  
print(person1.age)
print(person2.age)
print("Age:", person1.get_age())
  
# print the result
print(Person.isAdult(22))


class Meta(type):
    def create_local_attrs(self, *args, **kwargs):
        for key, value in self.class_attrs.items():
            self.__dict__[key] = value

    def __init__(cls, name, bases, attrs):
        cls.class_attrs = attrs
        cls.__init__ = Meta.create_local_attrs

class Women(metaclass=Meta):
    title = "Python"
    content = "content"
    photo = "image"

w = Women()
print(w.__dict__)


# method types
class MethodTypes:

    # class atributi
    name = "Ali"

    def instanceMethod(self):
        # self kalit so'zi orqali instance atributini yaratish
        self.lastname = "Valiyev"
        print(self.name, self.lastname, sep="\n")

    @classmethod
    def classMethod(cls):
        # cls kalit so'zi orqali class atributiga kirish
        cls.name = "Botir"
        print(cls.name)

    @staticmethod
    def staticMethod():
        print("Bu statik metod")


m = MethodTypes()
m.instanceMethod()

MethodTypes.classMethod()
MethodTypes.staticMethod()


#excel file to sqlite3 information import
import pandas as pd
import sqlite3

db = sqlite3.connect(':memory:')
dfs = pd.read_excel('BotBaza.xlsx', sheet_name=None)
for table, df in dfs.items():
    df.to_sql(table, db)

import sqlite3
import pandas as pd
filename="script"
con=sqlite3.connect("basebot.db")
wb=pd.ExcelFile('BotBaza.xlsx')
for sheet in wb.sheet_names:
        df=pd.read_excel(filename+'.xlsx',sheetname=sheet)
        df.to_sql(sheet,con, index=False,if_exists="replace")
con.commit()
con.close()


# class
class Geom:
    name = "Geom"

    def __init__(self, x1, y1, x2, y2):
        print(f"Geom ishlayapti! {self.__class__}")
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.fill = 0


class Line(Geom):
    def draw(self):
        print("Chiziq chizish")

class Rect(Geom):
    def __init__(self, x1, y1, x2, y2, fill=None):
        super().__init__(x1, y1, x2, y2)
        print("Rect ishlayapti!")
        self.fill = fill

    def draw(self):
        print("Chiziq chizish")

l = Line(0, 0, 10, 20)
r = Rect(1,2,3,4)
print(r.__dict__)


# data science
from sklearn import tree

clf = tree.DecisionTreeClassifier()

# ma'lumotlarni yig'amiz
# quyoshli_kunlar, yomg'irli_kunlar, qorli_kunlar

x = [
    [220, 110, 35], [290, 60, 15],
    [260, 75, 30], [210, 140, 15],
    [200, 140, 25], [180, 180, 5],
    [180, 135, 50], [205, 120, 35],
    [110, 180, 75], [95, 197, 73]
]

y = [
    'yaxshi', 'yomon', "o'rtacha", 'yaxshi', "o'rtacha", 'yomon', 'yaxshi', "o'rtacha",        'yomon', 'yomon'
    ]

clf = clf.fit(x, y)
taxmin = clf.predict([[200, 65, 100]])
print(taxmin)


# magic methods
class Cat:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"{self.__class__}: {self.name}"

    def __str__(self):
        return f"{self.name}"

    def __len__(self):
        return len(self.name)

    def __abs__(self, other):
        return other

c = Cat(name="Mosh")
print(str(c))
print(repr(c))
print(len(c))
print(abs(-5))


# all, map
def true_x(a):
    return a == 'x'

P = ['x', 'x', 'o', '0', 'x', 'o', 'x', 'x', 'x']

print(P[::3], P[1::3], P[2::3])

row_1 = all(map(true_x, P[:3]))
row_2 = all(map(true_x, P[3:6]))
row_3 = all(map(true_x, P[6:]))

col_1 = all(map(true_x, P[::3]))
col_2 = all(map(true_x, P[1::3]))
col_3 = all(map(true_x, P[2::3]))

print(row_1, row_2, row_3)
print(col_1, col_2, col_3)


# matndan ovozga
# import pyttsx3
# import os
# dis2 = pyttsx3.init()
# dis2.setProperty('rate', 150)
# dis2.setProperty('volume', 0.7)
# fil=open('aql.txt', 'r')
# matn=fil.read()
# # matn = input("Matn kiriting: ")
# dis2.say("Assalomu alaykum! Pythonda TTS dan foydalanish.")
# dis2.say(matn)
# dis2.save_to_file(matn,'test.mp3')
# dis2.runAndWait()
# os.system('music/test.mp3')

# class Person:
#     def __init__(self, first_name, last_name, age):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age

#     def info(self):
#         return f"Name: {self.first_name}\nSurname: {self.last_name}\nAge: {self.age}"

# class Student(Person):
#     def __init__(self, first_name, last_name, age, group):
#         super().__init__(first_name, last_name, age)
#         self.group = group

#     def info(self):
#         return f"Name: {self.first_name}\nSurname: {self.last_name}\nAge: {self.age}\nGroup: {self.group}"

# student = Student("Ali", "Olimov", 23, "9-19")
# print(student.info())

# n = int(input("Enter the number: "))
# suma = 0
# mult = 1
 
# while n > 0:
#     digit = n % 10
#     suma = suma + digit
#     mult = mult * digit
#     n = n // 10
 
# print("Total:", suma)
# print("Multiplication:", mult)


# from random import randint
# from math import log10, floor

# def human_format(num, ends=["", "K", "M", "B", "T"]):
#     # divides by 3 to separate into thousands (...000)
# 	return ends[int(floor(log10(num))/3)]

# if __name__ == '__main__':
#     for i in range(10):
#         x = randint(1,10**i)
#         print(x, human_format(x))


####################################################

# from collections import Counter, defaultdict

# def build_counter(word):
#     counter = defaultdict(int)
#     for char in word:
#         counter[char] += 1
#     return counter

# def is_anogram(word1:str, word2:str) -> bool:

#     counter1 = Counter(word1)
#     counter2 = Counter(word2)
#     print(counter1)
#     print(counter2)
#     return counter1 == counter2


# print(is_anogram("mosh", "shom"))

################################################

# from collections import Counter, defaultdict

# def build_counter(word):
#     counter = defaultdict(int)
#     for char in word:
#         counter[char] += 1
#     return counter

# def is_anogram(word1:str, word2:str) -> bool:

#     counter = build_counter(word1)

#     for char in word2:
#         counter[char] -= 1
#     return all(val == 0 for val in counter.values())
#     # for val in counter.values():
#     #     if val != 0:
#     #         return False
#     # return True

# print(is_anogram("mosh", "shom"))

###############################################
# def build_counter(word):
#     counter = dict()
#     for char in word:
#         if char not in counter:
#             counter[char] = 1
#             continue
#         counter[char] += 1
#     return counter


# def is_anogram(word1:str, word2:str) -> bool:

#     counter1 = build_counter(word1)
#     counter2 = build_counter(word2)
#     print(counter1)
#     print(counter2)
#     return counter1 == counter2


# print(is_anogram("mosh", "shom"))
######################################################


#######################################################
# def is_anogram(word1:str, word2:str) -> bool:

#     counter1 = dict()
#     counter2 = dict()

#     for char in word1:
#         if char not in counter1:
#             counter1[char] = 1
#             continue
#         counter1[char] += 1

#     for char in word2:
#         if char not in counter2:
#             counter2[char] = 1
#             continue
#         counter1[char] += 1

#     return counter1 == counter2

# print(is_anogram("mosh", "shom"))

#####################################################


# Misol: 
# two_sum([1,4,5,2], 3) => True
# two_sum([1,4,5,2], 8) => False


# def two_sum(arr: list[int], target: int) -> bool:
#     complements = {}

#     for index, num in enumerate(arr):
#         print("ayr:",target - num)
#         complements[target - num] = index
#     print(complements)

#     for index, num in enumerate(arr):
#         if num in complements and complements[num] != index:
#             # print(num, index)
#             return True
#     return False

# print(two_sum([1,4,5,2], 3))


# def enumerate_func(lst: list[int]) -> int:

#     for index, num in enumerate(lst):
#         print('index:',index, 'number:',num)
# print("Index va o'sha index'dagi son:\n")
# enumerate_func(lst = [12,25,3,4,42])


# regex
import re
from tkinter import N
# re.search
# boshlanishi va tugash va boshqa hallarni tekshiradi.
text = "hello guys what is guys"

text_start = re.search('^h', text)
text_end = re.search('s$', text)
text_none = re.search('y$', text)

print(text_start)
print(text_end)
print(text_none)

if text_start and text_end:
    print('Yes')
else:
    print('No')

# re.findall
# matnni ichidan kiritgan so'zni izlab topib list ko'rinishida qirqib oladi.
re_text1 = re.findall('^hello', text)
print(re_text1)

# re.split
# bo'sh joy bo'yicha split qiladi.
text_split = re.split("\s", text)
text_split_2 = re.split("\s", text, 2)
print(text_split)
print(text_split_2)

# re.sub
# bo'sh joyni berilgan belgi bilan almashtirib beradi va soni bo'yicha ham yuqoridagi ishni bajaradi
text_sub = re.sub("\s", "5", text)
text_sub_2 = re.sub("\s", "5", text, 2)
print(text_sub)
print(text_sub_2)




n = 125

S = n ** 2
P = 4 * n

print("Yuzasi:",S)
print("Peremetri:",P)


####### 2-qism ###########
# regex
import re
# re.search
# boshlanishi va tugash va boshqa hallarni tekshiradi.
text = "hello guys what is hi"

text1= re.search(r'\bg\w+', text)
text2 = re.search(r'\bg\w+', text)
text3 = re.search(r'\bg\w+', text)


# span() boshlanish va yakuniy pozitsiyalarini o'z ichiga olgan tuple qaytaradi.
print(text1.span())
# funktsiyaga kiritilgan satrni chop etadi.
print(text2.string)
# group() satrning mos keladigan qismini qaytaradi
print(text3.group())


######## dict and input #########
# user_info = dict()

# name = input(">>> Enter Name:")
# user_info["name"] = name

# username = input(f">>> {name} enter username:")
# user_info["username"] = username

# email = input(f">>> {name} enter email:")
# user_info["email"] = email

# password = input(f">>> {name} enter password:")
# user_info["password"] = password

# print(f"User info:\n\nName: {name}\nUsername: {username}\nE-mail: {email}\nPassword: {password}")
# print(f"Dictionary:\n{user_info}")

####### list ##########
mylist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(mylist)
# ro'yxat elementlariga kirish
print(mylist[0])
print(mylist[-1])
print(mylist[:2])
print(mylist[4:])
print(mylist[-3:-1])
print(mylist[2:6])

# ro'yxat elementlarini o'zgartirish
mylist[1] = "watermelon"
print(mylist)
mylist[1:2] = ["blackcurrant", "watermelon"]
print(mylist)
# ro'yxatga element qo'shish
# insert() - berilgan indexga ro'yxat elementini kiritish
mylist.insert(4, "watermelon")
print(mylist)
mylist.append("watermelon")
print(mylist)
tuple_e = ("kiwi", "orange")
mylist.extend(tuple_e)
print(mylist)

# # rjust
# string = "hello everybody"
# right_just = string.rjust(len(string) + 10, '*')
# print(right_just)
# right_just1 = string.rjust(len(string) + 10, '9')
# print(right_just1)
# right_just2 = string.rjust(len(string) + 10, 'a')
# print(right_just2)

# # ljust
# string = "hello everybody"
# left_just = string.ljust(len(string) + 10, '*')
# print(left_just)
# left_just1 = string.ljust(len(string) + 10, 'a')
# print(left_just1)
# left_just2 = string.ljust(len(string) + 10, '5')
# print(left_just2)

# random sorting
from random import randint

n = int(input("Enter a Number: "))
number_list = []
for i in range(n):
    number_list.append(randint(1, 99))
print(number_list)

for i in range(n - 1):
    for j in range(n-i-1):
        if number_list[j] > number_list[j+1]:
            number_list[j], number_list[j+1] = number_list[j+1], number_list[j]
print(number_list)


# class
class Car:
    def __init__(self, top_speed: int) -> None:
        self.top_speed = top_speed

    def drive(self):
        print("Driving")

def create_fast_car_(car_class: type[Car], top_speed: int):
    return car_class(top_speed=top_speed)
create_fast_car_(Car, 120).drive()


import numpy as np
import scipy as sp
import matplotlib as mp
import pandas as pd
import sklearn as sl
import seaborn as sb

import numpy
import scipy
import matplotlib
import pandas
import sklearn
import seaborn

# pip install numpy
# pip install pandas
# pip install scipy
# pip install matplotlib
# pip install seaborn
# pip install scikit-learn

arr = np.array([1, 2, 3, 4], dtype=int)

print(arr)
print(type(arr))
