# 1. Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

var_auto_tuple = ("val_test", 23.3)
var_int: int = 20
var_float: float = 2.2
var_string: str = "string"
var_bool: bool = True
var_list: list = ["test_string", 35, 3.4]
var_tuple: tuple = ("value_1", 1)
var_dict: dict = {"name": "Maria", "age": 99}

my_list = [var_auto_tuple, var_int, var_float, var_string, var_bool, var_list, var_tuple, var_dict]
for list_item in my_list:
    print(f"List item type: {type(list_item)}")
