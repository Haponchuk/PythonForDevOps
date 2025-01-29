# Create a function that accepts a list of numbers and returns their sum.

def sum_of_numbers(numbers):
    if not numbers:
        return 0
    return sum(numbers)

sumx = sum_of_numbers([1, 4, 8, 11, 15])
print(sumx)