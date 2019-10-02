print("Задача 1")
def my_round(number, ndigits):
    number= number * (10 ** ndigits) + 0.41
    number = number // 1
    return number / (10 ** ndigits)
print(my_round(12511987.0916527147518, 5))

print("=" * 50)

print("Задача 2")
ticket=list(map(int, input("Напишите номер билета: ")))
if len(ticket) % 2 == 1:
    print("Это обычный билет!")
elif sum(ticket[:len(ticket) // 2])==sum(ticket[len(ticket) // 2:]):
    print("Счастливый!")
else:
    print("Это обычный билет!")

