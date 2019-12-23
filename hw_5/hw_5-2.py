with open("hw_5-2.txt") as pillar:
    line = pillar.readlines()
    for i, d in enumerate(line):
        _number = len(d.split())
        print("Строка {} содержит {} слов".format(i + 1, _number))