import random
random_int = (random.randint(1, 10))

guesses_left = 5
Win = False


while guesses_left > 0 and Win == False:
    print("What number am I thinking of?")
    guess = input()
    guess = int(guess)
    if guess > random_int:
        print("Go lower.")
        guesses_left -= 1
    elif guess < random_int:
        print("Go higher.")
        guesses_left -= 1
    elif guess == random_int:
        print("How did you figure that out? You must've cheated.")
        Win = True



if Win == False:
    print("You've lost. Try again buddy.")

