import itertools
import random
my_list = random.sample(range(0, 22), 7)
for i in itertools.cycle(my_list):
    print(i)