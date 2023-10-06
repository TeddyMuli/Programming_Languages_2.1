import datetime
print("****Calculator*****")
todays_date = datetime.datetime.now()

name = input("Hi, enter your name > ")
date_of_birth = input("Enter your date of birth (dd/mm/yyyy) > ")
birthdate = datetime.datetime.strptime(date_of_birth, '%d/%m/%Y')

age = todays_date - birthdate

years = ((age.total_seconds()) / (365.242*24*3600))
years_int = int(years)

months = (years - years_int) * 12
months_int = int(months)

days = (months - months_int) * (365.242/12)
days_int = int(days)

print(f"Hi {name}, you are {years_int} years, {months_int} months and {days_int} days old.")
