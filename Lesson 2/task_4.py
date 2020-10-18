# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки.
# Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.

user_string_list = input("Enter your string: ").split(' ')
for index, user_string in enumerate(user_string_list):
    print(f"{index} {user_string if len(user_string) <= 10 else user_string[:10]}")
