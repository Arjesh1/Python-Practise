# strings
name = 'Arjesh'

# Integers
experience = 1.5

# Boolean
is_SDeveloper = True

# Array
skills = ['JS', 'TS', 'Python', 'React']

# object
userData = {
    'name' : 'Arjesh',
    'experience' : 1.5,
    'is_Developer' : True,
    'skills' : ['JS', 'TS', 'Python', 'React'],
}

#  Prints a string into the console, and asks the user for a string input.
info = input('What do you want to know?')

# CONDITIONALS
if info == 'name':
    print('His name is '+ name)
elif info == 'experience':
    print('His experience is '+ userData['experience'])
elif info == 'isDeveloper' and userData['is_Developer'] == True:
    print('Yes, he is a developer')
elif info == 'skills':
    print('His name is '+ ','.join(userData['skills']))
else:
    print('No record found')




