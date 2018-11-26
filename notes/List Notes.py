# Lists
shopping_list = ["whole milk", "PC", "Eggs", "Trash (Xbox One)", "Other Trash (PS4)", "Batteries"]
print(shopping_list)
print(shopping_list[0])
print("The second thing in the list is %s" % shopping_list[1])
print("The length of the list is %d" % len(shopping_list))

# Changing Elements in a list
shopping_list[0] = "2% milk"
print(shopping_list)
print(shopping_list[0])

# Looping through lists
# for item in shopping_list:
#     print(item)


# List Practice

name_list = ["Monique", "Jun", "June", "Angelina", "Danny", "Braydon", "Anthony", "Brian"]
name_list[2] = "James"
print(name_list[2])
print(name_list)

new_list = ["eggs", "cheese", "oranges", "raspberries", "banana"]
new_list[2] = "apples"
print("The last thing in the list is %s" % new_list[len(new_list) - 1])
print(new_list)

# Getting part of a list
print(new_list[1:3])
print(new_list[1:4])  # 1:4 goes up to the indices but doesn't include the last one
print(new_list[1:])  # Would include everything from Index 1 to the very end.
print(new_list[:2])  # This is the same thing, but it would go from the start, and only up to Index 2.
