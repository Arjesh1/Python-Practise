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

letter = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def encode(message, shiftNumber):
    encoded_message = []
    for index in range(len(message)):
        if message[index] == " ":
            encoded_message.append(' ')
        else: 
           if message[index] in letter:
               for letterIndex in range(len(letter)):
                  if message[index] == letter[letterIndex]:
                     encoded_message.append(letter[(letterIndex + shiftNumber) % len(letter)])
           else:
              encoded_message.append(message[index])

    return(''.join(encoded_message))

def decode(message, shiftNumber):
    decoded_message = []
    for index in range(len(message)):
        if message[index] == " ":
            decoded_message.append(' ')
        else:
           if message[index] in letter:
               for letterIndex in range(len(letter)):
                   if message[index] == letter[letterIndex]:
                       decoded_message.append(letter[(letterIndex - shiftNumber) % len(letter)])
           else:
                 decoded_message.append(message[index])

    return(''.join(decoded_message))


type = input("Type 'encode'to encrypt, type 'decode' to decrypt: \n>>> ").lower()
message = list(input('Type your message:\n>>> ').lower())
shiftNumber = int(input('Type your shift number:\n>>> '))

if type == "encode" :
    encoded_message = encode(message, shiftNumber)
    print(encoded_message)
elif type == "decode" :
    decoded_message = decode(message, shiftNumber)
    print(decoded_message)
else :
    print('Wrong request.') 

