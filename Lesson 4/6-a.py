from itertools import count

start_int = 3
stop_int = 10

for el in count(start_int):
    if el > stop_int:
        break
    print(el, end=' ')
