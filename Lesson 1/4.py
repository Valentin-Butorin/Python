max_num = 0

num = int(input('Введите целое положительное число: '))

if num % 10 == num:
    print(num)
else:
    while num > 0:
        if num % 10 >= max_num:
            max_num = num % 10
            num = (num - num % 10) // 10
        else:
            num //= 10
    print(max_num)