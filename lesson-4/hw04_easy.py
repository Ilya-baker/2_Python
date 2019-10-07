print("Задача 1")

digits = [4, 26, -11, -8, 3, 42]
print('Исходный список: ', digits)
list_1 = [num ** 2 for num in digits]
print('Новый список: ', list_1)
print("==============================")

print("Задача 2")

a = ['apricot', 'quince', 'orange', 'watermelon', 'banana', 'grapes']
b = ['quince', 'grapefruit', 'pear', 'orange', 'melon', 'figs', 'watermelon']
c= [num for num in a if num in b]
print('a = {} \nb = {} \nc = {}'.format(a,b,c))
print("==============================")

print("Задача 3")

list_2 = list(num for num in digits if (num % 3 == 0 and num > 0 and num % 4 != 0))
print(list_2)