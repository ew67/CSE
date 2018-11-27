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

# Adding things to a list
holiday_list = []  # Always use Brackets for Lists
holiday_list.append("Tacos")
holiday_list.append("Bumblebee")
holiday_list.append("Red Dead Redemption 2")
print(holiday_list)

#  Notice this is "object.method(Parameters)"

# Remove things from a lst
holiday_list.remove("Tacos")
print(holiday_list)

# List Practice

'''
1. Make a new list with 3 items
2. Add a 4th item to the lis
3 Remove one of the first three items from the list.
'''

gift_list = ["Toys","Games","Roblox $10 Gift Card"]
gift_list.append("Food")
gift_list.remove("Toys")
print(gift_list)

gift_list.pop(0)  # Pop is like remove, but removes the item in the Index Number Instead
print(gift_list)

# Tuple
brands = ("Apple", "Samsung", "HTC")  # notice the parentheses
colors = ["blue", "red", "green", "black", "brown", "purple", "pink", "orange", "teal", "white", "yellow", "indigo",
          "violet", "magenta", "gray", "cyan",
          "tan", "lime", "Jade", "Silver"]
print(len(colors))


# Find the index
print(colors.index("violet"))

# Changing things into a list
string1 = "Jade"
list1 = list(string1)
print(list1)

for character in list1:
    if character == "u":
        # replace with a *
        current_index = list1.index(character)
        list1.pop(current_index)
        list1.insert(current_index, "*")

# Changing lists into strings
print("".join(list1))
