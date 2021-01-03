from functools import reduce

start_int = 100
stop_int = 1000

even_numbers_in_range = [n for n in range(start_int, stop_int + 1, 2)]
multiplication = reduce(lambda prev_el, el: prev_el * el, even_numbers_in_range)

print(f'Произведение всех четных чисел от {start_int} до {stop_int}: {multiplication}')
