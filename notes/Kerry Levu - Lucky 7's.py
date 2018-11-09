import random

money = 15
money = int(money)


highest_money = list()

amount_of_rounds = 0


while money > 0:
    highest_money.append(money)
    dice_int_1 = (random.randint(1, 6))
    dice_int_2 = (random.randint(1, 6))
    dice_roll = dice_int_1 + dice_int_2
    print("Dice roll : %d" % dice_roll)
    money -= 1

    if dice_roll == 7:
        money += 4
        print("You have $%d right now!" % money)
        amount_of_rounds += 1
    else:
        print("You have $%d right now!" % money)
        amount_of_rounds += 1

print()
print()

print("You lasted %d bets until you hit rock bottom." % amount_of_rounds)
print()

print(highest_money)

print(len(highest_money))

print(max(highest_money))

print("The highest amount of money you had was %d" % highest_money)
