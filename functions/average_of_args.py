# Write a function that takes any number of arguments (*args) and returns their average.

def average_number(*args):
    return sum(args)/len(args)

average = average_number(15, 15, 30)
print(f'The average of the provided numbers is: {average}')
