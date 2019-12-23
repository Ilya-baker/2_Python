class Car:
    _speed = ()
    _color = ()
    _name = ()
    _is_police = False

    def __init__(self, name, color):
        self.name = name
        self.color = color
        print(f'Model: {self.name} ({self.color}) {type(self)} color')

    def go(self):
        print(f'{self.name}: The car went.')

    def stop(self):
        print(f'{self.name}: The car stopped.')

    def turn(self, direction):
        print(f'{self.name}: Turned {"left" if direction == 0 else "right"}.')

    def show_speed(self, speed):
        print(f'{self.name}: Car speed: {speed}.')


class TownCar(Car):

    def show_speed(self, speed):
        if speed > 60:
            print(f'{self.name}: Car speed: {speed}. Over speed!')
        else:
            super().show_speed(speed)

class SportCar(Car):
    pass

class WorkCar(Car):

    def show_speed(self, speed):
        if speed > 40:
            print(f'{self.name}: Car speed: {speed}. Over speed!')
        else:
            super().show_speed(speed)

class PoliceCar(Car):

    def __init__(self, name, color):
        super().__init__(name, color)
        self.is_police = True

town_car = TownCar('"Town car"', 'green')
town_car.go()
town_car.show_speed(40)
town_car.turn(1)
town_car.turn(0)
town_car.show_speed(80)
town_car.stop()
print()

sport_car = SportCar('"Spohts car"', 'red')
sport_car.go()
sport_car.turn(0)
sport_car.turn(1)
sport_car.show_speed(100)
sport_car.stop()
print()

work_car = WorkCar('"Truck"', 'blue')
work_car.go()
work_car.turn(1)
work_car.turn(0)
work_car.show_speed(30)
work_car.show_speed(50)
work_car.stop()
print()

police_car = PoliceCar('"Police car"', 'white')
police_car.go()
police_car.show_speed(90)
police_car.turn(0)
police_car.stop()
print()

print(f'{town_car.name} - {town_car.color} color.')
print(f'{sport_car.name} - {sport_car.color} color.')
print(f'{work_car.name} - {work_car.color} color.')
print(f'{police_car.name} - {police_car.color} color.')




