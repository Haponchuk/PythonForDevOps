# Write a function that calculates the factorial of a number using recursion.


def factorial(number):

    if number <= 1:
        return 1
    else: 
       return number * factorial(number - 1)
    
number = int(input('Enter ur number to calc the factorial: '))
print(factorial(number))