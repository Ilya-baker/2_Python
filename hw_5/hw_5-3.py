with open("hw_5-3.txt", "r") as my_file:
    s_sum = []
    less = []
    line = my_file.read().split("\n")
    for i in line:
        i = i.split()
        if int(i[1]) < 20000:
            less.append(i[0])
        s_sum.append(i[1])
print(f"Sallary less 20.000 {less}. Average salary - {sum(map(int, s_sum)) / len(s_sum)}")
