# # # # def say_hi(name):
# # # #     print(f"Hello {name}!")
# # # #
# # # #
# # # # print(say_hi("Gosho"))
# # #
# # #
# # # class Person:
# # #     def __init__(self, first_name, last_name, age=0):
# # #         self.first_name = first_name
# # #         self.last_name = last_name
# # #         self.age = age
# # #
# # #     def say_hello(self):
# # #         return f"Hello {self.first_name} {self.last_name}! "
# # #
# # #     def say_goodbye(self):
# # #         return f"Goodbye {self.first_name} {self.last_name}! "
# # #
# # #     def say_welcome(self):
# # #         return f"Welcome {self.first_name} {self.last_name}! "
# # #
# # #
# # # boris = Person("Boris", "Borisov", 21)
# # # boris.age += 1
# # #
# # # print(boris.age)
# #
# #
# # class Test:
# #     phone_number = '+3598521425144'
# #
# #     value = 52
# #
# #     def __init__(self):
# #         self.value = 42
# #
# #     @classmethod
# #     def phone_data(cls):
# #         return cls.phone_number
# #
# #
# # print(Test.value)
# #
# # obj = Test()
# # print(obj.phone_data())
#
#
# class Test:
#     __pi = 3.14
#
#     def __init__(self):
#         pass
#
#
# test = Test()
# test.__pi += 10
# print(test.__pi)
