"""7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название,
форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:

[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджеры контекста.
"""
import json

txt_lines = []
with open("task_7_file.txt", "r", encoding="UTF-8") as file:
    file_str = file.read()
    txt_lines = file_str.split("\n")

dic_companies = {}
for line in txt_lines:
    company_inf = {}
    data = line.split(" ")
    if len(data) == 4:
        try:
            company_inf["type"] = data[1]
            company_inf["proceeds"] = int(data[2])
            company_inf["costs"] = int(data[3])
            company_inf["profit"] = int(data[2]) - int(data[3])
            dic_companies.setdefault(data[0], company_inf)
        except ValueError:
            print("ValueError")

profit_sum = 0
good_comp_counter = 0
# Calculate average profit
for com_name, com_params in dic_companies.items():
    if com_params.get("profit") > 0:
        profit_sum += com_params.get("profit")
        good_comp_counter += 1

average_profit = {"average_profit": 0}
if profit_sum > 0:
    average_profit["average_profit"] = profit_sum / good_comp_counter

inner_dic = {}
for com_name, com_params in dic_companies.items():
    inner_dic[com_name] = com_params.get("profit")

# Create result list
result_list = [inner_dic, average_profit]

# Save to JSON
with open("task_7_file_out.json", "w", encoding="UTF-8") as file:
    json.dump(result_list, file)