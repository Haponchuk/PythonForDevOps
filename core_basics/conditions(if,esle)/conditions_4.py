# 4. Create a program to classify grades:
# A: 90-100
# B: 80-89
# C: 70-79
# D: 60-69
# F: Below 60

grade = int(input('Enter ur grade from 0 to 100: '))
if grade >= 90:
    print('A')
elif grade >= 80:
    print('B')
elif grade >= 70:
    print('C')
elif grade >= 60:
    print('D')
else:
    print('F')
