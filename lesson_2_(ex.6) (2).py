my_list = []
sp_name = []
sp_price = []
sp_quantity = []
sp_number = []
while(True):
    menu = int(input("1 - добавить товар, 2 - показать структуру, 3 - выполнить аналитику, 4 - выйти: "))
    if menu == 1:
        name = input("Ведите назавание товара:")
        price = float(input("Введите стоимость товара:"))
        quantity = int(input("Введите количество товара:"))
        number = input("Введите единицы количества товара:")
        slovar = {"название": name, "цена": price, "количество": quantity, "eд": number}
        my_list.append(((len(my_list) + 1), slovar))
        sp_name.append(name)
        sp_price.append(price)
        sp_quantity.append(quantity)
        sp_number.append(number)
    elif menu == 2:
        print(my_list)
    elif menu == 3:
        analit = {"название": list(set(sp_name)), "цена": list(set(sp_price)), "количество": list(set(sp_quantity)), "eд": list(set(sp_number))}
        print(analit)
    elif menu == 4:
        print("Программа завершила работу")
        break