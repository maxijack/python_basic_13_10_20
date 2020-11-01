"""2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

try:
    with open("task_2_file.txt", "r") as file:
        lines = file.readlines()
        for index, string in enumerate(lines):
            print(f"{index}: {len(string)}")
except IOError:
    print("IO File Error")
