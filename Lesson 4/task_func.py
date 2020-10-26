"""Module with custom functions
"""


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
