print('Задача 1')
Fruits = ["яблоко", "банан", "киви", "арбуз"]
last_name = len(Fruits)
for i in range(last_name):
    print(str(i + 1) + '.' + '{}'.format(Fruits[i]))

print('Задача 2')
a = {'a', 'b', 'c', 'd', 'e', 'f', 'g'}
b = {'a', 'b', 'c'}
c = a - b
print(list(c))

print('Задача 3')
the_first = [1, 2, 3, 4, 5, 9, 8, 7, 6]
new = []
last = len(the_first)
for i in range(last):
    if the_first[i] % 2 == 0:
        new.append(the_first[i] / 4)
    else:
        new.append(the_first[i] * 2)
print(new)