# word_list = ["ardvark", "baboon", "camel"]

import random
from hangman_words import word_list
from hangman_art import stages, logo

print(logo)

chosen_word = random.choice(word_list)

display = ["_" for i in chosen_word]
lives = 6

while "_" in display:
    user_ans = input("Guess a letter: ").lower()

    for i in range(len(chosen_word)):
        if user_ans == chosen_word[i]:
            display[i] = user_ans

    if user_ans not in chosen_word:
        lives -= 1
        if lives == 0:
            print(''.join(display))
            print(stages[lives])
            print("Your Lose!")
            break

    print(''.join(display))
    print(stages[lives])


if "_" not in display:
    print("Your Win!")