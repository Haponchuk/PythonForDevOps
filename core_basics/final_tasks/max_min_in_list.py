# Write a function that takes a list of numbers as input 
# and returns both the maximum and minimum values. 
# Ensure the function handles cases where the list is empty.

def max_min_in_list(our_list):
    if not our_list:
        raise ValueError("The list is empty. Please provide at least one value.")

    return min(our_list), max(our_list)


list_to_enter = [5, 15, 102, 4, 114, 1000, 0, 212, 999]
min_list_value, max_list_value = max_min_in_list(list_to_enter)
print(f'Minimum value in our list is: {min_list_value}\nMaximum list value: {max_list_value}')

    # max = our_list[0]
    # for i in range(1, len(our_list)):
    #     if our_list[i] > max:
    #         max = our_list[i]
    # return max