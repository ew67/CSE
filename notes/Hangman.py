import random
import string

random_answer_words_list = ["purple", "blue", "dog", "cat", "sky", "biology", "edison", "clovis", "black", "white",
                            "ghosts", "hangman", "United Nations", "Volleyball", "Soviet Union", "Washington",
                            "Bookshelf", "Vietnamese", "Japanese", "American", "Korean", "Chinese", "Polish", "Mexican",
                            "Laos", "Hispanic", "Spike", "Set", "Pass", "Molten", "Intel", "AMD", "Nvidia", "Steam",
                            "Battlefield", "New Year , New Me", ]
# answer_word = (random.choice(random_answer_words_list))
answer_word = "New Year,, New Me"
answer_word = answer_word.lower()
string1 = answer_word
answer_in_list = list(answer_word)
guesses_left = 8
letters_used = []
win = 0
answer_hidden = []
punctuation_list = list(string.punctuation + " ")
print(punctuation_list)
print(answer_word)

def index_of(word, letter, starting_index):
    """Finds an index starting at a given point
    @:return the index of the next instance
    """
    try:
        chopped_word = word[starting_index:]
        found_index = chopped_word.index(letter)
        return found_index + starting_index
    except ValueError:
        return -1


for i in range(len(answer_word)):
    answer_hidden.append("*")

# Find Punctuation
for char in punctuation_list:
    current_index = 0
    found_index = index_of(answer_in_list, char, current_index)
    while found_index >= 0:
        answer_hidden.pop(found_index)
        answer_hidden.insert(found_index, char)
        current_index = found_index + 1
        found_index = index_of(answer_in_list, char, current_index)

print("".join(answer_hidden))
print("This word has %s letters." % len(answer_word))
while win == 0:

    print()
    player_guess = (input("What's your guess?"))
    player_guess = player_guess.lower()
    letters_used.append(player_guess)

    if player_guess in answer_in_list:
        print("That's the right letter!")
        current_index = 0
        found_index = index_of(answer_in_list, player_guess, current_index)
        while found_index >= 0:
            answer_hidden.pop(found_index)
            answer_hidden.insert(found_index, player_guess)
            current_index = found_index + 1
            found_index = index_of(answer_in_list, player_guess, current_index)
        print()
        print("".join(answer_hidden))
    elif player_guess not in answer_in_list:
        guesses_left -= 1
        print("You have %d guesses left." % guesses_left)
    if guesses_left == 0:
        print("You've ran out of guesses and have lost.")
        win = 2
    if "*" not in answer_hidden:
        if guesses_left > 1:
            print("You've won the game! You had %d guesses left." % guesses_left)
        else:
            print("You've won the game! You had %d guess left." % guesses_left)
        win = 1