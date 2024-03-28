import random

letter = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
upperCase = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '-', '=', '{', '}', '[', ']', '|', ':', ';', ',', '.', '/', '?', '~']

print('Welcome to Python password generator.')
passwordLength = int(input('Length of password - '))
totalSymbol = int(input('How many symbols do you want? - '))
totalNumber = int(input('How many numbers do you want? - '))
totalUppercase = int(input('How many uppercase do you want? - '))

password_list = []
for character in range(1, passwordLength - totalNumber - totalSymbol- totalUppercase + 1):
    password_list += random.choice(letter)

for character in range(1, totalUppercase + 1):
    password_list += random.choice(upperCase)

for character in range(1, totalSymbol + 1):
    password_list += random.choice(symbols)

for character in range(1, totalNumber + 1):
    password_list += random.choice(numbers)

random.shuffle(password_list)

print('Your Password is ' + ''.join(password_list))