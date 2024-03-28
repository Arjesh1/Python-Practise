print('Welcome to the roller coaster.')
height = int(input('What is your height?'))
if height < 120:
    print('Sorry you cant ride.')
else:
    print('You can ride.')
    age = int(input('What is your age?'))
    initialPrice = 0
    if age < 12:
        initialPrice += 5
    elif age <= 18:
        initialPrice += 7
    else:
        initialPrice += 12
    photos = input('Do you want photos?')
    if photos == 'yes':
        initialPrice += 3
    print(f'Your total bill is {initialPrice}')


