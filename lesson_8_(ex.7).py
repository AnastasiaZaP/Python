class Nums:
    def __init__(self, num):
        self.num = num

    def __str__(self):
        return f"{self.num}"

    def __add__(self, other):
        return Nums(self.num + other.num)

    def __sub__(self, other):
        return Nums(self.num - other.num)

    def __mul__(self, other):
        return Nums(self.num * other.num)

# "Хитрый" способ (рука не поднимается удалить)
a = Nums(2+5j)
b = Nums(3+8j)
print('"Хитрый" способ сложения и умножения комплексных чисел')
print(f'(2+5j) + (3+8j) = {a + b}')
print(f'(2+5j) * (3+8j) = {a * b}')

# Способ "как надо было сделать"
c = Nums(2)
d = Nums(3)
e = Nums(5)
f = Nums(8)
print('Способ сложения и умножения комплексных чисел "как надо было сделать"')
print(f'(2+5j) + (3+8j) = {c + d}+{e + f}j')
print(f'(2+5j) * (3+8j) = {c * d - e * f}+{e * d + c * f}j')




