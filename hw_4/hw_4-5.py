from functools import reduce
first_num = [el for el in range(100, 1001, 2)]
second_num = reduce(lambda x, y: x * y, first_num)
print(second_num)