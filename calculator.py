def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    return a / b

operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

print('Welcome to the calculator')
def calculator():
   firstNumber = float(input('What is the first number? '))
   print('+ \n-\n*\n/')
   should_continue = True
   while should_continue :
      operation =  input('Pick an operation ')
      nextNumber = float(input('What is the next number? '))
      answer = operations[operation](firstNumber, nextNumber)
      result = f'{firstNumber}  {operation}  {nextNumber} = {answer}'
      print(result)
      continue_calculation = input(f'Type "y" to continue calculating with {answer}, or type "n" to start a new calculation: ')

      if continue_calculation == 'y':
         firstNumber = answer
      else:
         should_continue = False
         calculator()

calculator()
