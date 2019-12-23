from sys import argv

def formula():
    try:
        hours, rate, bonus = map(float, argv[1:])
        print(f"Monthly payment: {hours * rate + bonus} rub.")
    except ValueError:
        print("Enter all 3 numbers.")
formula()