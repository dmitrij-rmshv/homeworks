# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

total_salary = 0
pov_line = 20000
poor_bodies = ""
with open("text_3.txt", encoding="utf-8") as payroll:
    pay_list = payroll.readlines()
for lines in pay_list:
    salary = float(lines.split()[1])
    total_salary += salary
    if salary < pov_line:
        poor_bodies = poor_bodies + " " + lines.split()[0]
print(f'Employees:{poor_bodies} have a salary below {pov_line}\nAverage salary = {total_salary / len(pay_list)}')
