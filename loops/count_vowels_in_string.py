# Write a for loop that iterates over a string and counts the number of vowels in it.
# a e i o u

find_wovels = input()
number_of_vowels = 0

for word in find_wovels.lower():
    if word in 'aeiou':
    #if word == 'a' or word == 'e' or word == 'i' or word == 'o' or word == 'u':
        number_of_vowels += 1

print(f'There is {number_of_vowels} vowels in word {find_wovels}')