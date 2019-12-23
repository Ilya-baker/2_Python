num_list = []

class Patch(Exception):
    def __init__(self, txt):
        self.txt = txt

while True:
    user = input('Write any number. Or "Enter" to display the result: ')
    if user == "":
        break
    try :
        if float(user):
            num_list.append(float(user))
    except ValueError:
        print( "Try again" )
    except Patch as err:
        print(err)

print(num_list)