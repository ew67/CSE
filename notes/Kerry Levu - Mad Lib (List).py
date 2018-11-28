print(123)

# Inputs / Questions

word_list = []


word_list.append(input("Give me an adjective."))
word_list.append(input("Give me another adjective."))
word_list.append(input("I need a type of bird."))
word_list.append(input("Give me the name of a room in a house."))
word_list.append(input("Maybe a Past Tense of a Verb?"))
word_list.append(input("Now give me a Present Tense Verb."))
word_list.append(input("Think of a name, any name."))
word_list.append(input("Suggest me a noun."))
word_list.append(input("Type     in the first liquid that you can think of."))
word_list.append(input("I dare you to give me a Verb ending in -ing"))
word_list.append(input("Name a Plural Body Part."))
word_list.append(input("A plural noun please."))
word_list.append(input("An -ing ending verb please."))
word_list.append(input("Ok last one, I want a noun"))
word_list.append(input("Give me another adjective."))

# Print Statements for Mad_Lib
# Printed 1 sentence at a time.

print()
print()

print("It was a %s,cold November day." % word_list[0])
print("I woke up to the %s smell of %s roasting in the %s downstairs." % (word_list[1],word_list[2],word_list[3]))
print("I %s down the stairs to see if I could help %s the dinner." % (word_list[4],word_list[5]))
print("My mom said to see if %s needs a fresh %s." % (word_list[6],word_list[7]))
print("So I carried a tray of glasses full of %s into the %s room." % (word_list[8], word_list[9]))
print("When I got there, I couldn't believe my %s!" % word_list[10])
print("There were %s %s on the %s!" % (word_list[11], word_list[12], word_list[13]))
