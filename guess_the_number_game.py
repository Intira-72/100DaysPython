import random


EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def set_difficulty():
    ask_u = True
    while ask_u:
        level = input("Choose a difficulty. Type 'easy' or 'hard' : ")
        if level == 'easy':
            return EASY_LEVEL_TURNS
        elif level == 'hard':
            return HARD_LEVEL_TURNS
        else:
            ask_u = False


def check_answer(guess, answer, turns):
    if guess > answer:
        print("Too high.\nGuess again.")
        return turns - 1
    elif guess < answer:
        print("Too low.\nGuess again.")
        return turns - 1
    else:
        print(f'You got it! The answer was {answer}.')


def guess_the_number():
    print("""Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.""")

    turns = set_difficulty()
    guess = 0
    answer = random.randint(1, 100)

    while guess != answer:
        print(f'You have {turns} attempts remaining to guess the number.')
        guess = int(input("Make a guess :"))

        if turns == 1:
            print(f"You're run out of guesses, you lose.")
            return
        else:
            turns = check_answer(guess, answer, turns)


if __name__ == '__main__':
    guess_the_number()

