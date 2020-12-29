def div_func(dividend, divider):
    if divider != 0:
        return dividend / divider
    else:
        return 'Cannot divide by 0!'


try:
    a, b = float(input()), float(input())
    print(div_func(a, b))
except ValueError as err:
    print(err)
