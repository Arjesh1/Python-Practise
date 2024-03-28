import random

userSelection = int(input('Welcome to the rock scissor and paper.\nType 0 for rock, 1 for scissor and 2 for paper'))
if userSelection == 0:
    print('''
    You
                                       /\| | | |
                                      / /|_|_|_|
                                      \        |
            (  ( ) ) ( )  )            \_______/
           ( ( ( ( )  )  ) )           /______/
          ( ( )) ) (   ) ( ( )        /       /
          ( (__.-.___.-.__) )        /       /
          / ---._.---._.---\        /       /
          \||    '/  '   ||/       /       /
            |||  (_     |||       /       /
             || ///\\\  ||\______/       /
        ___/ ||||\__/|||||/             /
       /   \   ||||||||  /             /
      /     \   ||||||  /        _____/
          ''')
elif userSelection == 1:
  print('''
  You 
            ,/'
   (_).  ,/'
   __  ::
  (__)'  `\.
            `\.
        ''')
elif userSelection == 2:
  print('''  
  You       
          __________
         |   Paper  |
         |&&& ======|
         |=== ======|
         |=== == %%$|
         |[_] ======|
         |=== ===!##|
         |__________|
        ''')
  
computerSelection = random.randint(0,2)

if computerSelection == 0:
    print('''
    Computer
                                       /\| | | |
                                      / /|_|_|_|
                                      \        |
            (  ( ) ) ( )  )            \_______/
           ( ( ( ( )  )  ) )           /______/
          ( ( )) ) (   ) ( ( )        /       /
          ( (__.-.___.-.__) )        /       /
          / ---._.---._.---\        /       /
          \||    '/  '   ||/       /       /
            |||  (_     |||       /       /
             || ///\\\  ||\______/       /
        ___/ ||||\__/|||||/             /
       /   \   ||||||||  /             /
      /     \   ||||||  /        _____/
          ''')
elif computerSelection == 1:
  print('''
  Computer       
            ,/'
   (_).  ,/'
   __  ::
  (__)'  `\.
            `\.
        ''')
elif computerSelection == 2:
  print(''' 
  Computer        
          __________
         |   Paper  |
         |&&& ======|
         |=== ======|
         |=== == %%$|
         |[_] ======|
         |=== ===!##|
         |__________|
        ''')
   

if userSelection == computerSelection:
   print('It is a draw.')
elif (userSelection == 0 and computerSelection == 1) or \
        (userSelection == 1 and computerSelection == 2) or \
        (userSelection == 2 and computerSelection == 0):
    print('You win!')
else:
    print('You lose!')