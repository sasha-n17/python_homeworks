from datetime import datetime


class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def conversion_to_number(cls, date_as_string):
        day, month, year = map(int, date_as_string.split('-'))
        full_date = cls(day, month, year)
        return full_date

    @staticmethod
    def is_date_valid(date_as_string):
        day, month, year = map(int, date_as_string.split('-'))
        return 1 <= day <= 31 and 1 <= month <= 12 and year <= 5999

    def existing_date(self):
        correct_date = True
        try:
            datetime(self.year, self.month, self.day)
        except ValueError:
            correct_date = False
        return correct_date


print(Date.is_date_valid('30-02-2021'))
date_test = Date.conversion_to_number('30-02-2021')
print(date_test.month)
print(date_test.existing_date())
