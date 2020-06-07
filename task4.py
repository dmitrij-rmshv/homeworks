# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
# который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
# уникальные для каждого типа оргтехники.


class EquipmentWarehouse:
    pass


class OfficeEquipment:

    def __init__(self, price, weight, dimensions):
        self.price = price
        self.weight = weight
        self.dimensions = dimensions


class Printer(OfficeEquipment)

    def __init__(self, price, weight, dimensions, print_speed):
        super().__init__(price, weight, dimensions)
        self.print_speed = print_speed


class Scanner(OfficeEquipment)

    def __init__(self, price, weight, dimensions, cost_per_page):
        super().__init__(price, weight, dimensions)
        self.cost_per_page = cost_per_page

