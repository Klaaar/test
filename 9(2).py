#def func(a,b, c=0):
#    print(a)
#    print(b)
#    print(c)

#func(b=1,a=8,c=5)#сначала позиционные(8),потом именованные(a=8)
#---------------------------------------
#def func(*args):#аргс принимает любое кол-во ПОЗИЦИОННЫХ аргументов
#   s = 0
#    for i in args:
#        s+= i
#    print(s)
#func(1,8,5,8,2345)#находит сумму неогранич кол-ва оргументов
#---------------------------------------
#def func(*args,**kwargs):#выводит именнованные аргументы в виде словаря
#    print(args)
#    print(kwargs)
#func(1,8,c=1,b=5,flag=True)
#------------------------------------------------
#def func(*args,**kwargs):#выводит именнованные аргументы в виде словаря
#    print(args)
#   print(kwargs.get('flag'))#выводит без ошибки при отсутсвии нужного ключа
#func(1,8,c=1,b=5,flag=True)
#--------------------------------------------------
# a = 5
# b = 6
# if a < b:
#     print('+')
# else:
#     print('-')
#
# print('+' if a<b else '-')#тоже самое, что и чуть выше..(это тернарный оператор(сначала писать что выводить если условие правдиво, потом иначе и то, что выводит при иначе))
# c = 'Верно' if a<b else 'Неверно'
#- - - - - - - - - - - - - - - - - - - - - - - -
# val = 'None'
# if val is None:#лучше использовать is, чтобы проверить, является ли что-то чем-то
#     r = []
# else:
#     r = val
# print(r)
# r= [] if val is None else val
# print(r)
#
# r = val or []
# print(r)
#-------------------------------------------
# l = []
# for i in range(100):
#     if i % 6 == 0:#проверка на кратность( остаток ноль)
#         l.append(i)
# print()
#- - - - - - - - - - - - - - - - - - - - -
# l = []
# for i in range(0,100,6):
#     l.append(i)
# print(l)
#- - - -- - - - -- - -
# l = [i for i in range(0,100,6)]
# print(l)
#- - - - -- - - -
# l = [i for i in range(100) if i % 6 == 0]
# print(l)
#-------------------------------
# l = [i if i >= 30 else i**2 for i in range(100) if i % 6 == 0]#i if i >= 30 else i**2 терналльный оператор,
# print(l)
#- -- - - - -- - - - - --
# d = {i: len(i) for i in ['dsf','asdf','sdfg']}
# print(d)#выводитключ(что в ковычках) и значение(длина того что в ковычках)
#- -- - -- - - -- - - - - - -
# l = [i * j for i in range(5) for j in range(5,11)]
# print(l)
#- -- - - - - -- - - -- - - --
# d = {(2,2): 5}
#
# l = [4,5,67]
# l[0] = 14
# print(l)
# a = (4,5,67)#это картеж ( он неизменяем)
# a[0] = 14#}
# print(a)#}   Не будет работать
#
# st = 'hi'
# st[0] = 't'#нельзя
#-- - - -- - - -- - - -- - - - -
# l = list('hi')#фнкция лист создает список(может изменяться)
# tp = tuple(l)#создает картеж(не может изменяться)
# print(l)
# print(tp)
#
# l_2 = list(tp)
# print(l_2)
#- -- - - - -- - - -- - -- - - -- - -
# l = [5,6,2,78]
# #l_2 = list(l)
# l_2 = l[:]
# l.append(5)
# print(l)
# print(l_2)

import copy

l = [[1,2],6,2,78]
#l_2 = l[:]#копирует
l_2 = copy.deepcopy(l)#глубоко копирует
l[0].append(5)
print(l)
print(l_2)