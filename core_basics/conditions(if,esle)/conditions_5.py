# 5. Write a program that checks if a given year is a leap year.
year = int(input())

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f'{year} year is Leap')
else:
    print(f'{year} year is not Leap')