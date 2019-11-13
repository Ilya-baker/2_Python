num = int(input("Введите любое целое положительное число: "))
i = 0
while num > 10:
    a = num % 10
    num //= 10
    if a > i:
        i = a
print(i)