n = input('Введите число n: ')
result = int(n) + int(n + n) + int(n + n + n)
print(f'{n} + {n}{n} + {n}{n}{n} = {result}')