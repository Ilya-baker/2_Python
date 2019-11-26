pillar = {}
with open("hw_5-6.txt") as hw5_6:
    for draft in hw5_6:
        line = draft.split()
        discipline = line[0]
        time = line[1:]
        pillar[discipline] = 0
        for types in time:
            try:
                pillar[discipline] += int(types[:types.find("(")])
            except ValueError:
                pass
print(pillar)