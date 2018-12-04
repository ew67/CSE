import math
# Challenge 1
def challenge1(first_name, last_name):
    print(" %s , %s" % (last_name, first_name))


challenge1("ghost", "delaney")


# Challenge 2
def challenge2(number):
    if number % 2 == 0:
        print("That's an even number!")
    else:
        print("You have an odd number.")


challenge2(4)


# Challenge 3
def challenge3(base, height):
    area = base * height / 2
    print(area)


challenge3(3, 10)


# Challenge 4
def challenge4(number):
    if number > 0:
        print("That's a positive number")
    elif number < 0:
        print("Why so negative?")
    elif number == 0:
        print("You've got a zero")


challenge4(3)


# Challenge 5
def challenge5(radius):
    print("Radius : %s" % radius)
    answer = math.pi*radius*radius
    print("Area : %s " % answer)


challenge5(1)


# Challenge 6


def challenge6(radius):
    print("This is your radius : %s" % radius)
    answer = 4 / 3 * math.pi * radius ** 3
    print("This is your area : %s." % answer)


challenge6(3)


# Challenge 7
def challenge7(number):
    print(number+number*number+number**3)


challenge7(9)


def challenge8(number):
    if number < 150:
        print("This isn't it Chief.")
    elif number <= 2000:
        print("Looks good Chief.")
    elif number > 2000:
        print("Chief said to try again")


challenge8(555)


def challenge9(letter):
    # Can look for a way to accept both lowercase and uppercase
    vowels_list = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
    if letter in vowels_list:
        print("Yes, that's a vowel.")
    else:
        print("That's not a vowel.")


challenge9("A")


def challenge10()