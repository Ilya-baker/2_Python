class Stationery:
    def __init__(self, title="all my troubles seemed so far away"):
        self.title = title

    def draw(self):
        print(f"Yesterday, {self.title}")


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f"Now it looks {self.title} here to stay")


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f"Oh, {self.title} in yesterday")


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f"Oh, I believe {self.title} day..")


stationery_ = Stationery()
stationery_.draw()
pen_ = Pen("as though they're")
pen_.draw()
pencil_ = Pencil("I believe")
pencil_.draw()
handle_ = Handle("in tomorrow")
handle_.draw()