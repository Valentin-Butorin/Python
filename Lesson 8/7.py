class Complex:
    def __init__(self, re, im):
        self.re = re
        self.im = im

    def __str__(self):
        if self.im < 0:
            return f'({self.re}{self.im}j)'
        return f'({self.re}+{self.im}j)'

    def __add__(self, other):
        return Complex(self.re + other.re, self.im + other.im)

    def __mul__(self, other):
        a = self.re * other.re + self.im * other.im
        return Complex(self.re * other.re - self.im * other.im, self.re * other.im + self.im * other.re)


complex_1 = Complex(1, 3)
complex_2 = Complex(-3, 4)
complex_3 = Complex(5, -9)
print(complex_1)
print(complex_2)
print(complex_3)
print(complex_1 + complex_2 + complex_3)
print(complex_1 * complex_2 * complex_3)
