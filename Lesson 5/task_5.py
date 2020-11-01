"""5. Создать (программно) текстовый файл, записать в него программно набор чисел,
разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
import my_function

# write
with open("task_5_file.txt", "w") as file:
    for row_number in my_function.custom_range(0, 10):
        for column_number in my_function.custom_range(0, 10):
            file.write(f"{column_number} ")
        file.write("\n")

# read
with open("task_5_file.txt", "r") as file:
    rows = file.readlines()
    sum = 0
    for row in rows:
        numbers = row.split(" ")
        for number in numbers:
            if number.isdigit():
                sum += int(number)
    print(f"Result: {sum}")