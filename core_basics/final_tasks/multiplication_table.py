# Write a function that takes a number as input 
# and prints its multiplication table from 1 to 10.

def multiplication(num, table_range):
    if not num:
        print('Enter a single number.')

    for i in range(1, table_range + 1):
        print(f'{num} * {i} = {i * num}')



number = int(input('Choose a number to print its multiplication table: '))
range_number = int(input('Choose a mulptiplication table range: '))

multiplication(number, range_number)