from random import randint
sum_el = 0
with open("hw_5-5.txt", "w") as my_file:
    for i in range(10):
        el = randint(0, 100)
        sum_el += el
        my_file.write(str(el) + " ")
print(f"Сумма: {sum_el}")
