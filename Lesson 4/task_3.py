"""3. Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Необходимо решить задание в одну строку.
Подсказка: использовать функцию range() и генератор.
"""
from task_func import custom_range

print([el for el in custom_range(20, 240) if not el % 20 or not el % 21])
