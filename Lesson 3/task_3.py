# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_sort(values):
    """Bubble sort"""
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(values) - 1):
            if values[i] > values[i + 1]:
                values[i], values[i + 1] = values[i + 1], values[i]
                swapped = True


def my_func(arg_1, arg_2, arg_3):
    """
    Find max values
    :return: two max values
    """
    user_list = [arg_1, arg_2, arg_3]
    my_sort(user_list)
    return user_list[-2:]


while True:
    try:
        value_1 = int(input('Enter first value: '))
        value_2 = int(input('Enter second value: '))
        value_3 = int(input('Enter third value: '))
    except ValueError:
        print('Enter three values')
        continue
    result = my_func(value_1, value_2, value_3)
    print(f"Max values {result}")
    break
