# Write a function that takes a name as input and prints a personalized greeting.

def greetings(name='User'):
    print(f'Nice to meet you, {name}')
    
user_name = input("Enter your name: ").strip()
if not user_name:
    user_name = 'User'
greetings(user_name)