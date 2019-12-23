class Date():

    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def string_date(cls, turning):
        day, month, year = map(int, turning.split('-'))
        num = cls(day, month, year)
        return num

    @staticmethod
    def valid_date():
        if (0 < date.day <= 31) and (0 < date.month <= 12) and (0 < date.year <= 4444):
            branch  = f"{date.day} {date.month} {date.year}"
        else:
            branch  = "Date entered is not correct!"
        return branch

date = Date.string_date('20-11-2011')
print(Date.valid_date())
