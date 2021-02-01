class ComplexOperations:
    def __init__(self, real_part, im_part):
        self.real_part = real_part
        self.im_part = im_part

    def __str__(self):
        if self.im_part >= 0:
            return f'{self.real_part} + {self.im_part}i'
        else:
            return f'{self.real_part} - {abs(self.im_part)}i'

    def __add__(self, other):
        return ComplexOperations(self.real_part + other.real_part, self.im_part + other.im_part)

    def __sub__(self, other):
        return ComplexOperations(self.real_part - other.real_part, self.im_part - other.im_part)

    def __mul__(self, other):
        multiplication_real = self.real_part * other.real_part - self.im_part * other.im_part
        multiplication_im = self.real_part * other.im_part + other.real_part * self.im_part
        return ComplexOperations(multiplication_real, multiplication_im)

    def __truediv__(self, other):
        division_real = (self.real_part * other.real_part + self.im_part * other.im_part) / (
                other.real_part ** 2 + other.im_part ** 2)
        division_im = (other.real_part * self.im_part - self.real_part * other.im_part) / (
                other.real_part ** 2 + other.im_part ** 2)
        return ComplexOperations(division_real, division_im)


complex_1 = ComplexOperations(-1, 3)
complex_2 = ComplexOperations(1, 2)
print(complex_1)
print(complex_2)
print(complex_1 + complex_2)
print(complex_1 - complex_2)
print(complex_1 * complex_2)
print(complex_1 / complex_2)
