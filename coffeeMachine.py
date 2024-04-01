MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 300,
    "coffee": 100,
}

def calculate_total(two_dollar,one_dollar,fifty_cents,twenty_cents, ten_cents, five_cents ):
    return 2 * two_dollar + 1 * one_dollar + 0.50 * fifty_cents + 0.20 * twenty_cents + 0.10 * ten_cents + 0.05 * five_cents

while 2 > 1:
    print(resources)
    print('Welcome to the coffee machine.')
    print('espresso: $1.5\nlatte: $2.5\ncappuccino: $3')
    order = input('What would you like? (espresso/latte/cappuccino): ')
    if order in MENU:
        orderDescription = MENU.get(order)
        if orderDescription['ingredients']['water'] > resources["water"]:
            print('Sorry, we do not have enough water.')
        elif 'milk' in orderDescription['ingredients'] and orderDescription['ingredients']['milk'] > resources["milk"]:
            print('Sorry, we do not have enough milk.')
        elif orderDescription['ingredients']['coffee'] > resources["coffee"]:
            print('Sorry, we do not have enough coffee.')
        else:
            print('Please insert coins:')
            two_dollar = int(input('How many 2 dollars?: '))
            one_dollar = int(input('How many 1 dollars?: '))
            fifty_cents = int(input('How many 50 cents?: '))
            twenty_cents = int(input('How many 20 cents?: '))
            ten_cents = int(input('How many 10 cents?: '))
            five_cents = int(input('How many 5 cents?: '))
            amount = calculate_total(two_dollar,one_dollar,fifty_cents,twenty_cents, ten_cents, five_cents )
            print(amount)
            if amount >= orderDescription['cost']:
                if amount > orderDescription['cost']:
                    print(f'Here is your change of ${amount-orderDescription['cost']}')
                print(f'Here is your {order}. Enjoy')
                for resource in resources:
                    for ingredient in orderDescription['ingredients']:
                        if resource == ingredient:
                            resources[resource] -= orderDescription['ingredients'][ingredient]
            else:
                print(f'Thats not enough money. Refunding ${amount}')
    else: 
        print("Sorry we don't have your order.")


        

