"""1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""

from sys import argv


def calc_salary(hours, money_value, bonus_value):
    return hours * money_value + bonus_value


script_name, work_hours, money_per_hour, bonus = argv

try:
    work_h = float(work_hours)
    money_ph = float(money_per_hour)
    bonus_val = float(bonus)
    print("Your result is: ", calc_salary(work_h, money_ph, bonus_val))
except ValueError:
    is_result = False
    print('Input error')


