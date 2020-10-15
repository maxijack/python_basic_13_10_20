"""
5. Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает
фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки). Выведите соответствующее сообщение.
Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

revenue - выручка
cost - издержки
profit - прибыль
loss - убыток
profitability - рентабильность
"""

is_company_profit = False


revenue = float(input("What is the company's revenue?:"))
cost = float(input("What is the company's cost?:"))

if revenue > cost:
    print("Congratulations! Your company is profitable")
    is_company_profit = True
else:
    print("Sorry! Your company is unprofitable")

if is_company_profit:
    print("Profitability: {:.2f}".format(revenue / cost))
    workers_count = int(input("Enter workers count:"))
    print("Firm profit per employee: {:.2f}".format(revenue / workers_count))
