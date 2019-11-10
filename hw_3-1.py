def user_num(user_1, user_2):
    try:
        user_div = user_1 / user_2
    except ZeroDivisionError:
        return 'You cannot divide by zero, try again.'
    except ValueError:
        return 'Enter numbers, please!'
    return user_div
print(user_num(int(input("Write your number: ")), int(input("Write your second number: "))))
# если ввести вторым числом ноль срабатывает except ZeroDivisionError:, 
# если вводить строку except ValueError: не срабатывает. В чём ошибка?  