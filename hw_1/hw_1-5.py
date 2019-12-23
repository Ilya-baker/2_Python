income = int(input("Выручка: "))
loss = int(input("Расход: "))
profit = income - loss
print("Чистая прибыль:", profit, "руб.")
print("Соотношение рентабельность выручки составит", float("%.2f" % (profit / income * 100)),"%.")
if profit > 0:
    people = int(input("Введите количество сотрудников: "))
    print("Прибль на одного сотрудника составит:", "%.1f" % (profit / people), "руб.")
