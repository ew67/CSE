import random

money = 15
money = int(money)


highest_money_list = list()

amount_of_rounds = 0
max_money = 0
max_money = int(max_money)

while money > 0:
    highest_money_list.append(money)
    dice_int_1 = (random.randint(1, 6))
    dice_int_2 = (random.randint(1, 6))
    dice_roll = dice_int_1 + dice_int_2
    print("Dice roll : %d" % dice_roll)
    money -= 1

    if dice_roll == 7:
        money += 5
        print("You have $%d right now!" % money)
        amount_of_rounds += 1
        if max_money < money:
            max_money = money
    else: print("You have $%d right now!" % money)
    amount_of_rounds += 1
print()
print()

print("You lasted %d bets until you hit rock bottom." % amount_of_rounds)
print()

print(highest_money_list)

print(len(highest_money_list))

highest_money = (max(highest_money_list))

print("The highest amount of money you had was %d" % highest_money)
print(max_money)


