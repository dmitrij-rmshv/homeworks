# 5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название)
# и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.”
# Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер). В каждом из классов реализовать
# переопределение метода draw. Для каждого из классов методы должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.


class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'Start draw with {self.title}')


class Pen(Stationery):

    def __init__(self, title):
        super().__init__(title='Pen')

    def draw(self):
        print('writes a pen')


class Pencil(Stationery):

    def __init__(self, title):
        super().__init__(title='pencil')

    def draw(self):
        print('writes a pencil')


class Handle(Stationery):

    def __init__(self, title):
        super().__init__(title='handle')

    def draw(self):
        print('writes a handle')


pen = Pen('pen')
pencil = Pencil('pencil')
handle = Handle('handle')

print(f'object {pen.title}: ', end='')
pen.draw()

print(f'object {pencil.title}: ', end='')
pencil.draw()

print(f'object {handle.title}: ', end='')
handle.draw()
