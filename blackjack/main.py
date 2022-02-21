import random, os
from art import logo

clear = lambda: os.system('clear')
play_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

def deal_card():
    return random.choice(cards)

def calculate_score(list_cards):
    if 11 in list_cards:
        if len(list_cards) == 2 and sum(list_cards) == 21:
            return 0
        elif sum(list_cards) > 21:
            list_cards[list_cards.index(11)] = 1
    return sum(list_cards)

def compare(user_score, computer_score):
    if user_score == computer_score:
        return 'draw'
    elif computer_score == 0:
        return ("Lose, opponent has Blackjack 😱")
    elif user_score == 0:
        return ("Win with a Blackjack 😎")
    elif user_score > 21:
        return ("You went over. You lose 😭")
    elif computer_score > 21:
        return ("Opponent went over. You win 😁")
    elif computer_score > user_score:
        return ("You lose 😤")
    else:
        return ("You win 😃")

while play_game == 'y':
    clear()
    print(logo)
    
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    user_cards = []
    computer_cards = []
    is_done = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())


    while not is_done:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"    Your cards: {user_cards}, current score: {user_score}")
        print(f"    Computer's first card: {user_cards[0]}")

        if computer_score == 0 or user_score == 0 or user_score > 21:
            is_done = True
        else:
            if input("Type 'y' to get another card, type 'n' to pass: ") == 'y':
                user_cards.append(cards[deal_card()])
            else:
                is_done = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"    Your final hand: {user_cards}, final score: {user_score}")
    print(f"    Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))
    
    play_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
