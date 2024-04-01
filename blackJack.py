import random

cards = [11, 2 , 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]
play_game = input('Do you want to a game of Blackjack? Type "y" or "n" ')

def add_cards(cardsList):
   score = 0
   for card in cardsList:
      score += card
   if 11 in cards and score > 21:
       score -= 10
   return score
   

while play_game == 'y':
   player_card = [11,11]
   player_score = add_cards(player_card)
   computer_card = random.choices(cards, k=2)
   computer_score = add_cards(computer_card)
   game_Over = False
   print(f'   Your card: {player_card}, current score: {player_score}')
   print(f'   Computer first card: {computer_card[0]}')

   if computer_score == 21 or player_score == 21:
       game_Over = True

   another_card = input('Type "y" to get another card, type "n" to pass:  ')

   while not game_Over:
        if another_card == 'y':
            while another_card == 'y' and player_score < 21 and not game_Over:     
                player_card.append(random.choice(cards))
                player_score = add_cards(player_card)
                print(f'   Your card: {player_card}, current score: {player_score}')
                print(f'   Computer first card: {computer_card[0]}')
                another_card = 'n'
                if player_score > 21 or player_score == 21:
                   game_Over = True
                else:
                    another_card = input('Type "y" to get another card, type "n" to pass:  ')
                    
        else:
            while computer_score < 21 and not game_Over:
               computer_card.append(random.choice(cards))
               computer_score = add_cards(computer_card)
               if computer_score > 21 or computer_score == 21 or computer_score == 20:
                   game_Over = True

   print(f'Your final hand: {player_card}, final score: {player_score}')
   print(f'Computers final hand: {computer_card}, final score: {computer_score}')
    
   if player_score == computer_score: 
       print('Draw')
   elif player_score == 21:
       print('You have a BlackJack. You win')
   elif computer_score == 21:
       print('Opponent has a Blackjack. You loose')
   elif player_score > 21:
       print('You went over. You loose')
   elif computer_score > 21:
       print('Opponent went over. You win')
   else :
        if player_score < computer_score:
           print('Opponent is more near to 21. You loose')
        else:
            print('You are more near to 21. You win')
      
   play_game = input('\nDo you want to a game of Blackjack? Type "y" or "n" ')






