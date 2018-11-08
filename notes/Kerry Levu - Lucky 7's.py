import random

money = 15
money = int(money)

amount_of_rounds = 0


while money > 0:
    dice_int_1 = (random.randint(1, 6))
    dice_int_2 = (random.randint(1, 6))
    dice_roll = dice_int_1 + dice_int_2
    print(dice_roll)
    money -= 1

    if dice_roll == 7:
        money += 4
        print("You have $%d right now!" % money)
        amount_of_rounds += 1
    else:
        money -= 1
        print("You have $%d right now!" % money)
        amount_of_rounds += 1

print()
print()

print(amount_of_rounds)