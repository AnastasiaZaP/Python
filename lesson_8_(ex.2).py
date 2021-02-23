class MyOwnErr(Exception):
    def __init__(self, txt):
        self.txt = txt

div1 = input('Введите делимое: ')
div2 = input('Введите делитель: ')

try:
    div1 = int(div1)
    div2 = int(div2)
    if div2 == 0:
        raise MyOwnErr('На ноль делить нельзя!')
except ValueError:
    print('Вы ввели не число!')
except MyOwnErr as err:
    print(err)
else:
    print(int(div1) / int(div2))
