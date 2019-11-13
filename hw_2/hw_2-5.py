rating = [8, 1, 3, 6, 2]
while True:
    user = input("Введите любое число, для выхода из цикла введите 111: ")
    user_2 = int(user)
    if user_2 == 111:
        print("Выход")
        break
    rating.append(user_2)
    order = sorted(rating, reverse = True)
    print(order)
