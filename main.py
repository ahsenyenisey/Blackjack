from art import logo
import os
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
    """system spell the shuffle card to user or computer with this function."""
    card = random.choice(cards)
    return card

def calculate_sum(list):
    """this function calculate sum of the cards which you or computer have.Also convert 11 to 1 if it's necessary."""
    if sum(list) == 21 and len(list) == 2:
        return 21

    if 11 in list and sum(list) > 21:
        list.remove(11)
        list.append(1)

    return sum(list)


def compare(u_score, c_score):
    """Compares the user score u_score against the computer score c_score and detect the last situation."""
    if u_score == c_score:
        return "Draw"

    elif c_score == 21:
        return "Lose, opponent has Blackjack."

    elif u_score == 21:
        return "Win with a Blackjack."

    elif u_score > 21:
        return "You went over. You lose."

    elif c_score > 21:
        return "Opponent went over. You win."

    elif u_score > c_score:
        return "You win"

    else:
        return "You lose."


def blackjack():
    blackjack_continue = True
    user_cards = []
    computer_cards = []
    print(logo)
    play_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if play_game == "y":
        for _ in range(2):
            user_cards.append(deal_card())
            computer_cards.append(deal_card())

        while blackjack_continue:
            user_score = calculate_sum(user_cards)
            computer_score = calculate_sum(computer_cards)
            print(f"Your cards: {user_cards}, current score: {user_score}")
            print(f"Computer's first card: {computer_cards[0]}")

            if user_score == 21 or computer_score == 21 or user_score > 21 or computer_score > 21:
                blackjack_continue = False
                print(f"Your final hand: {user_cards}, final score: {user_score}")
                print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
                print(compare(user_score, computer_score))

            else:
                should_continue = input("Type 'y' to get another card, type 'n' to pass: ")
                if should_continue == "y":
                    user_cards.append(deal_card())
                    computer_cards.append(deal_card())

                elif should_continue == "n":
                    blackjack_continue = False
                    print(f"Your final hand: {user_cards}, final score: {user_score}")
                    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
                    print(compare(user_score, computer_score))
                    os.system('cls')

        while computer_score != 21 and computer_score < 17:
            computer_cards.append(deal_card())
            computer_score = calculate_sum(computer_cards)
    else:
        os.system('cls')

blackjack()