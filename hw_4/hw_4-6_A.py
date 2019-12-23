import itertools
def infinity():
    try:
        user_num = int(input("Your number: "))
        for i in itertools.count(user_num, 1):
            print(i)
    except ValueError:
        print("Enter number, try again")
        return infinity()
infinity()




