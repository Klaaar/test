goods = {
    "Лампа": "12345",
    "Стол":"23456",
    "Диван":"34567",
    "Стул":"45678"
}
store = {
    "12345": [{"quantity": 27, "price": 42}],
    "23456": [{"quantity": 22, "price": 510},
              {"quantity": 32, "price": 520}],
    "34567": [{"quantity": 2, "price": 1200},
              {"quantity": 1, "price": 1150}],
    "45678": [{"quantity": 50, "price":100},
              {"quantity": 12, "price": 95},
              {"quantity": 43, "price": 97}],
}

for it in goods:
    it_name = it
    it_id = goods[it]
    it_qty = 0
    it_price = 0
    for i in store[it_id]:
        item_qty = i['quantity']
        item_price = i['price'] * item_qty
        print(it_name, "- кол-во", item_qty, "шт. Стоимость", item_price, "руб.")














