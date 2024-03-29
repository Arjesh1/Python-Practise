import random
import hangman_art
import hangman_words

print(hangman_art.logo)
print('Welcome to hangman game.')

word = random.choice(hangman_words.word_list)
guessedWord = ''
emptyLines = ''
lifeline = 6

for line in range (len(word)):
    emptyLines += '_'
 
while lifeline != 0 and emptyLines != word:
    print(hangman_art.stages[lifeline])
    print(f'{emptyLines}\n')
    userGuessedLetter = input('Guess a letter: ').lower()
    if len(userGuessedLetter) < 1:
        userGuessedLetter = input('Guess a letter: ').lower()
    if userGuessedLetter in word :
        positions = [pos for pos, char in enumerate(word) if char == userGuessedLetter]
        for position in positions:
            emptyLines = emptyLines[:position] + userGuessedLetter + emptyLines[position+1:]
        print(emptyLines)
    else:
       print('Wrong Answer')
       lifeline -= 1
       
if lifeline == 0:
    print(hangman_art.stages[lifeline])
    print('Game Over')
    print(f'The answer was: {word}')

if emptyLines == word:
    print('Congrats, You won')
