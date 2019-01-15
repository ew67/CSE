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
answer_hidden = answer_word
guesses_left = 8
letters_used = []
answer_in_list_joined = "".join(answer_in_list)


for i in range(len(answer_word)):
    print("This word has %s letters." % len(answer_word))
    print()
    player_guess = input("What's your guess?")
    letters_used.append(player_guess)

    if player_guess in answer_in_list:
        print("That's the right letter!")
        current_index = answer_in_list.index(player_guess)
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
