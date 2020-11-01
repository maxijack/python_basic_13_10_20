"""1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""

user_data = []

while True:
    user_str = input("Enter your text (Empty string for exit): ")
    if len(user_str) == 0:
        break
    user_data.append(user_str)

try:
    with open("out_file.txt", "w") as file:
        for user_str in user_data:
            file.write(user_str + "\n")
except IOError:
    print("IOError")
