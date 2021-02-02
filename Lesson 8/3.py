class IsNotInt(Exception):
    def __init__(self, input_data):
        self.input_data = input_data

    def __str__(self):
        return 'Количество элементов списка, которые не являются числом: ' + str(self.check_int(self.input_data))

    @staticmethod
    def check_int(input_data):
        not_int = 0
        for el in input_data:
            if el.isdigit():
                continue
            not_int += 1
        return not_int


try:
    data = input('Введите числа через пробел: ').split()
    if IsNotInt.check_int(data) > 0:
        raise IsNotInt(data)
except IsNotInt as err:
    print(err)
else:
    print(data)
