# strings
name = 'Arjesh'

# Integers
experience = 1.5

# Boolean
is_SDeveloper = True

# list
skills = ['JS', 'TS', 'Python', 'React']

# dictionaries
userData = {
    'name' : 'Arjesh',
    'experience' : 1.5,
    'is_Developer' : True,
    'skills' : ['JS', 'TS', 'Python', 'React'],
}

#  Prints a string into the console, and asks the user for a string input.
currentUser = input('What is your name?')
print(f'Hello {currentUser}')
info = input('What do you want to know about Arjesh?')

# CONDITIONALS
if info == 'name':
    print('His name is '+ name)
elif info == 'experience':
    print('His experience is '+ str(userData['experience']) + ' yrs')
elif info == 'isDeveloper' and userData['is_Developer'] == True:
    print('Yes, he is a developer')
elif info == 'skills':
    print('His skill are '+ ','.join(userData['skills']))
else:
    print('No record found')

# function with parameters
def add_function(a, b):
    return a + b

print(add_function(1,2))





