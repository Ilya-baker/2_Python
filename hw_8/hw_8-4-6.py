# задание не обошлось без помощи наставника
class Warehouse:
    def __init__(self):
        self.total_qty = 0
        self.unit = {}
        self.questions_template = (
            {'Name': 'Product name: '},
            {'Cost': 'Cost of product: '},
            {'Quantity': 'Quantity product: '}
        )

    @staticmethod
    def is_int(number: str):
        try:
            int(number)
            return True
        except ValueError:
            return False

    def reception(self):
        user_input = input('To start filling in the goods, enter "1", to finish - "enter": ')
        user_list = []
        while user_input == '1':
            user_dict = {}
            for quest in self.questions_template:
                key = tuple(quest)[0]
                tmp = input(quest[key])
                if key == 'Cost':
                    if self.is_int(tmp):
                        tmp = int(tmp)
                    else:
                        print('Invalid data type!')
                        return
                elif key == 'Quantity':
                    if self.is_int(tmp):
                        tmp = int(tmp)
                        self.total_qty += tmp
                    else:
                        print('Invalid data type!')
                        return
                user_dict.update({key: tmp})
            user_list.append(user_dict)
            user_input = input('Subdivision name: ')
            self.unit.update({user_input: user_list})
            user_input = input('To continue filling - enter "1", to finish - "enter": ')


class OfficeEquipment:
    def __init__(self, name: str, price: int):
        self.name = name
        self.price = price


class Printer(OfficeEquipment):
    def __init__(self, name: str, price: int, speed: int, print_quality: str):
        self.speed = speed
        self.print_quality = print_quality
        super().__init__(name, price)


class Scanner(OfficeEquipment):
    def __init__(self, name: str, price: int, document: str, photo: str, picture: str):
        self.document = document
        self.photo = photo
        self.picture = picture
        super().__init__(name, price)


class Xerox(OfficeEquipment):
    def __init__(self, name: str, price: int, color: int, black_white: str):
        self.color = color
        self.black_white = black_white
        super().__init__(name, price)

warehouse = Warehouse()
warehouse.reception()
print(warehouse.unit)
print(warehouse.total_qty)