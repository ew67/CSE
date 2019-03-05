import random

class Item(object):
    def __init__(self, name, value):
        self.Name = name
        self.Value = value


class Weapon(Item):
    def __init__(self, name, value, damage, element, role):
        super(Weapon, self).__init__(name, value)
        self.damage = damage
        self.element = element
        self.role = role

    def attack(self):
        enemy_hp -= self.damage
        print("You swung your sword and did %s damage" % self.damage)

    @staticmethod
    def block():
        chance = random.randint(0, 1)
        if chance == 1:
            print("You've successfully blocked the attack!")
        else:
            print("Lmao you dropped your Note 8 and the screen cracks. You die.")

class Melee(Weapon):

class Ranged(Weapon):
    def __init__(self, name, value, damage, element, role, ammo_type, weapon_range):
        super(Ranged, self).__init__(name, value, damage, element, role)
        self.ammo_type = ammo_type
        self.weapon_range = weapon_range


test_sword = Ranged("Bow of Dirt", 0, 0.5, "Neutral", "", Arrow, 2)

test_sword.attack()