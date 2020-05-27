# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

from random import randint, randrange


def num_gen():
    nums = []
    for num in range(randint(10, 20)):
        nums.append(str(randrange(-99, 99)))
    return ' '.join(nums)


print('\n""" Program for calculating the sum of numbers """\n')

with open('text_numbers.txt', 'w') as file:
    file.write(num_gen())

with open('text_numbers.txt', 'r') as file:
    numbers = map(float, file.readline().split())

print(f'The sum of numbers in file is {sum(numbers)}')
