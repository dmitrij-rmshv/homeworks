# 3. Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка. В его конструкторе
# инициализировать параметр, соответствующий количеству клеток (целое число). В классе должны быть реализованы методы
# перегрузки арифметических операторов: сложение (__add__()), вычитание (__sub__()), умножение (__mul__()),
# деление (__truediv__()).Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение,
# умножение и обычное (не целочисленное) деление клеток, соответственно. В методе деления должно осуществляться
# округление значения до целого числа.
# Сложение. Объединение двух клеток. При эт. число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток
# Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток
# больше нуля, иначе выводить соответствующее сообщение.
# Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение количества ячеек
# этих двух клеток.
# Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества
# ячеек этих двух клеток.
# В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
# Данный метод позволяет организовать ячейки по рядам.
# Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу
# Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
# Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод make_order() вернет
# строку: *****\n*****\n**.
# Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод make_order() вернет
# строку: *****\n*****\n*****.


class Cell:

    def __init__(self, num_cells):
        self.num_sells = num_cells

    def __add__(self, other):
        return Cell(self.num_sells + other.num_sells)

    def __sub__(self, other):
        """
        Логику здесь реализовал в соответствии с буквой задания, как я её понял.
        Но она отличается от того, что вы озвучили.
        Разницу клеток представил в абсолютном виде.
        """
        diff = self.num_sells - other.num_sells
        return Cell(abs(diff)) if diff != 0 else Cell('Operation impossible: cells are equal')

    def __mul__(self, other):
        return Cell(self.num_sells * other.num_sells)

    def __truediv__(self, other):
        """
        А здесь вроде получилось удовлетворить и задание и вас.
        """
        div = round(self.num_sells / other.num_sells)
        return Cell(div) if div > 0 else Cell('Operation impossible: dividing the smaller by the larger')

    def make_order(self, row_sells):
        i, f = divmod(self.num_sells, row_sells)
        return ('*' * row_sells + '\n') * i + '*' * f


my_cell_1 = Cell(57)
my_cell_2 = Cell(21)
my_cell_3 = Cell(57)

print(f'Created cells are : {my_cell_1.num_sells}; {my_cell_2.num_sells}; {my_cell_3.num_sells}.')

print((my_cell_1 + my_cell_2).num_sells)
print((my_cell_1 - my_cell_2).num_sells)
print((my_cell_1 - my_cell_3).num_sells)
print((my_cell_1 * my_cell_2).num_sells)
print((my_cell_1 / my_cell_2).num_sells)
print((my_cell_2 / my_cell_3).num_sells)

print(my_cell_1.make_order(9))
print(my_cell_2.make_order(7))
