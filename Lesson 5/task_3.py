"""3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов. Определить,
кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""
import my_function


def mid_salary(dic):
    sum_salary = 0
    for key, value in dic.items():
        sum_salary += value
    return sum_salary / len(dic)


try:
    with open("task_3_file.txt", "r", encoding="UTF-8") as file:
        data = file.readlines()
        dic_data = my_function.convert_to_dic(data, ":")
        print(f"Меньше 20к у:{[key for key, value in dic_data.items() if value < 20000]}")
        print(f"Средняя величина дохода: {mid_salary(dic_data)}")
except IOError:
    print("File read error")
