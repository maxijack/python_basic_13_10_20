"""Custom functions for HW
"""


def convert_to_dic(data_arg, delimiter):
    """
    Convert file data to dic. Split by custom delimiter
    :param data_arg: data container
    :param delimiter: delemiter symbol
    :return: dictionary
    """
    ret_dic = {}
    for item in data_arg:
        item = item.replace("\n", "")
        item = item.split(delimiter)
        salary = int(item[1])
        ret_dic.setdefault(item[0], salary)

    return ret_dic


def custom_range(start, stop):
    """Generate list from start to stop
    :rtype: list
    :param start: int value start range
    :param stop: int value end of range
    :return: List with range
    """
    if not isinstance(start, int) or not isinstance(stop, int):
        raise TypeError('Expect int')
    ret_list = []
    while start <= stop:
        ret_list.append(start)
        start += 1

    return ret_list


def custom_reduce(func, iterable):
    """Use func for previous and current element and return its result
    :param func: custom function
    :param iterable: iterable object
    :return: value
    """
    it = iter(iterable)
    value = next(it)
    for element in it:
        value = func(value, element)
    return value


def custom_count(start=0, step=1):
    """Make an iterator that returns evenly spaced values starting with number start
    """
    n = start
    while True:
        yield n
        n += step


def custom_cycle(iterable):
    """Make an iterator returning elements from the iterable and saving a copy of each.
    When the iterable is exhausted, return elements from the saved copy. Repeats indefinitely
    """
    saved = []
    for element in iterable:
        yield element
        saved.append(element)
    while saved:
        for element in saved:
              yield element
