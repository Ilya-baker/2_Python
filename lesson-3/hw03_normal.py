print("Задача 1")
def fibonacci(n, m):
    fib = []
    a, b = 0, 1
    for num in range(m):
        fib.append(b)
        a, b = b, a+b
    n -= 1
    res = [fib[i] for i in range(n, m)]
    del fib
    print(res)
    return res
fibonacci(4, 12)

print("=" * 50)

print("Задача 2")
def sort_to_max(origin_list):
    def min_num(i):
        min_elem = float('inf')
        for elem in i:
            if elem < min_elem:
                min_elem = elem
        return min_elem
    draft = [x for x in origin_list]
    sorting = []
    while len(draft):
        for elem in draft:
            if elem == min_num(draft):
                sorting.append(elem)
                draft.remove(elem)
    print('Список: \n%s \nПреобразование по возростанию:\n%s' % (origin_list, sorting))
    del draft
    return sorting
sort_to_max([7, 6.8, 34, 0, -7.1, 19.9, 3.7, -11, 5, 17])

print("=" * 50)

print("Задача 3")
def alt_filter(func, itr):
    new_itr = [elem for elem in itr if func(elem)]
    if type(itr) is tuple:
        new_itr = tuple(new_itr)
    if type(itr) is set:
        new_itr = set(new_itr)
    if type(itr) is str:
        new_itr = ''.join(new_itr)
    print(new_itr)
    return new_itr
alt_filter(lambda x: x < 10, {7, 6.8, 34, 0, -7.1, 19.9, 3.7, -11, 5, 17})

print("=" * 50)

# Задача 4 - запутался, очень сложно с геометрией.