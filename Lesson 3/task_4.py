# 4. Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.

def simple_pow(value_a, value_b):
    """Simple pow function. **"""
    return value_a ** value_b


def custom_abs(value):
    """Calc abs"""
    return value if value > -value else -value


def custom_pow(base, exp):
    if exp == 1:
        return base

    while exp > 1:
        base *= base
        print(base)
        exp -= 1
    return base


while True:
    try:
        user_float = float(input('Enter float: '))
        user_int = int(input('Enter negative int: '))
    except ValueError:
        print('Input error. Try again...')
        continue

    print(f"Simple pow result: {simple_pow(user_float, user_int)}")
    if user_int >= 0:
        custom_pow_result = custom_pow(user_float, user_int)
    else:
        abs_user_value = custom_abs(user_int)
        custom_pow_result = 1 / custom_pow(user_float, abs_user_value)

    print(f"Custom pow result: {custom_pow_result}")
    break
