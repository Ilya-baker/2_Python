import json
import codecs

with codecs.open("hw_5-7.json", "w", encoding='utf-8') as j_file:
    with open("hw_5-7.txt", encoding='utf-8') as a:
        i = 0
        b = 0
        c = {}
        sub = {}
        for pillar in a:
            line = pillar.split()
            profit = int(line[2]) - int(line[3])
            sub[line[0]] = profit
            if profit >= 0:
                b += 1
                i += profit
            c["average_profit"] = int(i/b)
        all_s = [sub, c]
        json.dump(all_s, j_file, ensure_ascii=False, indent=4)
print(f"Company accounting:\n{line}\n\nTotal:\n{all_s}")


