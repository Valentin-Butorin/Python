from functools import reduce

with open('text3.txt', encoding='utf-8') as file:
    all_lines = file.readlines()
    low_salary = []
    for line in all_lines:
        if int(line.replace('\n', '').split(' ')[1]) < 20000:
            low_salary.append(line.split(' ')[0])
    all_salaries = list(map(lambda x: x.replace('\n', '').split(' ')[1], all_lines))
    average = reduce(lambda x, y: int(x) + int(y), all_salaries) / len(all_lines)
    print('Средний оклад: ', average)
    print('Сотрудникики с окладом менее 20000:', ', '.join(low_salary))
