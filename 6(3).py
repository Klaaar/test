# class Year:
#     def __init__(self,season,days):
#         self.__season = season
#         self.__days = days
#
#     @property
#     def season(self):
#         return self.__season
#
#     @season.setter
#     def season(self,season):
#         self.__season = season
#
#     @property
#     def days(self):
#         return self.__days
#
#     @days.setter
#     def days(self, days):
#         self.__days = days
#
#
#     # def get_days(self):#геттеры
#     #     return self.__days
#     # def get_season(self):
#     #     return self.__season
#     #
#     # # def set_days(self,days):#сеттеры
#     # #     self.__days = days
#     # def set_season(self,season):
#     #     self.__season = season
#
#     def set_days(self,days):
#         if days == 365 or days == 366:
#             self.__days = days
#         else:
#             raise Exception('Некорректное значение')
#
# year = Year('зима',365)
# # print(year.get_days()) это к геттерам
# # year.set_days(365)
# # year.set_season('осень')
# print(year.season)
# print(year.days)
# ~~~~~~~~~~~~~~~~~~~~~~~~~
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def name(self):  # здесь нужно назвать функцию как атрибут!!!!!!!и геттор должен будет идти после сеттера
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @name.deleter
    def name(self):
        print('Удалено')
        self.__name = None

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age <= 0:
            raise ValueError('Вы еще не родились :/')
        self.__age = age

    @age.deleter
    def age(self):
        print('Удалено')
        self.__age = None
person = Person('Ivan', 1)
print(person.name)
print(person.age)
del person.name
del person.age
print(person.name)
print(person.age)

