"""4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""
import my_function

rus_dic = {
    1: 'Один',
    2: 'Два',
    3: 'Три',
    4: 'Четыре',
}

data = []

try:
    with open("task_4_file.txt", "r", encoding="UTF-8") as file:
        data = file.readlines()
except IOError:
    print("File read error")

rus_data = {}

dic_data = my_function.convert_to_dic(data, "—")
for key, value in dic_data.items():
    rus_data.setdefault(rus_dic.get(value), value)

try:
    with open("task_4_file_out.txt", "w", encoding="UTF-8") as file:
        for key, value in rus_data.items():
            file.write(f"{key} — {value}\n")
except IOError:
    print("File read error")