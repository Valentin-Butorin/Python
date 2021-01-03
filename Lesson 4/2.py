from random import randint

input_list = [randint(1, 100) for i in range(10)]
new_list = [input_list[i] for i in range(1, len(input_list)) if input_list[i] > input_list[i - 1]]
print('Исходный список: ', input_list)
print('Результат: ', new_list)
