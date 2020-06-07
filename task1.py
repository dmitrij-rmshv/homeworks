# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-мес-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и
# преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца
# и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.


class Date:

    def __init__(self, date_str):
        try:
            self.day, self.month, self.year = Date.extract(date_str)
            print(f'day of the month: {self.day}; month: {self.month}, year: {self.year}')
        except TypeError:
            print('Date invalid')

    @classmethod
    def extract(cls, date_str):
        day, month, year = map(int, date_str.split('-'))
        if Date.is_valid(day, month, year):
            return day, month, year

    @staticmethod
    def is_valid(day, month, year):
        if day < 1 or day > 31 or month < 1 or month > 12 or year < 1 or year > 2222:
            return False
        else:
            return True


my_date = Date('22-13-1995')
