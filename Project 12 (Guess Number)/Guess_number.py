from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def chack_answer(guess, answer, turns):
    if guess > answer:
        print("Too high")
        return turns -1
    elif guess < answer:
        print("Too low")
        return turns -1
    else:
        print(f"You won, The correct answer is {answer}")

def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == 'easy':
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS
    
def game():
    print("Welcome to the Number Guessing Game")
    answer = randint(1, 100)
    print(f"{answer}")

    turns = set_difficulty()
    guess = 0
    
    while guess != answer:
        print(f"You have {turns} left to guess the number")
        guess = int(input("Guess: "))
        turns = chack_answer(guess, answer, turns)
        if turns == 0:
            print("You lose")
        elif guess != answer:
            print("Guess again")

game()