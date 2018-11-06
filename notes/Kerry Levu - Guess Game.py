import random
random_int = (random.randint(1, 10))
print(random_int)

guesses = 0
amount_guesses = guesses + 1



for i in (1, 2, 3, 4, 5):
    print("What number am I thinking of?")
    guess = input()
    guess = int(guess)
    if guess > random_int:
        print("Go lower.")
    elif guess < random_int:
        print("Go higher.")
    elif guess == random_int:
        print("How did you figure that out? You must've cheated.")


