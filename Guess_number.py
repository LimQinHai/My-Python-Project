from ASCII_ART_resource_file import Guess_number_logo
print(Guess_number_logo)

EASY_LEVEL_ATTEMPTS = 10
HARD_LEVEL_ATTEMPTS = 5

def set_difficulty():
    difficulty = input("Choose a difficulty.Type 'Easy' or 'Hard'. ")
    if difficulty == "easy":
        return EASY_LEVEL_ATTEMPTS
    else:
        return HARD_LEVEL_ATTEMPTS

def check_answer(number_guessed, number,attempt):
    if number_guessed > number:
        print("Too high")
        return attempt - 1
    elif number_guessed < number:
        print("Too low")
        return attempt - 1
    else:
        print(f"You got it! The answer is {number}")


print("Welcome To The Number Guessing Game !!")
print("I am thinking a number between 1 and 100.")
print("You are required to guess the number.")
def game():
    number_list = []
    for n in range(1, 101):
        number_list.append(n)
    import random
    number = random.choice(number_list)
    print(number)

    attempt=set_difficulty()
    number_guessed = 0
    while number_guessed != number:
        print(f"You have {attempt} attempts remaining to guess the number.")
        number_guessed = int(input("Make a guess:"))
        attempt = check_answer(number_guessed,number,attempt)
        if attempt == 0:
            print("You have run out of guesses.You lose.")
            return
        if number_guessed != number:
            print("Guess again.")


game()








