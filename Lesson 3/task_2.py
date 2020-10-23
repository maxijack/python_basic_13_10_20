# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def user_print(name, surname, birthday, city, email, phone):
    """
    Print in one string
    """
    print(f"Name {name} surname {surname} birthday {birthday} city {city} email {email} phone {phone}")


user_name = input("Name: ")
user_surname = input("Surname: ")
user_birthday = input("birthday")
user_city = input("City")
user_email = input("Email")
user_phone = input("Phone")

user_print(user_name, user_surname, user_birthday, user_city, user_email, user_phone)
