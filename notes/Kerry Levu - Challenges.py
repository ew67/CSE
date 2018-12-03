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


# Challenge 7
def challenge7(number):
    print(number+number*number+number**3)


challenge7(9)