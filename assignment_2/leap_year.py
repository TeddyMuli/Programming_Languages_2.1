# Teddy Muli Ndaisi         SCT211-0023/2022

year = int(input("Enter the year > "))

if ((year % 100 == 0) and (year % 400 != 0)):
        print(f"{year} is not a leap year")
else:
    if (year % 4 == 0):
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")
