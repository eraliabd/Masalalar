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
