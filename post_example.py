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
