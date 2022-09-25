from datetime import date
d1_year =int(input('enter year of first date :'))
d1_month =int(input('enter month of first date :'))
d1_day =int(input('enter day of first date :'))
d1 = date(d1_year,d1_month,d1_day)

print('---------------------------------')

d2_year =int(input('enter year of second date :'))
d2_month =int(input('enter month of second date :'))
d2_day =int(input('enter day of second date :'))
d2 = date(d2_year,d2_month,d2_day)

delta = d2 - d1
print(delta.days,'days')
