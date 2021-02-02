def sum_digit(stroka):
    index = 0
    while index < len(stroka):
        if stroka[index].isdigit() or stroka[index] == " ":
            index += 1
        else:
            stroka = stroka.replace(stroka[index], ' ')
    stroka_split = stroka.split()
    for index in range(len(stroka_split)):
        stroka_split[index] = int(stroka_split[index])
    return sum(stroka_split)


with open("text_6.txt", "r", encoding="utf-8") as my:
    inp_list = my.readlines()
    print(inp_list)
    list_to_dict = dict((inp_list[i].split(":")[0], sum_digit(inp_list[i].split(":")[1])) for i in range(len(inp_list)))
    print(list_to_dict)