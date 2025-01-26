# 2. Create a script that asks the user for their age and prints:
# "Child" if age < 12
# "Teenager" if 12 <= age < 18
# "Adult" if age >= 18

try:
    personAge = int(input('Enter ur age: '))
    if personAge < 12:
        print('Child')
    elif personAge >= 18:
        print('Adult')
    else:
        print('Teenager')
except ValueError:
    print('U entered wrong data type. Enter a number.')