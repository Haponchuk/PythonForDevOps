# Write a program to calculate the sum of all even numbers between 1 and 50 using a for loop.

result = 0
for i in range (2, 51, 2):
    result += i
print(result)

# for i in range (1, 50):
#     if i % 2 == 0:
#         result += i
# print(result)