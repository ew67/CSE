import random

class Waterbottle:
    def __init__(self, amountin=100, capacity=100, cap=False, color="black", rate_of_fire=5,
                 opacity="transparent", material="plastic"):
        self.capacity = capacity
        self.cap = cap
        self.color = color
        self.rate_of_fire = rate_of_fire
        self.opacity = opacity
        self.material = material
        self.amountin = amountin

    def refill(self):
        self.amountin = 100
    def empty(self):
        self.amountin = 0
    def consume(self):
        print("You have %d in the water bottle." % self.amountin)
        want = input("How much do you want to drink?")
        want = int(want)
        amount_left = self.amountin - want
        print("You have %d in the water bottle." % amount_left)
    # def bottle_flip:
    #     random.randint(1,6)



kyle_waterbottle = Waterbottle(100, 10, False, "green", 1, "opaque", "steel")

print(kyle_waterbottle)

kyle_waterbottle.consume()