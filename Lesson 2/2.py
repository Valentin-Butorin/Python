str_input = input('Введите все элементы списка через пробел: ')
final_list = str_input.split(' ')
for i in range(0, len(final_list) - 1, 2):
    final_list[i], final_list[i + 1] = final_list[i + 1], final_list[i]
print(final_list)
