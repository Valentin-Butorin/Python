def my_sum():
    my_sum_result = 0

    def line_sum():
        nonlocal my_sum_result
        for elem in line_input():
            if elem == 'q':
                return my_sum_result
            else:
                my_sum_result += int(elem)
        print(my_sum_result)
        return line_sum()
    return line_sum()


def line_input():
    try:
        line = input('Введите числа через пробел (чтобы закончить, введите q): ')
        if '  ' in line:
            print('Ошибка! Введены лишние пробелы. Повторите попытку.')
            return line_input()
        line_list = line.removesuffix(' ').removeprefix(' ').split(' ')
    except ValueError:
        print('Ошибка! Введены лишние пробелы. Повторите попытку.')
        return line_input()
    return line_list


print(my_sum())
