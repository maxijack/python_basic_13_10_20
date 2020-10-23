# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def div_calc(user_val_1, user_val_2):
    """
    Divide two numbers
    :param user_val_1: first value
    :param user_val_2: second value
    :return: result
    """
    try:
        return user_val_1 / user_val_2
    except ZeroDivisionError:
        print('Div zero error')


while True:
    try:
        value_1 = int(input('Enter first value: '))
        value_2 = int(input('Enter second value: '))
    except ValueError:
        print('Enter int number')
        continue
    result = div_calc(value_1, value_2)
    if result is not None:
        print(f'Your result {result}')
        break

