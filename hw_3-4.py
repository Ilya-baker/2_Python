def user_num(x, y):
    try:
        x, y = float(x), float(y)
    except ValueError:
        return 'Enter only numbers, please!'
    power = x ** y
    return "%.4f" % power
print(user_num(input("Enter number: "), input("Enter second number: ")))