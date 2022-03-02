from ASCII_ART_resource_file import Blackjack_logo
import random

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    if (len(cards)==2) and (10 in cards) and (11 in cards):
        return 0
    if len(cards)>=2 and (sum(cards)>21) and (11 in cards):
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare_cards(total_user_score,total_computer_score):
    if total_user_score == total_computer_score:
        return "    It is a draw !"
    elif total_computer_score == 0:
        return "    Computer gets a Blackjack! You lose."
    elif total_user_score == 0:
        return "    You get a Blackjack! You win !!"
    elif total_computer_score>21:
        return "    You win! Because computer went bust !! haha"
    elif total_user_score > 21:
        return "    You went bust. You lose..."
    elif total_user_score > total_computer_score:
        return "    You win !"
    else:
        return "    You lose."

def Blackjack():
    print(Blackjack_logo)

    user_cards = []
    computer_cards = []
    for n in range(0,2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    total_user_score = calculate_score(user_cards)
    total_computer_score = calculate_score((computer_cards))
    print(f"Your cards:{user_cards}, current scores:{total_user_score}")
    print(f"Computer's first hand: {computer_cards[0]}")

    game_over = False
    while not game_over:
        if (total_computer_score==0) or (total_user_score==0):
            game_over = True
        else:
            if total_user_score <= 17:
                draw_card = input("Do you want to draw another card? Type 'y' if you want, otherwise type 'n' ").lower()
            else:
                draw_card = input("You got enough numbers.Type 'y' if you want to draw more card.")
            if draw_card == "y":
                user_cards.append(deal_card())
                total_user_score = calculate_score(user_cards)
                print(f" Your cards:{user_cards}, current scores:{total_user_score}")
            else:
                game_over = True


        while total_computer_score <= 17:
                computer_cards.append(deal_card())
                total_computer_score = calculate_score((computer_cards))

        if total_user_score == 0 or total_user_score == 21 or total_user_score > 21:
            game_over = True
        if total_computer_score == 0 or total_computer_score == 21 or total_computer_score > 21:
            game_over = True

    print(f"   Your final hand: {user_cards}, final score: {total_user_score}\n")
    print(f"   Computer's final hand: {computer_cards}, final score: {total_computer_score}\n")
    print(compare_cards(total_user_score,total_computer_score))

while input("Do you want to play a game of Blackjack? Type'y' or 'n':").lower() == "y":
    Blackjack()
print("Thank you !! Hope to see you again. Bye~~")
