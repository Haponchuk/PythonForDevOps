# Write a function that takes a list of numbers 
# and returns the second largest number. 
# Handle cases where the list has fewer than two unique numbers.


# The function does not handle cases where the list has fewer than two unique numbers. 
# For example, [5, 5, 5] would incorrectly return the same number :cc


def second_largest(numbers_list):
    if not numbers_list:
        return 'Number is empty. Reenter.'

    if numbers_list[0] > numbers_list[1]:
        max1 = numbers_list[0]
        max2 = numbers_list[1]
    else:
        max1 = numbers_list[1]
        max2 = numbers_list[0]

    for i in range(2, len(numbers_list)):
        if numbers_list[i] > max1:
            max2 = max1
            max1 = numbers_list[i]
        elif numbers_list[i] > max2:
            max2 = numbers_list[i]

    return max2
        

list_of_numbers = [1, 5, 10, 15, 125, 15, 14, 14, 16]
second_max_number = second_largest(list_of_numbers)
print(f'The second largest number is: {second_max_number}')
