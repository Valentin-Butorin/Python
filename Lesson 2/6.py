goods_list = []
goods_tuple = ()
goods_dict = {'название': '', 'цена': '', 'количество': '', 'ед': ''}
analytics_dict = {'название': [], 'цена': [], 'количество': [], 'ед': []}
index = 1
print('Для того, чтобы прекратить ввод, введите 0')
while True:
    goods_dict['название'] = input('Введите название (для отмены введите 0): ')
    if goods_dict['название'] == '0':
        break
    # Циклы с исключениями здесь для того, чтобы пользователю не приходилось
    # вводить заново большой объем данных в случае ошибки.
    while True:
        try:
            goods_dict['цена'] = int(input('Введите цену (для отмены введите 0): '))
        except ValueError:
            print('Ошибка! Необходимо ввести число!')
            continue
        break
    if goods_dict['цена'] == 0:
        break
    while True:
        try:
            goods_dict['количество'] = int(input('Введите количество (для отмены введите 0): '))
        except ValueError:
            print('Ошибка! Необходимо ввести число!')
            continue
        break
    if goods_dict['количество'] == 0:
        break
    goods_dict['ед'] = input('Введите единицу измерения (для отмены введите 0): ')
    if goods_dict['ед'] == '0':
        break
    goods_tuple = index, goods_dict.copy()
    goods_list.append(goods_tuple)
    index += 1
if not goods_list:
    print('Вы ничего не ввели')
else:
    for elem in goods_list:
        for key in elem[1]:
            if elem[1][key] in analytics_dict[key]:
                continue
            else:
                analytics_dict[key].append(elem[1][key])
    print(analytics_dict)
