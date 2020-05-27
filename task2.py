# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

new_f = open("new_file.txt", encoding="utf-8")  # open file from task #1
line_num = 0
while True:
    line_words = len(new_f.readline().split())
    if line_words == 0:
        break
    else:
        line_num +=1
        print(f'line {line_num} contains {line_words} words')
new_f.close()
print(f'\nTotal lines count: {line_num}')
