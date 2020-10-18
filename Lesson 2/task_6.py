# 6. * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
# Пример готовой структуры:
# [
# (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
# (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
# (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]
# Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара,
# например название, а значение — список значений-характеристик, например список названий товаров.
# Пример:
# {
# “название”: [“компьютер”, “принтер”, “сканер”],
# “цена”: [20000, 6000, 2000],
# “количество”: [5, 2, 7],
# “ед”: [“шт.”]
# }


user_key = ""
user_products = []
index_num = 0

while user_key != 'q':
    name = input("Enter product's name: ")
    price = input("Enter product's price: ")
    amount = input("Enter number of products: ")
    unit = input("Enter unit of calculation: ")

    index_num += 1

    user_tuple = (index_num, {"name": name, "price": price, "amount": amount, "unit": unit})
    user_products.append(user_tuple)

    user_key = input("Do you want continue? (print q - for end): ")


list_values = []
for prod in user_products:
    list_values.append(prod[1].values())

analytic = list(zip(*list_values))

keys = list(user_products[0][1].keys())

final_dic = {}


for key in keys:
    final_dic.update({key: list(analytic[keys.index(key)])})

print(final_dic)
