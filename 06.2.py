from itertools import cycle

my_list = [False, 'ABC', 123, None]
for el in cycle(my_list):
    print(el)