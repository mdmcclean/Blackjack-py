import random
from IPython.display import clear_output
class Card():
	def __init__(self, suit, card_number):
		self.suit = suit
		self.card_number = card_number
		if card_number in '2345678910':
			self.card_value = int(self.card_number)
		elif card_number.upper() == 'ACE':
			self.card_value = 11
		else:
			self.card_value = 10

class CasinoPlayer():
	def __init__(self):
		self.bankroll = 1000
	def make_bet(self):
		bet_amount = 0
		while True:
			try:
				bet_amount = int(input(f'Total Bankroll: {self.bankroll}. How much would you like to wager?'))
			except:
				print('Not a valid amount... Try again')
			else:
				if bet_amount > self.bankroll or bet_amount < 0:
					print('Unable to bet this amount... Try again')
				else:
					print('Good Luck!')
					break
		return bet_amount

class Deck():
	def __init__(self):
		suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
		self.deck_of_cards = []
		cards = ['2','3','4','5','6','7','8','9','10','Jack','Queen','King', 'Ace']
		for i in suits:
			for j in cards:
				self.deck_of_cards.append(Card(i,j))
		random.shuffle(self.deck_of_cards)
	def deal_card(self):
		return self.deck_of_cards.pop()
                
class Hand():
	def __init__(self):
		self.total = 0
		self.aces = 0
		self.card_list = []
	def hit(self, card):
		self.card_list.append(card)
		if card.card_number.upper() == 'ACE':
			self.aces += 1
		self.total += card.card_value
		if self.total > 21 and self.aces > 0:
			self.aces -= 1
			self.total -= 10
	def display_cards(self, dealer = False):
		for i in range(0, len(self.card_list)):
			if dealer and i == 0:
				print('X X')
			else:
				print(f'{self.card_list[i].card_number} of {self.card_list[i].suit}')

def display_game(player_turn = False):
	dealer_score = dealer.total

	if player_turn:
		dealer_score = ''
	print(f'Dealer Cards: {dealer_score}')
	dealer.display_cards(player_turn)

	print('\nPlayer Total: {}'.format(player.total))
	player.display_cards()
print('Welcome to the BlackJack Table!\n\n')

casino_guy = CasinoPlayer()
while True:
	card_deck = Deck()
	dealer = Hand()
	player = Hand()
	dealer.hit(card_deck.deal_card())
	dealer.hit(card_deck.deal_card())
	player.hit(card_deck.deal_card())
	player.hit(card_deck.deal_card())

	bet = casino_guy.make_bet()
	bust = False
	display_game(True)


	while True:
		selection = ''
		while selection.upper() != 'H' and selection.upper() != 'S':
			selection = input(f"You have {player.total}... Would you like to (H)it or (S)tay?")
		if selection.upper() == 'H':
			player.hit(card_deck.deal_card())
			clear_output()
			display_game(True)
		else:
			break
		if player.total == 21:
			print('21!!!')
			break
		elif player.total > 21:
			clear_output()
			bust = True
			print('BUST')
			break

	display_game()

	if bust == False:
		while dealer.total < 17:
			dealer.hit(card_deck.deal_card())
		clear_output()
		display_game()

	print()
	if (bust or dealer.total > player.total) and dealer.total <= 21:
		print(f'You Lose! Dealer: {dealer.total} You: {player.total}')
		casino_guy.bankroll -= bet
	elif dealer.total == player.total:
		print(f'Both you and the dealer ended up with: {player.total}.... PUSH')
	else:
		print(f'You Won! Dealer: {dealer.total} You: {player.total}')
		casino_guy.bankroll += bet

	if casino_guy.bankroll == 0:
		print(f"Okay Buddy, you are out of money... I'm going to have to ask you to leave")
		break
	selection = ''
	while selection.upper() != 'Y' and selection.upper() != 'N':
		selection = input('Would you like to play again? (Y)es or (N)o')
		clear_output()
	if selection.upper() == 'N':
		print('Thank you for playing BlackJack. Come back soon!')
		break

