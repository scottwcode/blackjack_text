######## Blackjack House Rules for this project ###########
# There is one deck of cards
# There are no jokers
# The Jack/Queen/King all count as 10
# The the Ace can count as 11 or 1
# The following list is the deck of cards:
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn
# Cards are not removed from the deck as they are drawn
# The computer is the dealer

import random
# from replit import clear
from art import logo


def deal_card(player_cards):
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    player_cards.append(random.choice(cards))
    # print(f"player_cards={player_cards}")


def calculate_score(cards):
    """Takes a list of cards and returns a score. Returns 0 if blackjack"""
    score = sum(cards)
    if cards == [11, 10] or cards == [10, 11]:
        return 0
    if score > 21 and (11 in cards):
        cards.remove(11)
        cards.append(1)
        score = sum(cards)
    return score


def compare(user_score, computer_score):
    """ Compares user's score to computer's score and returns appropriate message"""
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "You Lose, opponent has Blackjack :-("
    elif user_score == 0:
        return "You WIN with Blackjack!!"
    elif user_score > 21:
        return "You went over (busted). You lose :-("
    elif computer_score > 21:
        return "Opponent went over (busted). You WIN!!"
    elif user_score > computer_score:
        return "You WIN!!"
    else:
        return "You lose. :-("


def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    is_game_over = False

    # Deal first card
    deal_card(user_cards)
    deal_card(computer_cards)

    # Deal next card
    deal_card(user_cards)
    deal_card(computer_cards)
    # user_cards = [10,11]

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print("")
        print(f"\t Your Cards: {user_cards}, current score: {user_score}")
        print(f"\t Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            print("")
            user_hits = input(
                "Type 'y' to get another card, type 'n' to pass: ")
            if user_hits == "y":
                deal_card(user_cards)
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        deal_card(computer_cards)
        computer_score = calculate_score(computer_cards)

    print("")
    print(f"   Your final hand: {user_cards}, final score: {user_score}")
    print(
        f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
    print("")
    print(compare(user_score, computer_score))


# Main functionality
while input("\n Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    # clear()
    print("")
    play_game()
print("Thanks for playing. It was fun!!")
