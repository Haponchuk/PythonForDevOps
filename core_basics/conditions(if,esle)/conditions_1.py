# 1. Check if a number is positive, negative, or zero.

number = int(input("Enter a number: "))

if number > 0:
    print(f'Number {number} is positive')
elif number == 0:
    print('Number equals to 0')
else:
    print(f'Number {number} is negative')
