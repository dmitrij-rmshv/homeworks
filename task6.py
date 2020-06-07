# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
# изученных на уроках по ООП.


class EquipmentWarehouse:

    def __init__(self, **goods):
        self.goods = {}
        for el in goods.keys():
            if isinstance(goods.get(el), int):
                self.goods[el] = goods.get(el)
            else:
                print(f'Position "{el}" has invalid parameter, not taken')
        print(f'The warehouse initially contains : {self.goods}')

    def accept(self, **acc_goods):
        print(f'\nStock replenishment : {acc_goods}')
        for el in acc_goods.keys():
            if not isinstance(acc_goods.get(el), int):
                print(f'Position "{el}" has invalid parameter, changed to 0')
                acc_goods[el] = 0

        for el in acc_goods:
            if el in self.goods.keys():
                self.goods.update({el: (self.goods.get(el) + acc_goods.get(el))})
            else:
                self.goods.update({el: acc_goods.get(el)})

    def transfer(self, **trans_goods):
        print(f'\nAssigned goods for shipment: : {trans_goods}')
        for el in trans_goods.keys():
            if not isinstance(trans_goods.get(el), int):
                print(f'Position "{el}" has invalid parameter, changed to 0')
                trans_goods[el] = 0

        for el in trans_goods:
            if el in self.goods.keys():
                in_stock = self.goods.get(el)
                balance = in_stock - trans_goods.get(el)
                if balance < 0:
                    print(f'only {in_stock} of {el} available')
                    # self.goods.update({el: 0})
                    self.goods.pop(el)
                else:
                    self.goods.update({el: balance})
            else:
                print(f'{el} out of stock')


class OfficeEquipment:

    def __init__(self, price, weight, dimensions):
        self.price = price
        self.weight = weight
        self.dimensions = dimensions


class Printer(OfficeEquipment):

    def __init__(self, price, weight, dimensions, print_speed):
        super().__init__(price, weight, dimensions)
        self.print_speed = print_speed


class Scanner(OfficeEquipment):

    def __init__(self, price, weight, dimensions, cost_per_page):
        super().__init__(price, weight, dimensions)
        self.cost_per_page = cost_per_page


wh = EquipmentWarehouse(printer='4', copier=4)

wh.accept(printer=7, scanner='2')
print(f'Total in stock : {wh.goods}')

wh.transfer(copier=3, printer='3')
print(f'Total in stock : {wh.goods}')
