def my_func(inp_str):
    str_list = inp_str.split(' ')
    num_list = []
    for word in str_list:
        if word.isnumeric():
            num_list.append(int(word))
    return sum(num_list)


sum_all = 0
while True:
    a = input("Введите числа, разделенные пробелами: ")
    q_in_a = a.find("q")
    if q_in_a == -1:
        sum_all += my_func(a)
        print(f"{my_func(a)}({sum_all})")
    else:
        a = a[:q_in_a]
        sum_all += my_func(a)
        print(sum_all)
        break
