# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

# ver 2 - googletrans

from googletrans import Translator
translator = Translator()

with open('text_4.txt', encoding='utf-8') as in_file:
    content = in_file.readlines()
new_content = []
for line in range(len(content)):
    line_words = content[line].split()
    line_words[0] = translator.translate(line_words[0], src='en', dest='ru').text
    new_content.append(' '.join(line_words) + '\n')
with open('text_4rus.txt', 'w', encoding='utf-8') as out_file:
    out_file.writelines(new_content)
