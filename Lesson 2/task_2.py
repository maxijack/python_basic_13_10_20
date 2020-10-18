# 2. Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

user_key = ""
user_list = []

while user_key != 'q':
    user_value = input("Enter list value: ")
    user_list.append(user_value)
    user_key = input("Do you want continue? (print q - for end): ")

end = len(user_list) - len(user_list) % 2
user_list[:end:2], user_list[1:end:2] = user_list[1:end:2], user_list[:end:2]
print(user_list)
