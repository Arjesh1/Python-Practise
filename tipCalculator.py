print('Welcome to the tip calculator')
totalBill = input('What is the total bill?')
tipPercentage = input('How much percent do you want to tip?')
tipAmount =  int(totalBill) * (int(tipPercentage) / int(totalBill))
finalBillAmount = int(totalBill) + tipAmount
print(f'Your total bill after tip will be $ {str(finalBillAmount)}')
totalPeople = input('How many people are splitting the bill?')
print(f'Each one of you should pay $ {finalBillAmount/ int(totalPeople)}')