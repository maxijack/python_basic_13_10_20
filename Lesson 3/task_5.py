# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел,
# разделенных пробелом и снова нажать Enter. Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел
# к полученной ранее сумме и после этого завершить программу.

def is_end_symbol(arg_string, end_symbol):
    for letter in arg_string:
        if letter == end_symbol:
            return True
    return False


def conv_to_int_list(arg_string):
    str_list = arg_string.split()
    int_list = []
    for item in str_list:
        try:
            int_list.append(int(item))
        except ValueError:
            print("convertValue error")
    return int_list


def list_sum(arg_list):
    sum_result = 0
    for item in arg_list:
        sum_result += item
    return sum_result


user_sum = 0

while True:
    user_string = input("Input number string with whitespaces (q - for end): ")
    print(is_end_symbol(user_string, "q"))
    if is_end_symbol(user_string, "q"):
        if len(user_string) > 1:
            user_string.replace("q", "")
            user_int_list = conv_to_int_list(user_string)
            user_sum += list_sum(user_int_list)
            print(user_sum)
        else:
            print(user_sum)
        break

    user_int_list = conv_to_int_list(user_string)
    user_sum += list_sum(user_int_list)
    print(user_sum)
