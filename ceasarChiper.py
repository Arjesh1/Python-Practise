print('''
                                _     _                       
                               | |   (_)                      
  ___ ___  __ _ ___  ___    ___| |__  _ _ __  _ __   ___ _ __ 
 / __/ _ \/ _` / __|/ _ \  / __| '_ \| | '_ \| '_ \ / _ \ '__|
| (_|  __/ (_| \__ \  __/   (__| | | | | |_) | |_) |  __/ |   
 \___\___|\__,_|___/\___|  \___|_| |_|_| .__/| .__/ \___|_|   
                                     | |   | |              
                                     |_|   |_|   
''')



type = input("Type 'encode'to encrypt, type 'decode' to decrypt: \n")
message = input('Type your message:\n')
shiftNumber = input('Type your shift number:\n')

messageList = list(message)
print(messageList)
