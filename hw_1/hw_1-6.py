a = float(input("Введите количество км. пройденных спортсменом в первый день: "))
b = float(input("Введите желаемый результат: "))
i = 0
c = float()
while c < b:
    c = a + a * 0.1
    i += 1
    if c == b:
        print("Понадобится", int(i), "дней.")
        break
    elif c > b:
        print("Понадобится", int(i + 1), "дней.")
        break
