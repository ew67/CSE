import random

random_answer_words_list = ["purple", "blue", "dog", "cat", "sky", "biology", "edison", "clovis", "black", "white",
                            "ghosts", "hangman", "United Nations", "Volleyball", "Soviet Union", "Washington",
                            "Bookshelf", "Vietnamese", "Japanese", "American", "Korean", "Chinese", "Polish", "Mexican",
                            "Laos", "Hispanic", "Spike", "Set", "Pass", "Molten", "Intel", "AMD", "Nvidia", "Steam",
                            "Battlefield", "New Year , New Me", ]
answer_word = "boba"
# Remove After
# answer_word = (random.choice(random_answer_words_list))
string1 = answer_word
answer_in_list = list(answer_word)
guesses_left = 8
letters_used = []
answer_in_list_joined = "".join(answer_in_list)
win = 0
answer_hidden = []


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


print(answer_hidden)
while win == 0:
    print("This word has %s letters." % len(answer_word))
    print()
    player_guess = input("What's your guess?")
    letters_used.append(player_guess)

    if player_guess in answer_in_list:
        print("That's the right letter!")
        current_index = 0
        found_index = index_of(answer_in_list, player_guess, current_index)
        print(found_index)
        while found_index >= 0:
            answer_hidden.pop(found_index)
            answer_hidden.insert(found_index, player_guess)
            current_index = found_index + 1
            found_index = index_of(answer_in_list, player_guess, current_index)
        print()
        print(answer_hidden)
    elif player_guess not in answer_in_list:
        guesses_left -= 1
    print("You have %d guesses left." % guesses_left)


'''for character in answer_in_list:
    if character == player_guess:
        # replace with a *
        current_index = answer_in_list.index(character)
        answer_in_list.pop(current_index)
        answer_in_list.insert(current_index, "a")
'''

print(answer_in_list)
print(answer_in_list_joined)
