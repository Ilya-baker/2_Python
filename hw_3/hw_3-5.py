def sum_fum():
    sum_1 = 0
    while True:
        sum_2 = 0
        user = input("Введите число через пробелы: ").split()
        try:
            for n, i in enumerate(user):
                sum_2 += int(user[n])
            print(sum_2)
            sum_1 += sum_2
            answer = input("[1]Continue \n[2]Result \n[3]Exit\n")
            if answer == '1':
                continue
            elif answer == '2':
                print(f"The all sum: {sum_1}.")
            elif answer == '3':
                break
        except ValueError:
            return f"Enter only numbers, the all sum - {sum_1}"
    return f"The all sum: {sum_1}."

print(sum_fum())



