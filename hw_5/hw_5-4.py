my_dic = {"One" : "Один", "Two" : "Два", "Three" : "Три", "Four" : "Четыре"}
with open("hw_5-4.txt") as first_file:
    with open("hw_5-4_draft.txt", "a") as finite_file:
        line = first_file.read().split("\n")
        for i in line:
            i = i.split(" - ")
            finite_file.writelines(my_dic[i[0]] + ' - ' + i[1] + "\n")