import random
from ASCII_ART_resource_file import Higher_Lower_game_logo
from Higher_Lower_Game_Data import data
from ASCII_ART_resource_file import vs
import replit
def check_answer(answer,account_A_follower,account_B_follower):
    if account_A_follower > account_B_follower:
        return answer == 'a'
    else:
        return answer == 'b'


print(Higher_Lower_game_logo)
game_over = False
score = 0
account_B = random.choice(data)

while not game_over:
    account_A = account_B
    account_B = random.choice(data)
    while account_A == account_B:
        account_B = random.choice(data)

    print(f"Compare A: {account_A['name']}, a {account_A['description']}  from {account_A['country']}\n")
    print(vs)
    print(f"Against B: {account_B['name']}, a {account_B['description']}  from {account_B['country']}")
    account_A_follower = account_A["follower_count"]
    account_B_follower = account_B["follower_count"]
    answer = input("Who has more followers in Instagram. Choose'A'or'B'.").lower()

    is_correct = check_answer(answer,account_A_follower,account_B_follower)

    replit.clear()
    print(Higher_Lower_game_logo)
    if is_correct:
        score +=1
        print(f"You are right. Currently score:{score}")

    else:
        game_over = True
        print(f"Sorry.You are wrong. Final score:{score}")