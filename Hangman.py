from ASCII_ART_resource_file import hangman_word_list,hangman_logo,hangman_stages

import random
chosen_word = random.choice(hangman_word_list)
word_length = len(chosen_word)
lives=6
print(hangman_logo)
print(f"the solution is {chosen_word}")

display=[]    #Store the output in a list form
for letter in range(word_length): #Create the same number of underscores with the word length
    display += "_"

end_of_game = False
while not end_of_game:
    guess = input("Guess a letter:").lower()

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position]=letter

    if guess in display:
        print(f"You have guessed {guess}.")

    if guess not in chosen_word:
        lives -= 1
        print(f"You have guessed {guess} and it is not in the word.You lose a life.")
        if lives == 0:
            end_of_game = True
            print("You lose.")

    print(display)

    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(hangman_stages[lives])



