print('Welcome to Treasure Island.')
print('Your mission is to find the treasure.')
firstChoice= input('There are two ways which one do you want to go? left or right ')
if firstChoice == 'right':
    secondChoice = input ('Good choice you are walking down the and you saw river. \nDo you want to wait for boat or swim? wait or swim ')
    if secondChoice == 'wait':
        thirdChoice = input ('Good choice you got to other side of the river. \nThere are three doors red, blue and green. \n choose one ')
        if thirdChoice == 'red':
            print('You won')
        else:
            print('Game Over. You got eaten by lions.') 
    else:
        print('Game Over. You got eaten by a crocodile.') 
else:
    print('Game Over')