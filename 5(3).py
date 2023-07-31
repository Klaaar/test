# import time
# class Running():
#     def __init__(self):
#         self.start = None
#
#     def __enter__(self):
#         self.start = time.time()
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         t = time.time() - self.start
#         print(f'Время работы кода: {t} сек.')
#
#         if exc_type is TypeError:
#             return True
#
# with Running() as t1:
#     my_list = [x for x in range(1,100000000)]
#     my_list -= 's'
#``````````````````````````````````````````````````````````````
# lst = [1,2,3,4,5]
# list_iterator = iter(lst)-возвращает объект итератора
#next - возвращает след. объект последовательности этого итератора
# print(next(list_iterator))
# print(next(list_iterator))
# print(next(list_iterator))
# print(next(list_iterator))
# print(next(list_iterator))
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#то же самое, что и выше(опустошаем итератор)
# for i in list_iterator:
#     print(i)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import random
#итератор случайных чисел

class RandomIter():
    def __init__(self, limit):
        self.limit = limit
        self.__reload = limit

    def __iter__(self):
        self.limit = self.__reload
        return self

    def __next__(self):
        if self.limit == 0:
            raise StopIteration

        self.limit -= 1
        return random.randint(0,100)

rand_iter = RandomIter(10)
print(iter(rand_iter))

for rand_int in rand_iter:
    print(rand_int)
