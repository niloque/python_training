day = 29
month = 2
year = 2010

MONTH_LEN = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

if month != 2:
    max_day = MONTH_LEN[month-1]
elif year % 4 == 0 and (year % 100) != 0 or year % 400 == 0:
    max_day = 29
else:
    max_day = 28

if day < max_day:
    new_day, new_month, new_year = day + 1, month, year
elif month == 12:
    new_day = 1
    new_month = 1
    new_year = year + 1
else:
    new_day, new_month, new_year = 1, month + 1, year

print('Następna data:', new_day, new_month, new_year)