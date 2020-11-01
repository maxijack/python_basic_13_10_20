"""6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие
лекционных, практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета
не обязательно были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий
по нему. Вывести словарь на экран.
Примеры строк файла:

Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —
Пример словаря:

{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""
import my_function


def find_name(row: str):
    """Parse name"""
    return row[0:row.find(":")]


def find_class_hours(row: str):
    """Parse classes' hours"""
    ret_dic = {}
    content = row[row.find(":") + 1:].split(" ")
    for el in content:
        if len(el) > 0 and el[0].isdigit():
            val = el.split("(")
            int_value = int(val[0])
            name_value = ""
            if len(val) > 1:
                end_pos = val[1].find(")")
                name_value = val[1][:end_pos]
            ret_dic.setdefault(name_value, int_value)
    return ret_dic


rows = []
with open("task_6_file.txt", "r", encoding="UTF-8") as file:
    rows = file.readlines()
    classes = {}
    for row in rows:
        name = find_name(row)
        hour_dic = find_class_hours(row)
        res = my_function.custom_reduce(lambda x, y: x + y, hour_dic.values())
        classes.setdefault(name, res)
    print(classes)
