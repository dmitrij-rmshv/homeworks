# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
# income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
# например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
# проверить значения атрибутов, вызвать методы экземпляров).

class Worker:

    def __init__(self, name, family, post, salary, prize):
        self.name = name
        self.surname = family
        self.position = post
        self._income = {"wage": salary, "bonus": prize}


class Position(Worker):

    def __init__(self, name, family, post, salary, prize):
        super().__init__(name, family, post, salary, prize)

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._income.get("wage") + self._income.get("bonus")


pos = Position('Vasia', 'Pupkin', 'developer', 25000, 5000)
posi = Position('Condoleezza', 'Rice', 'Secretary of State', 32000, 6000)

print(pos.name, pos.surname, pos.position, pos._income)
print(f'{pos.get_full_name()} is a {pos.position} with an income of {pos.get_total_income()}')

print(posi.name, posi.surname, posi.position, posi._income)
print(f'{posi.get_full_name()} is a {posi.position} with an income of {posi.get_total_income()}')
