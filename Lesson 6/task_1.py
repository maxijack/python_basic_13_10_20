"""1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный.
В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
третьего (зеленый) — на ваше усмотрение.
Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов,
и при его нарушении выводить соответствующее сообщение и завершать скрипт.
"""
import time


class TrafficLight:
    __colors_lib = [('red', 7), ('yellow', 2), ('green', 3)]
    __color = 'red'

    def __find_color_pos(self, color):
        pos = 0
        for color_tuple in self.__colors_lib:
            if color_tuple[0] == color:
                return pos
            else:
                pos += 1
        return None

    def __init__(self, color):
        if self.__find_color_pos(color) is not None:
            self.__color = color
        else:
            raise AttributeError("Color not found ")

    def running(self):
        pos = self.__find_color_pos(self.__color)
        while pos < len(self.__colors_lib):
            print(self.__colors_lib[pos][0])
            time.sleep(self.__colors_lib[pos][1])
            pos += 1


trafficLight = TrafficLight('red')
trafficLight.running()
