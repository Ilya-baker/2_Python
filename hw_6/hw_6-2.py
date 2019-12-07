class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width
    def get(self):
        return f"{self._length} m * {self._width} m * 25 kg * 5 cm = {int((self._length * self._width * 25 * 5) / 1000)} t"
road_1 = Road(5000, 20)
print(road_1.get())
