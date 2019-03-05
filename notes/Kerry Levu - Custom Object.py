import random


class WaterBottle:
    def __init__(self, amountin=100, capacity=100, cap=False, color="black", rate_of_fire=5,
                 opacity="transparent", material="plastic"):
        self.capacity = capacity
        self.cap = cap
        self.color = color
        self.rate_of_fire = rate_of_fire
        self.opacity = opacity
        self.material = material
        self.amount_in = amountin

    def refill(self):
        self.amount_in = 100

    def empty(self):
        self.amount_in = 0

    def consume(self):
        print("You have %d in the water bottle." % self.amount_in)
        want = input("How much do you want to drink?")
        want = int(want)
        self.amount_in = self.amount_in - want
        print("You have %d in the water bottle." % self.amount_in)

    def bottle_flip(self):
        if self.amount_in == 30:
            chance = random.randint(1, 6)
            if chance == 6:
                print("You bottle flipped correctly. +6 to your attack.")
            else:
                print("Everyone laughs at you. You die.")
        elif self.amount_in > 30:
            print("You have too much water")
        elif self.amount_in < 30:
            print("You don't have enough water.")


my_watter_bottle = WaterBottle(100, 10, False, "green", 1, "opaque", "steel")

my_watter_bottle.consume()
my_watter_bottle.bottle_flip()
my_watter_bottle.refill()
