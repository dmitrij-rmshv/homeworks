# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
# вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту
# ситуацию и не завершиться с ошибкой.


class DelenieNaNullError(Exception):

    def __init__(self, txt):
        self.txt = txt


inp_divisible = input("Введите делимое: ")
inp_divisor = input("Введите делитель: ")

try:
    divisible = int(inp_divisible)
    divisor = int(inp_divisor)
    if divisor == 0:
        raise DelenieNaNullError("Вы ввели недопустимый делитель - ноль!")
except ValueError:
    print("Вы ввели не число")
except DelenieNaNullError as err:
    print(err)
else:
    print(f"Все хорошо. Ваше число: {divisible / divisor:.2f}")
