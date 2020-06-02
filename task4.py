# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name,
# is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,
# остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
# должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.


class Car:

    auto_count = 0

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        Car.auto_count += 1
        self.count = Car.auto_count
        print(f'#{self.count} {self.color} {self.name} car with a speed of {self.speed}\n')

    def go(self):
        print(f'{self.name} car #{self.count} went\n')

    def stop(self):
        print(f'{self.name} car #{self.count} stopped\n')

    def turn_left(self):
        print(f'{self.name} car #{self.count} turned left\n')

    def turn_right(self):
        print(f'{self.name} car #{self.count} turned right\n')

    def show_speed(self):
        print(f'{self.name} car #{self.count} speed {self.speed} mph\n')


class TownCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            print(f"{self.name} car #{self.count} speed exceeded\n")
        else:
            print(f'{self.name} car #{self.count} speed {self.speed} mph\n')


class SportCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            print(f"{self.name} car #{self.count} speed exceeded\n")
        else:
            print(f'{self.name} car #{self.count} speed {self.speed} mph\n')


class PoliceCar(Car):

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, is_police=True)


jc = Car(20, 'lizard green', 'Antilopa-GNU', False)
tc = TownCar(55, 'grey', 'Logan', False)
sc = SportCar(222, 'red', 'Lamborghini', False)
wc = WorkCar(40, 'white', 'GAZel', False)
pc = PoliceCar(111, 'blue', 'Solaris')

tc.go()
jc.stop()
wc.show_speed()
sc.turn_left()
pc.turn_right()

tc.speed = 66
tc.show_speed()

wc.speed = 44
wc.show_speed()
