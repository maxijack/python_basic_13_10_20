# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

user_month_id = int(input("Enter month id (1-12): "))

months_dic = {
    "winter": (12, 1, 2),
    "spring": (3, 4, 5),
    "summer": (6, 7, 8),
    "autumn": (9, 10, 11)
}

isFound = False

for key, value in months_dic.items():
    if user_month_id in value:
        print(f"Your month is {key}")
        isFound = True
        break

if not isFound:
    print("Your month not found")
