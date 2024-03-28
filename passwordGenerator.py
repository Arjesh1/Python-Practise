import random

letter = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z', 'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '-', '=', '{', '}', '[', ']', '|', ':', ';', ',', '.', '/', '?', '~']

print('Welcome to Python password generator.')
passwordLength = int(input('Length of password '))
totalSymbol = int(input('Numbers of symbol '))
totalNumber = int(input('Numbers of number '))

password_list = []
for character in range(1, passwordLength - totalNumber - totalSymbol + 1):
    password_list += random.choice(letter)

for character in range(1, totalSymbol + 1):
    password_list += random.choice(symbols)

for character in range(1, totalNumber + 1):
    password_list += random.choice(numbers)

random.shuffle(password_list)

print('Your Password is ' + ''.join(password_list))