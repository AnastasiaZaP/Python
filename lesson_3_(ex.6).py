def int_func(inp_str):
    out_str = ''
    en_alphabet_small = set("""abcdefghijklmnopqrstuvwxyz'`""")
    word_list = inp_str.split(" ")
    for one_word in word_list:
        priznak_not_in_alphabet = False
        for one_char in one_word:
            if one_char not in en_alphabet_small:
                priznak_not_in_alphabet = True
                break
        if not priznak_not_in_alphabet:
            if out_str == '':
                out_str = one_word
            else:
                out_str += " " + one_word
    return out_str.title()

# строка проверки: nice авп ъghj hjjпаро вапрghgh cool
str = input("Введите слова из маленьких латинских букв, разделенных пробелом: ")
print(int_func(str))