# Write a function that takes a string as input 
# and returns the string reversed. Include a check to handle empty input.

def reverse_string(string_to_reverse):
    if not string_to_reverse:
        return 'String is Empty. Reenter, please.'
    return string_to_reverse[::-1]

our_string = input('Enter string to reverse: ')
reversed_string = reverse_string(our_string)
print(reversed_string)