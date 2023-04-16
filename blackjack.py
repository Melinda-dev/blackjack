import random
from replit import clear

# Define the deck of cards, each card has 2 elements: suit and rank
suits = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
ranks = [int(10) if rank in ['Jack', 'Queen', 'King'] else int(11) if rank == 'Ace' else int(rank) for rank in ranks]
deck = [(suit, rank) for suit in suits for rank in ranks]


# Shuffle the deck and draw a card
def draw_card(deck):
    random.shuffle(deck)
    return deck.pop()

# calculate the score from the cards
def calculate_sum(cards_in_hand):
    #print("enter calculation function. ")
    # print(cards_in_hand)
    result = 0
    for each_card in cards_in_hand:
        #print(each_card)
        result += int(each_card)

    for each_card in cards_in_hand:
        if each_card == 11 and result > 21:
            result = result - 10

    return result

#compare user_sum and computer_sum
def compare(user_sum, computer_sum):
    print(f" Your cards: {user_card}, current score: {user_sum}")
    print(f" computer cards: {computer_card}, current score: {computer_sum}")

    if user_sum > 21 and computer_sum > 21:
        print("Game is over. no one wins.")
    if user_sum == computer_sum:
        print( "Draw ")
    elif computer_sum == 21:
        print("you lose, opponent has Blackjack ")
    elif user_sum == 21:
        print("you win with a Blackjack ")
    elif user_sum > 21:
        print("You went over. You lose ")
    elif computer_sum > 21:
        print("Opponent went over. You win ")
    elif user_sum > computer_sum:
        print( "You win ")
    else:
        print("You lose ")

user_ranks = []  # store user's card rank
computer_ranks = []
user_card = [] # store user's cards list
computer_cards = []
user_sum = 0
computer_sum = 0
game_over = False


# initially, both get 2 cards

for i in range(2):
    user_card = draw_card(deck)
    #print(user_card):  data type is tuple
    user_ranks.append(user_card[1])
    computer_card = draw_card(deck)
    computer_ranks.append(computer_card[1])


print(f" Your two initial cards' are {user_card}")

while not game_over:
    computer_sum = calculate_sum(computer_ranks)

    while computer_sum is not None and computer_sum < 17:
        computer_card = draw_card(deck)
        #print(computer_card)
        computer_ranks.append(computer_card[1])
        #print(computer_ranks)
        # computer_cards.append(draw_card(deck))
        computer_sum = calculate_sum(computer_ranks)

        if computer_sum >= 17:
            break

    while True:
        user_continue_or_not = input("Do you want to continue? Yes or No: ").lower()
        if user_continue_or_not == "yes":
            new_card = draw_card(deck)[1]
            print(new_card)
            user_ranks.append(new_card)
            user_sum = calculate_sum(user_ranks)
        else:
            user_sum = calculate_sum(user_ranks)
            break

    compare(user_sum, computer_sum)
    game_over = True

