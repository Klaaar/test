import pprint



goods = [
    {
        'name':'Windows 10',
        'brand':'Microsoft',
        'price':'1000'
    },
    {
        'name':'Windows 11',
        'brand':'Microsoft',
        'price':'1100'
    },
    {
        'name':'Iphone 14',
        'brand':'Apple',
        'price':'900'
    }
]

def on_price(item):#item это каждый из этих словарей
    return item['price']#Обращаемся по ключу

print(sorted(goods, key=on_price,reverse=True))

print(sorted(goods, key=lambda item: item['price'], reverse=True))


def function(item):
    return item['brand']

# filtered_lst = filter(function = 'Microsoft', goods) #строчка норм, просто пайчарм ругается
# print(list(filtered_lst))

nymbers = ['1','2','3','4','5']
new_lst = map(int,nymbers)
print(list(new_lst))

names_list = ['Ирма','Иван', 'Егор', 'Ксения', 'Дмитрий']
surnames_list = ['Макарова', 'Голубкин','Бобин', 'X', 'Леонтьев']

result = list(map(lambda name, surname: f'{name} {surname}', names_list,surnames_list))
print(result)

indexed_goods = []

for index, item in enumerate(goods):
    indexed_goods.append({index:item})
pprint.pprint(indexed_goods)

names_list = ['Ирма','Иван', 'Егор']
surnames_list = ['Макарова', 'Голубкин','Бобин']

for name,surname in zip(names_list,surnames_list):
    print(name,surname)

print(__name__)#название модуля где исполняется данный скрипт