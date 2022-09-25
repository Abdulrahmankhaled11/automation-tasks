from datetime import datetime



def Get_birthday():
    year = int(input('enter your born year :'))
    month =int(input('enter your born month :'))
    day= int(input('enter your born day :'))
    birthday = datetime(year,month,day)
    return birthday

def calculate_dates(birthday):
    now = datetime.now()
    birthday = datetime(birthday.year, birthday.month, birthday.day)
    return ((now.today()-birthday ).days + 1)/365.25
bithd = Get_birthday()
age = calculate_dates(bithd)
print(age ,'years')