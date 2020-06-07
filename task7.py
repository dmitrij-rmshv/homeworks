# 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку
# методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные числа)
# и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.


class ComplexNumber:
    cnt = 0

    def __init__(self, real, image):
        self.real = real
        self.image = image
        ComplexNumber.cnt += 1
        self.image_sign = '-' if self.image < 0 else '+'
        print(f'complex number #{ComplexNumber.cnt}:  {self.real}{self.image_sign}{abs(self.image)}i')

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.image + other.image)

    def __mul__(self, other):
        return ComplexNumber(self.real * other.real - self.image * other.image,
                             self.real * other.image + other.real * self.image)


cn_1 = ComplexNumber(3, 1)
cn_2 = ComplexNumber(2, -3)
print('Sum: ', end='')
cn_1 + cn_2
print('Mul: ', end='')
cn_1 * cn_2
print()
n_1 = complex(3, 1)
print(n_1)
n_2 = complex(2, -3)
print(n_2)
print(n_1 + n_2)
print(n_1 * n_2)
