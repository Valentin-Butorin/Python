income = float(input('Введите сумму выручки: '))
expenses = float(input('Введите сумму издержек: '))

if income > expenses:
    profit = income - expenses
    profitability = int(profit / income * 100)
    print(f'Фирма отработала с прибылью {profit}')
    print(f'Рентабельность фирмы: {profitability}%')
    employees = int(input('Введите количество сотрудников: '))
    print(f'Прибыль фирмы в расчете на одного сотрудника: {profit / employees:.2f}')
else:
    print('Фирма отработала с убытком')