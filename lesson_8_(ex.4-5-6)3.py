from pprint import pprint


class MyOwnErr(Exception):
    def __init__(self, txt):
        self.txt = txt


class Store:
    def __init__(self):
        self.dict = {}

    def to_store(self, goods):
        return self.dict.setdefault(goods.__class__.__name__, []).append(goods.__dict__)

    def extract(self, good_name, dept_name):
        flag = False
        for key in self.dict.keys():
            if key == good_name:
                del self.dict[key]
                print(f'Товар {good_name} отправлен в отдел {dept_name}')
                break
            for i in range(len(self.dict[key]) - 1, -1, -1):
                if self.dict[key][i]['name'] == good_name:
                    extract_class = key
                    del self.dict[key][i]
                    flag = True
        if flag:
            print(f'Товар {good_name} класса {extract_class} отправлен в отдел {dept_name}')
        else:
            print('Запрашиваемый товар не найден на складе')
        self.dict = {k: v for k, v in self.dict.items() if not len(v) < 1}


class Equipment:
    def __init__(self, name, price, quantity, date_of_man, term):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.date_of_man = date_of_man
        self.term = term


class Printers(Equipment):
    def __init__(self, name, price, quantity, date_of_man, term, ink): # ink - чернила
        super().__init__(name, price, quantity, date_of_man, term)
        self.ink = ink


class Scanners(Equipment):
    def __init__(self, name, price, quantity, date_of_man, term, res): # res - разрешение
        super().__init__(name, price, quantity, date_of_man,term)
        self.res = res


class Xeroxes(Equipment):
    def __init__(self, name, price, quantity, date_of_man, term, form): # form - формат бумаги
        super().__init__(name, price, quantity, date_of_man, term)
        self.form = form


s = Store()
while True:
    try:
        main_menu = input("1 - добавить товар на склад\n"
                          "2 - отправить товар со склада в подразделение компании\n"
                          "3 - показать товары на складе\n"
                          "4 - выйти\n→ ")
        if not main_menu.isnumeric():
            raise MyOwnErr('Введите 1, 2, 3 или 4')
        else:
            if int(main_menu) < 1 or int(main_menu) > 4:
                raise MyOwnErr('Введите 1, 2, 3 или 4')
    except MyOwnErr as err:
        print(err)
    else:
        main_menu = int(main_menu)
        if main_menu == 1:
            while True:
                try:
                    menu_add = input("1 - добавить принтеры\n"
                                     "2 - добавить сканеры\n"
                                     "3 - добавить ксероксы\n"
                                     "4 - вернуться в основное меню\n → ")
                    if not menu_add.isnumeric():
                        raise MyOwnErr('Введите 1, 2, 3 или 4')
                    else:
                        if int(menu_add) < 1 or int(menu_add) > 4:
                            raise MyOwnErr('Введите 1, 2, 3 или 4')
                except MyOwnErr as err:
                    print(err)
                else:
                    menu_add = int(menu_add)
                    if menu_add == 1 or menu_add == 2 or menu_add == 3:
                        while True:
                            name = input(f'Введите название модели: ')
                            try:
                                if name == '':
                                    raise MyOwnErr('Вы ничего не ввели!')
                            except MyOwnErr as err:
                                print(err)
                            else:
                                break
                        alphabet_price = set(".1234567890")
                        while True:
                            price = input(f'Введите цену: ')
                            try:
                                if price == '':
                                    raise MyOwnErr('Вы ничего не ввели!')
                                for one_char in price:
                                    if (not one_char.isnumeric() and len(price) < 2) \
                                            or (one_char == "." and price.count(one_char) > 1) \
                                            or one_char not in alphabet_price:
                                        raise MyOwnErr('Цена должна задаваться неотрицательным числом')
                            except MyOwnErr as err:
                                print(err)
                            else:
                                price = float(price)
                                break
                        while True:
                            quantity = input(f'Введите количество: ')
                            try:
                                if quantity == '':
                                    raise MyOwnErr('Вы ничего не ввели!')
                                if not quantity.isnumeric():
                                    raise MyOwnErr('Количество должно задаваться целым числом')
                                if int(quantity) == 0:
                                    raise MyOwnErr('Количество должно быть положительным')
                            except MyOwnErr as err:
                                print(err)
                            else:
                                quantity = int(quantity)
                                break
                        while True:
                            date_of_man = input(f'Введите год прозводства: ')
                            try:
                                if date_of_man == '':
                                    raise MyOwnErr('Вы ничего не ввели!')
                                if not len(date_of_man) == 4:
                                    raise MyOwnErr('Год вводится в четырёхзначном формате')
                                if not date_of_man.isnumeric():
                                    raise MyOwnErr('Год должен задаваться целым числом')
                                if int(date_of_man) < 1990:
                                    raise MyOwnErr('Год производства не может быть меньше 1990 года')
                            except MyOwnErr as err:
                                print(err)
                            else:
                                date_of_man = int(date_of_man)
                                break
                        while True:
                            term = input(f'Введите срок службы (кол-во лет): ')
                            try:
                                if term == '':
                                    raise MyOwnErr('Вы ничего не ввели!')
                                if not term.isnumeric():
                                    raise MyOwnErr('Срок службы должен задаваться целым числом')
                                if int(term) == 0:
                                    raise MyOwnErr('Срок службы должен быть положительным')
                            except MyOwnErr as err:
                                print(err)
                            else:
                                term = int(term)
                                break
                        if menu_add == 1:
                            while True:
                                try:
                                    menu_ink = input("Чернила: 1 - чёрные, 2 - цветные\n")
                                    if not menu_ink.isnumeric():
                                        raise MyOwnErr('Введите 1 или 2')
                                    else:
                                        if int(menu_ink) != 1 and int(menu_ink) != 2:
                                            raise MyOwnErr('Введите 1 или 2')
                                except MyOwnErr as err:
                                    print(err)
                                else:
                                    menu_ink = int(menu_ink)
                                    if menu_ink == 1:
                                        ink = 'ЧБ'
                                    elif menu_ink == 2:
                                        ink = 'RGB'
                                    break
                            new_printer = Printers(name, price, quantity, date_of_man, term, ink)
                            s.to_store(new_printer)
                        elif menu_add == 2:
                            while True:
                                try:
                                    menu_res = input("Разрешение: 1 - 6400x9600, 2 - 600x1200\n")
                                    if not menu_res.isnumeric():
                                        raise MyOwnErr('Введите 1 или 2')
                                    else:
                                        if int(menu_res) != 1 and int(menu_res) != 2:
                                            raise MyOwnErr('Введите 1 или 2')
                                except MyOwnErr as err:
                                    print(err)
                                else:
                                    menu_res = int(menu_res)
                                    if menu_res == 1:
                                        res = '6400x9600'
                                    elif menu_res == 2:
                                        res = '600x1200'
                                    break
                            new_scanner = Scanners(name, price, quantity, date_of_man, term, res)
                            s.to_store(new_scanner)
                        elif menu_add == 3:
                            while True:
                                try:
                                    menu_form = input("Формат бумаги: 1 - A3, 2 - A4\n")
                                    if not menu_form.isnumeric():
                                        raise MyOwnErr('Введите 1 или 2')
                                    else:
                                        if int(menu_form) != 1 and int(menu_form) != 2:
                                            raise MyOwnErr('Введите 1 или 2')
                                except MyOwnErr as err:
                                    print(err)
                                else:
                                    menu_form = int(menu_form)
                                    if menu_form == 1:
                                        form = 'A3'
                                    elif menu_form == 2:
                                        form = 'A4'
                                    break
                            new_xerox = Xeroxes(name, price, quantity, date_of_man, term, form)
                            s.to_store(new_xerox)
                    elif menu_add == 4:
                        break
        elif main_menu == 2:
            if s.dict != {}:
                while True:
                    print('Введите пункт назаначения:')
                    try:
                        menu_destination = input("1 - бухгалтерия\n"
                                                 "2 - руководство\n"
                                                 "3 - цех\n")
                        if not menu_destination.isnumeric():
                            raise MyOwnErr('Введите 1, 2 или 3')
                        else:
                            if int(menu_destination) < 1 and int(menu_destination) > 3:
                                raise MyOwnErr('Введите 1, 2 или 3')
                    except MyOwnErr as err:
                        print(err)
                    else:
                        menu_destination = int(menu_destination)
                        if menu_destination == 1:
                            dept_name = 'Бухгалтерия'
                        elif menu_destination == 2:
                            dept_name = 'Руководство'
                        elif menu_destination == 3:
                            dept_name = 'Цех'
                        break
                while True:
                    name = input('Введите товар для отправки: ')
                    try:
                        flag = False
                        for key in s.dict.keys():
                            if key == name:
                                flag = True
                            for i in range(len(s.dict[key])):
                                if s.dict[key][i]['name'] == name:
                                    flag = True
                        if not flag:
                            raise MyOwnErr('На складе нет указанного товара для отправки')
                    except MyOwnErr as err:
                        print(err)
                    else:
                        good_name = name
                        break
                s.extract(good_name, dept_name)
            else:
                print('Склад пуст, невозможно отправить товар')
        elif main_menu == 3:
            if s.dict == {}:
                print('Склад пуст')
            else:
                pprint(s.dict, width=20)
        elif main_menu == 4:
            break
