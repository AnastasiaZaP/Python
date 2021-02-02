from translate import Translator
with open("text_4.txt", "r", encoding="utf-8") as my:
    a = my.readlines()

# перевод с помощью translate (бесплатная версия действует ограниченное кол-во раз в сутки :(()
out_f = open("translator.txt", "w", encoding="utf-8")
for el in a:
    b = el.split()
    translator = Translator(to_lang="Russian")
    b[0] = translator.translate(b[0])
    с = " ".join(b)
    out_f.write(f"{с}\n")
out_f.close()

# перевод с помощью цикла (если лимит translate закончился)
# out_f = open("translator.txt", "w", encoding="utf-8")
# for el in a:
#     print(a)
#     b = el.split()
#     if b[0] == 'One':
#         b[0] = 'Один'
#     elif b[0] == 'Two':
#         b[0] = 'Два'
#     elif b[0] == 'Three':
#         b[0] = 'Три'
#     elif b[0] == 'Four':
#         b[0] = 'Четыре'
#     с = " ".join(b)
#     out_f.write(f"{с}\n")
# out_f.close()




