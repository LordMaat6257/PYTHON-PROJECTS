import random
import os
logo = """
.------.            _     _            _    _            _
|A_  _ |.          | |   | |          | |  (_)          | |
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   <
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |
      `------'                           |__/
"""
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def deal_card():
    """Returns a random card from the deck."""
    return random.choice(cards)
def calculate_score(card_list):
    """Take a list of cards and return the score calculated from the cards."""
    score = sum(card_list)
    if score == 21 and len(card_list) == 2:
        return 0
    if 11 in card_list and score > 21:
        card_list.remove(11)
        card_list.append(1)
        score = sum(card_list)
    return score
def compare(user_score, computer_score):
    """Compares user and computer scores and returns the game result."""
    if user_score == computer_score:
        return "It's a draw!"
    elif computer_score == 0:
        return "You lose, dealer has Blackjack"
    elif user_score == 0:
        return "You win with a Blackjack"
    elif user_score > 21:
        return "You went over 21. You lose"
    elif computer_score > 21:
        return "Dealer went over 21. You win"
    elif user_score > computer_score:
        return "You win"
    else:
        return "You lose"
def play_game():
    print(logo)
    print("Welcome to Blackjack!")
    user_cards = []
    computer_cards = []
    game_over = False
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    while not game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"   Your cards: {user_cards}, current score: {user_score}")
        print(f"   Dealer's first card: {computer_cards[0]}")
        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                game_over = True
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    print(f"   Your final hand: {user_cards}, final score: {user_score}")
    print(f"   Dealer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    os.system("cls" if os.name == "nt" else "clear")
    play_game()
