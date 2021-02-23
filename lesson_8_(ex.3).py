class MyOwnErr(Exception):
    def __init__(self, txt):
        self.txt = txt
list = []
alphabet_float = set("-.1234567890")
while True:
    num = input("Введите число либо стоп-символ 'q' для завершения работы программы: ")
    try:
        if num == '':
            raise MyOwnErr('Вы ничего не ввели!')
        if num == 'q':
            raise MyOwnErr('Вы нажали стоп-символ.')
        for one_char in num:
            if (not one_char.isnumeric() and len(num) < 2)\
                    or (one_char == "-" and (num.index(one_char) > 0 or num.count(one_char) > 1))\
                    or (one_char == "." and num.count(one_char) > 1)\
                    or one_char not in alphabet_float:
                raise MyOwnErr('Вы ввели не число!')
    except MyOwnErr as err:
            print(err)
            print(list)
            if num == 'q':
                break
    else:
        list.append(float(num))
        print(list)
