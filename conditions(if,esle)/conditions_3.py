# 3. Write a program to determine if a number is divisible by both 3 and 5, only 3, only 5, or neither.
try:
    number = int(input('Enter a Number to be divided by two other numbers: '))
    divider1 = int(input('Enter first Divider: '))
    divider2 = int(input('Enter second Divider: '))

    if divider1 == 0 or divider2 == 0:
        print('Dividers cannot be zero. Please try again.')
    else:
        div1 = (number % divider1 == 0)
        div2 = (number % divider2 == 0)

    if div1 and div2:
        print(f'{number} is divisible by {divider1} and {divider2}')
    elif div1:
        print(f'{number} is divisible by {divider1}')
    elif div2:
        print(f'{number} is divisible by {divider2}')
    else:
        print(f'{number} is NOT divisible by {divider1} or {divider2}')
except ValueError:
    print('Reenter number as integer.')

# Challenge: Extend it to handle multiple divisors dynamically.
# Ask the user for two divisors and a number, and check if the number is divisible by both, either, or neither.