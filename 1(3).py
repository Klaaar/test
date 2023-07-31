# zp = 200000
# name = 'Danil'
# print(f'{name} он зарабатывает  {zp}  рублей в месяц')
# print(f'это {name}, он зарабатывает {zp*12} рублей в год')
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# baza = {'name':'Danil',
#         'zp':200000}
# print(f"{baza['name']} зарплата в месяц = {baza['zp']}")
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#реализация в виде словаря и списка, если сотрудников несколько
# big_baza = [
#     {'name':'Danil',
#          'zp':200000},
#     {'name':'Olga',
#          'zp':250000},
#     {'name':'Irina',
#          'zp':200000}
# ]
# for baza in big_baza:
#     print(f'Имя: {baza["name"]}, зарплата: {baza["zp"]}')
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Увольняем Данила.. метод remove
# for baza in big_baza:
#     if baza['name'] == 'Danil':
#         big_baza.remove(baza)
#         break
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Нанимаем сотрудника..
# new_p = {'name':'Kirill',
#          'zp':220000}
# big_baza.append(new_p)
# print(big_baza)
#
# #Как узнать сколько сотрудников в компании
# print(len(big_baza))
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# class Employee:
#     def __init__(self,name,zp,on_vacation,is_good_employee):
#         self.is_good_employee = is_good_employee
#         self.on_vacation = on_vacation
#         self.name = name
#         self.zp = zp
#     def get_info(self):
#         if self.on_vacation == True:
#             return f'{self.name} зарплата в месяц = {self.zp}, в отпуске'
#         else:
#             return f'{self.name} зарплата в месяц = {self.zp},не в отпуске'
# baza = [Employee('Danil', 200000,True),Employee('Olga', 250000,False), Employee('Irina', 2000000,True)]
# #выводим инфу о сотрудниках
# for i in baza:
#     print(i.get_info())
#```````````````````````````````````````````````````````````````````````````````````````````````````````````````
class Employee:
    def __init__(self,name,zp,is_good_employee):
        self.name = name
        self.zp = zp
        self.is_good_employee = is_good_employee
    def get_info(self):
        if self.is_good_employee == True:
            return f'{self.name}, зарплата = {self.zp}, хороший работник'
        else:
            return f'{self.name}, зарплата = {self.zp}, плохой работник'
baza = [Employee('Kirill', 150000,True), Employee('Alexandr', 160000,False), Employee('Olga',100000,True),Employee('Karina',150000,True), Employee('Marina', 120000,True)]
for i in baza:
    if baza['is_good_employee'] == False:
        baza.remove()
    print(baza)














