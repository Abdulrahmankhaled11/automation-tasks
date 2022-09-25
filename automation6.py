from datetime import datetime

def Get_birthday():
    year = int(input('enter your born year :'))
    month =int(input('enter your born month :'))
    day= int(input('enter your born day :'))
    birthday = datetime(year,month,day)
    return birthday

def calculate_dates(birthday):
    now = datetime.now()
    birthday = datetime(now.year, birthday.month, birthday.day)
    return (birthday - now.today()).days + 1

birday = Get_birthday()
calc = calculate_dates(birday)

print(calc,'days')