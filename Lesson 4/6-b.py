from itertools import cycle

my_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
stop_int = 10
i = 0
for el in cycle(my_list):
    i += 1
    if i > stop_int:
        break
    print(el)
