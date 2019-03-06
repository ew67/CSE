import random


class Item(object):
    def __init__(self, name, value):
        self.Name = name
        self.Value = value


class Weapon(Item):
    def __init__(self, name, value, damage, element, role, material):
        super(Weapon, self).__init__(name, value)
        self.damage = damage
        self.element = element
        self.role = role
        self.material = material

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
    def __init__(self, name, value, damage, element, role, material, handedness):
        super(Melee, self).__init__(name, value, damage, element, role, material)
        self.handedness = handedness


class Ranged(Weapon):
    def __init__(self, name, value, damage, element, role, material, ammo_type, weapon_range):
        super(Ranged, self).__init__(name, value, damage, element, role, material)
        self.ammo_type = ammo_type
        self.weapon_range = weapon_range


class Sword(Melee):
    def __init__(self, name, value, damage, element, role, material, sword_type, handedness):
        super(Sword, self).__init__(name, value, damage, element, role, material, handedness)
        self.sword_type = sword_type


class Mace(Melee):
    def __init__(self, name, value, damage, element, role, material, handedness):
        super(Mace, self).__init__(name, value, damage, element, role, material, handedness)


god_mace = Mace("Mac", "1500", 5, "Fire", "Knight", "Diamond", "1-Handed")


god_mace.attack()
