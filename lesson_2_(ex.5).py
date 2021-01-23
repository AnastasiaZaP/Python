my_list = [9, 8, 7, 6, 6, 5, 3, 3, 2]
print(my_list)
new_el = float(input("Введите новый элемент рейтинга: "))
if my_list.count(new_el) > 0: # проверка - есть ли в списке введенный пользователем элемент
    my_list.insert(my_list.index(new_el) + my_list.count(new_el), new_el)
elif my_list[len(my_list) - 1] > new_el:
    my_list.append(new_el)
else:
    for ind in range(len(my_list)):
        if my_list[ind] < new_el:
            my_list.insert(ind, new_el)
            break
print(my_list)