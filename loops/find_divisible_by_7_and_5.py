# Use a while loop to find the first number divisible by 7 and 5 within the range of 50 to 100.

number = 50
while number < 100:
    if number % 7 == 0 and number % 5 == 0:
        print(f'{number} is divisible by 5 and 7')
        break
    else:
        number += 1