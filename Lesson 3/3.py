# Вариант 1
def my_func(arg1, arg2, arg3):
    temp_list = [arg1, arg2, arg3]
    temp_list.remove(min(temp_list))
    return sum(temp_list)


a = int(input())
b = int(input())
c = int(input())
print(my_func(a, b, c))


# Вариант 2
def my_func(*args):
    args_list = list(args)
    temp_list = []
    for _ in range(0, 2):
        temp_list.append(args_list.pop(args_list.index(max(args_list))))
    return sum(temp_list)


a = int(input())
b = int(input())
c = int(input())
print(my_func(a, b, c))


# Вариант 3
def my_func(*args):
    args_list = list(args)
    first_max = max(args_list)
    args_list.remove(first_max)
    second_max = max(args_list)
    return sum([first_max, second_max])


a = int(input())
b = int(input())
c = int(input())
print(my_func(a, b, c))
