import random
print('Welcome to the Number Guessing Game!')
print('I am thinking of a number between 1 and 100.')

number =  random.randrange(1,100)
print(number)
lifeLine = 0
level = input('Choose a difficulty level. Type "easy" or "hard": ')
if level == 'easy':
    lifeLine = 10
elif level == 'hard': 
    lifeLine = 5

while lifeLine != 0:
    print(f'You have {lifeLine} attempts remaining to guess the number.')
    guessedNumber = int(input('Make a guess '))
    lifeLine -= 1
    if guessedNumber == number:
        print(f'Congrats you guessed the correct number. The answer was {number}')
        lifeLine = 0
    elif guessedNumber > number:
        print('Too high.')
    elif guessedNumber < number:
        print('Too low.')

if lifeLine == 0:
    print(f'Game over. The correct number was {number}')