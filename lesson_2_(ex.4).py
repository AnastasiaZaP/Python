words = input("Чем вы увлекаетесь? Перечислите через пробел: ")
words_split = words.split()
print(words_split)
for ind, el in enumerate(words_split, 1):
    print(ind, el[0:10])