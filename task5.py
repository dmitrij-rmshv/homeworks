# 5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу
# в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также
# других данных, можно использовать любую подходящую структуру, например словарь.


class EquipmentWarehouse:

    def __init__(self, **goods):
        self.goods = goods
        print(f'The warehouse initially contains : {self.goods}')

    def accept(self, **acc_goods):
        print(f'\nStock replenishment : {acc_goods}')
        for el in acc_goods:
            if el in self.goods.keys():
                self.goods.update({el: (self.goods.get(el) + acc_goods.get(el))})
            else:
                self.goods.update({el: acc_goods.get(el)})

    def transfer(self, **trans_goods):
        print(f'\nAssigned goods for shipment: : {trans_goods}')
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


wh = EquipmentWarehouse(printer=4, copier=4)

wh.accept(printer=7, scanner=2)
print(f'Total in stock : {wh.goods}')

wh.transfer(copier=3, printer=3)
print(f'Total in stock : {wh.goods}')

wh.transfer(printer=3, copier=3)
print(f'Total in stock : {wh.goods}')

wh.transfer(printer=3, copier=3)
print(f'Total in stock : {wh.goods}')

wh.accept(copier=7)
print(f'Total in stock : {wh.goods}')
