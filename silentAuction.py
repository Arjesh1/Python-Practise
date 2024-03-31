logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
print('Welcomme to silent auction.')
add_more = 'yes'
auctionList = []
highestBid = {}

while add_more == 'yes':
    name =  input('Bidders name? >> ')
    amount = input('Bid amount? >> $')
    auctionList.append({'name': name, 'amount': amount})
    add_more = input('Is there more bidders? yes or no >> ')

for bid in auctionList:
    highestBid = bid
    if bid['amount'] > highestBid['amount']:
        highestBid = bid
    
print(f'The higest bidder is {highestBid['name']} of amount ${highestBid['amount']}')