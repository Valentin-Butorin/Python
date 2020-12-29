# Вариант 1
def my_func(num, power):
    return num ** power


def check_num():
    try:
        x = float(input('Введите действительное положительное число x: '))
        if x <= 0:
            print('Ошибка! Вы ввели неположительное число!')
            x = check_num()
    except ValueError:
        print('Ошибка! Введенные данные не являются числом!')
        x = check_num()
    return x


def check_power():
    try:
        y = int(input('Введите целое отрицательное число y: '))
        if y >= 0:
            print('Ошибка! Вы ввели неотрицательное число!')
            y = check_power()
    except ValueError:
        print('Ошибка! Введенные данные не являются целым числом!')
        y = check_power()
    return y


print(my_func(check_num(), check_power()))


# Вариант 2
def my_func(num, power):
    exp_result = num
    for i in range(0, abs(power) - 1):
        exp_result *= num
    div_result = 1 / exp_result
    return div_result


def check_num():
    try:
        x = float(input('Введите действительное положительное число x: '))
        if x <= 0:
            print('Ошибка! Вы ввели неположительное число!')
            x = check_num()
    except ValueError:
        print('Ошибка! Введенные данные не являются числом!')
        x = check_num()
    return x


def check_power():
    try:
        y = int(input('Введите целое отрицательное число y: '))
        if y >= 0:
            print('Ошибка! Вы ввели неотрицательное число!')
            y = check_power()
    except ValueError:
        print('Ошибка! Введенные данные не являются целым числом!')
        y = check_power()
    return y


print(my_func(check_num(), check_power()))
