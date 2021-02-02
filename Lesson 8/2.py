class ZeroDiv(Exception):
    def __init__(self, txt):
        self.txt = txt


try:
    a = int(input('Введите делимое: '))
    b = int(input('Введите делитель: '))
    if b == 0:
        raise ZeroDiv('Деление а ноль')
except ZeroDiv as err:
    print(err)
else:
    print('Результат:', a / b)
