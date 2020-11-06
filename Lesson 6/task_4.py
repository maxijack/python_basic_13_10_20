"""4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
которые должны сообщать, что машина поехала, остановилась, повернула (куда). Опишите несколько дочерних классов:
TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат."""


class Car:
    _is_go = False

    def __init__(self, speed=10, color="White", name="Ford", is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        self._direction = ""

    def __str__(self):
        return f"Car name:{self.name} speed:{self.speed} color:{self.color} " \
               f"is_police: {self.is_police} is_go: {self._is_go}"

    def go(self):
        self._is_go = True
        print("Машина поехала")

    def stop(self):
        self._is_go = False
        print("Машина остановилась")

    def turn(self, direction):
        if self._is_go:
            self._direction = direction
        else:
            print("Машина еще стоит")

    def show_speed(self):
        print(f"Скорость: {self.speed}")


class TownCar(Car):
    def __init__(self, speed=20, color="Blue", name="Lada", is_police=False):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            print("Превышение скорости")
        else:
            super().show_speed()


class WorkCar(Car):
    def __init__(self, speed=30, color="Green", name="Mazda", is_police=False):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            print("Превышение скорости")
        else:
            super().show_speed()


class SportCar(Car):
    def __init__(self, speed=100, color="Red", name="Ferrari", is_police=False):
        super().__init__(speed, color, name, is_police)


class PoliceCar(Car):
    def __init__(self, speed=120, color="Red", name="Ford", is_police=True):
        super().__init__(speed, color, name, is_police)


town_car = TownCar(50)
work_car = WorkCar(100)
sport_car = SportCar()
police = PoliceCar()

print(town_car)
town_car.show_speed()
town_car.go()
print(town_car)
town_car.stop()
print(town_car)
print(work_car)
work_car.show_speed()
print(sport_car)
sport_car.show_speed()
print(police)
police.show_speed()