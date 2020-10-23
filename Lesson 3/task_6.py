# 6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки, но каждое слово
# должно начинаться с заглавной буквы. Необходимо использовать написанную ранее функцию int_func().

def int_func(text):
    """
    Convert first char
    :param text: text
    :return: Title style string
    """
    letter_int = ord(text[0])
    if 96 < letter_int < 123:
        letter_int -= 32
        replace_text = text.replace(text[0], chr(letter_int), 1)
        return replace_text
    return text


print(int_func("test"))
user_string = input("Enter lower string with whitespaces:")
for item in user_string.split():
    print(int_func(item), end=' ')
