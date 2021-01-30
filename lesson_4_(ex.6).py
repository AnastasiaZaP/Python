# а
from itertools import count
from itertools import islice

for el in islice(count(3),8):
    print(el)

# б
from itertools import cycle
my_list = ["ложки", "вилки", "тарелки", "стаканы"]
for el in islice(cycle(my_list), 2 * len(my_list) + 1):
    print(el)