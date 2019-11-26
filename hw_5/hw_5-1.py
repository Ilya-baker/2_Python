while True:
    pillar = input('Write something, press "Enter" to exit: ').split()
    if not pillar:
        break
    with open("hw_5-1.txt", "a") as my_file:
        for i in range(len(pillar)):
            print(pillar[i], file = my_file)
