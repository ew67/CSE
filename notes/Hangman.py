import random

random_answer_words_list = ["purple", "blue", "dog", "cat", "sky", "biology", "edison", "clovis", "black", "white",
                            "ghosts", "hangman"]

answer_word = (random.choice(random_answer_words_list))
string1 = answer_word
answer_in_list = list(answer_word)

# print(answer_word)  # Debug to see Answer.


# Custom Word Options - Delete # to enable.
# custom_word_answer = []
# custom_word_answer.append(input("You want to play your own game, with your own word? Well, put it here then."))

# while answer_in_list

player_guess = input("What's your guess?")

for character in answer_in_list:
    if character == player_guess:
        # replace with a *
        current_index = answer_in_list.index(character)
        answer_in_list.pop(current_index)
        answer_in_list.insert(current_index, "*")

print(answer_in_list)
