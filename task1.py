# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

print('\n   """ Program to create a text file """   \nWrite the lines of the creating file through "Enter".\n       '
      'To complete - another "Enter".')
new_f = open("new_file.txt", "w", encoding="utf-8")
while True:
    next_line = input('-> ')
    if next_line == "":
        break
    else:
        new_f.write(next_line + '\n')
new_f.close()
