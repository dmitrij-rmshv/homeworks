# 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.

# Пример строки файла: firm_1 ООО 10000 5000.

# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).

# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].

# Итоговый список сохранить в виде json-объекта в соответствующий файл.

# Пример json-объекта:
#
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджеры контекста.

import json

firm_profit_dict = dict()
aver_profit = dict()
total_profit, profit_cnt = 0, 0
with open('text_7.txt', encoding='utf-8') as in_txt:
    content = in_txt.readlines()
for line in content:
    firm_data = line.split()
    firm_name = firm_data[0]
    firm_profit = int(firm_data[2]) - int(firm_data[3])
    if firm_profit > 0:
        total_profit += firm_profit
        profit_cnt += 1
    firm_profit_dict.update({firm_name: firm_profit})
aver_profit.update({"average_profit": total_profit / profit_cnt})
out_list = [firm_profit_dict, aver_profit]
# print(out_list)
with open("text7.json", "w", encoding='utf-8') as write_f:
    json.dump(out_list, write_f, indent=4, ensure_ascii=False)
