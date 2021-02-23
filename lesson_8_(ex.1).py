class Date:
    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def from_string(cls, date_as_string):
        day, month, year = map(int, date_as_string.split('-'))
        date1 = cls(day, month, year)
        print(cls, date_as_string)
        return date1

    @staticmethod
    def is_date_valid(date_as_string):
        day, month, year = map(int, date_as_string.split('-'))
        # фильтры: месяцы 31 и 30 дней, февраль 28 дней, високосные года (февраль 29 дней), диапазон 1990 - 2021 гг
        if ((1 <= day <= 31 and (month == 1 or month == 3 or month == 5 or month == 7
                                 or month == 8 or month == 10 or month == 12)and (1990 <= year <= 2021))
            or ((1 <= day <= 28 and month == 2) and (1990 <= year <= 2021)) \
                or (1 <= day <= 30 and (month == 4 or month == 6 or month == 9 or month == 11)
                    and (1990 <= year <= 2021)) \
                or (1 <= day <= 29 and month == 2 and (year == 1992 or year == 1996
                                                       or year == 2000 or year == 2004
                                                       or year == 2008 or year == 2012
                                                       or year == 2016 or year == 2020)) \
                or (1 <= day <= 28 and month == 2 and (year == 1990 or year == 1991 or year == 1993
                                                       or year == 1994 or year == 1995 or year == 1997
                                                       or year == 1999 or year == 2001 or year == 2002
                                                       or year == 2003 or year == 2005 or year == 2006
                                                       or year == 2007 or year == 2009 or year == 2010
                                                       or year == 2011 or year == 2013 or year == 2014
                                                       or year == 2015 or year == 2017 or year == 2018
                                                       or year == 2019 or year == 2021))):
            print('Дата введена верно')
        else:
            print('Ошибка ввода данных')

d = '21-02-2021'
date2 = Date.from_string(d)
is_date = Date.is_date_valid(d)
d2 = '44-02-2021'
date2 = Date.from_string(d2)
is_date = Date.is_date_valid(d2)
d3 = '21-13-2021'
date2 = Date.from_string(d3)
is_date = Date.is_date_valid(d3)
d4 = '29-02-2021'
date2 = Date.from_string(d4)
is_date = Date.is_date_valid(d4)
d5 = '28-02-2021'
date2 = Date.from_string(d5)
is_date = Date.is_date_valid(d5)
d6 = '29-02-1992'
date2 = Date.from_string(d6)
is_date = Date.is_date_valid(d6)
d7 = '29-02-1993'
date2 = Date.from_string(d7)
is_date = Date.is_date_valid(d7)
d7 = '01-01-1000'
date2 = Date.from_string(d7)
is_date = Date.is_date_valid(d7)
d8 = '04-01-1000'
date2 = Date.from_string(d8)
is_date = Date.is_date_valid(d8)

