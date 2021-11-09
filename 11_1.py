class Date():

    def __init__(self, date):
        day, month, year = Date.from_string(date)
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        return f'{self.day:02}-{self.month:02}-{self.year:04}'

    @classmethod
    def from_string(cls, date_as_string):
        day, month, year = map(int, date_as_string.split('-'))
        return day, month, year

    @staticmethod
    def is_date_valid(date_as_string):
        day, month, year = Date.from_string(date_as_string)
        return day <= 31 and month <= 12 and year <= 3999

date1 = Date('01-08-2016')
print(date1)
s='21-10-2021'
if Date.is_date_valid(s):
    date2 = Date(s)
    print(date2)
s2='21-15-2021'
if not Date.is_date_valid(s2):
    print(f'Дата не верна {s2}')
day1, month1, year1 = Date.from_string('01-09-2016')
print(f'{day1}-{month1}-{year1}')

