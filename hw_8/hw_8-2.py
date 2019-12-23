class ZeroDiv(Exception):
    def __init__(self, txt):
        self.txt = txt


def division(num_1, num_2):
    try:
        num_1, num_2 = int(num_1), int(num_2)
        if num_2 == 0:
            raise ZeroDiv("Cannot be divided by zero!")
        return round(num_1 / num_2, 2)
    except ValueError:
        return "Value Error"
    except ZeroDiv as branch:
        return branch


print(division(input("Your first number: "), input("Your first second: ")))