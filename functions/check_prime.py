# Create a function that checks if a number is prime.
import math 

def prime_num_check(number):
    if number < 2: # all nums less than 2 are not prime
        return False
    
    for i in range(2, int(math.sqrt(number) + 1)): # int(math.sqrt(number) + 1) - we don't need to check all numbers up to number
        if number % i == 0:
            return False
    return True

number_to_check = int(input('Enter your number: '))
if prime_num_check(number_to_check):
    print(f'Number {number_to_check} is Prime')
else:
    print(f'Number {number_to_check} is Not Prime')