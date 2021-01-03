from random import randint

my_list = [randint(1, 10) for i in range(10)]
result_list = [elem for elem in my_list if my_list.count(elem) == 1]

print('Исходный список: ', my_list)
print('Результат: ', result_list)
