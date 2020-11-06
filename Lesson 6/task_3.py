"""3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker. В классе Position
реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения
атрибутов, вызвать методы экземпляров)."""


class Worker:
    _income = {"wage": float(0), "bonus": float(0)}

    def __init__(self, name, surname, position, wage: float, bonus: float):
        self.name = name
        self.surname = surname
        self.position = position
        self._income["wage"] = wage
        self._income["bonus"] = bonus


class Position(Worker):
    def __init__(self, name, surname, position, wage: float, bonus: float):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return self.name + " " + self.surname

    def get_total_income(self):
        return self._income.get("wage") + self._income.get("bonus")


accountant = Position("Evgeniy", "Egorov", "accountant", 15000, 2500)
print(accountant.get_full_name())
print(accountant.get_total_income())

manager = Position("Ivan", "Ivanov", "manager", 105000, 200500)
print(manager.get_full_name())
print(manager.get_total_income())