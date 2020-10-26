"""5. Реализовать формирование списка, используя функцию range() и возможности генератора.
В список должны войти четные числа от 100 до 1000 (включая границы).
Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce().
"""
from task_func import (
    custom_range,
    custom_reduce
)


def my_func(prev_el, el):
    return prev_el * el


even_list = [el for el in custom_range(100, 1001) if not el % 2]
print(even_list)
print(custom_reduce(my_func, even_list))
