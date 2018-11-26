import random

money = 15
money = int(money)

amount_of_rounds = 0
max_money = 0
max_money = int(max_money)
round_most_money = 0

while money > 0:
    dice_int_1 = (random.randint(1, 6))
    dice_int_2 = (random.randint(1, 6))
    dice_roll = dice_int_1 + dice_int_2
    print("Dice roll : %d" % dice_roll)
    money -= 1

    if dice_roll == 7:
        money += 5
        print("You have $%d right now!" % money)
        amount_of_rounds += 1
        print("You're on Round %d" % amount_of_rounds)
        print()
        if max_money < money:
            max_money = money
            round_most_money = amount_of_rounds
    else:
        print("You have $%d right now!" % money)
        amount_of_rounds += 1
        print("You're on Round %d" % amount_of_rounds)
        print()


print()
print()

print("You lasted %d bets until you hit rock bottom." % amount_of_rounds)
print()


print("At round %d you had $%d! You probably should've stopped right there." % (round_most_money, max_money))
