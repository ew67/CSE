import random


class Item(object):
    def __init__(self, name, value):
        self.Name = name
        self.Value = value


class Armor(Item):
    def __init__(self, name, value, durability, material, defense=5):
        super(Armor, self).__init__(name, value)
        self.durability = durability
        self.material = material
        self.defense = defense


class Helmet(Armor):
    def __init__(self, name, value, durability, material):
        super(Helmet, self).__init__(name, value, durability, material, 2)


class ChestPlate(Armor):
    def __init__(self, name, value, durability, material):
        super(ChestPlate, self).__init__(name, value, durability, material, 4)


class Leggings(Armor):
    def __init__(self, name, value, durability, material):
        super(Leggings, self).__init__(name, value, durability, material, 3)


class Boots(Armor):
    def __init__(self, name, value, durability, material):
        super(Boots, self).__init__(name, value, durability, material, 1)


class Consumable(Item):
    def __init__(self, name, value, durability):
        super(Consumable, self).__init__(name, value)
        self.durability = durability


class Potions(Consumable):
    def __init__(self, name, value, durability, heal_amount, mana_amount, splash=False):
        super(Potions, self).__init__(name, value, durability)
        self.splash = splash
        self.heal_amount = heal_amount
        self.mana_amount = mana_amount


class Food(Consumable):
    def __init__(self, name, value, durability, buff):
        super(Food, self).__init__(name, value, durability)
        self.buff = buff


class Weapon(Item):
    def __init__(self, name, damage, element, role, material, value):
        super(Weapon, self).__init__(name, value)
        self.damage = damage
        self.element = element
        self.role = role
        self.material = material

    def attack(self):
        print("You swung your sword and did %s damage" % self.damage)

    @staticmethod
    def parry():
        chance = random.randint(0, 1)
        if chance == 1:
            print("You've successfully blocked the attack!")
        else:
            print("Lmao you dropped your Note 8 and the screen cracks. You die.")


class Melee(Weapon):
    def __init__(self, name, value, damage, element, role, material, handedness):
        super(Melee, self).__init__(name, value, damage, element, role, material)
        self.handedness = handedness


class Shield(Melee):
    def __init__(self, name, damage, element, role, material, value, damage_block):
        super(Shield, self).__init__(name, damage, element, role, material, value, 1)
        self.damage_negation = damage_block

    @staticmethod
    def shield_block():
        print("You raise your shield in a defensive position.")

    @staticmethod
    def shield_bash():
        chance = random.randint(0, 1)
        if chance == 1:
            print("You charge with your shield, stunning the enemy.")
        else:
            print("You try charging forward, but your Note 8 falls out of your pocket and the back glass cracks. "
                  "You die.")


class Sword(Melee):
    def __init__(self, name, value, damage, element, role, material, sword_type, handedness):
        super(Sword, self).__init__(name, value, damage, element, role, material, handedness)
        self.sword_type = sword_type


class Mace(Melee):
    def __init__(self, name, value, damage, element, role, material, handedness):
        super(Mace, self).__init__(name, value, damage, element, role, material, handedness)


class Whip(Melee):
    def __init__(self, name, value, damage, element, role, material, whip_range):
        super(Whip, self).__init__(name, value, damage, element, role, material, handedness=False)
        self.range = whip_range


class Dagger(Melee):
    def __init__(self, name, value, damage, element, role, material, chance_bleed):
        super(Dagger, self).__init__(name, value, damage, element, role, material, handedness=False)
        self.chance_bleed = chance_bleed

    @staticmethod
    def stab():
        chance = random.randint(0, 1)
        if chance == 1:
            print("You gave them a present from the back.")
        else:
            print("Your Note 8 lights up, and gives your position away. You try to turn it off, but an arrow "
                  "comes by and cracks the screen. You die.")


class Ranged(Weapon):
    def __init__(self, name, value, damage, element, role, material, ammo_type, weapon_range, fire_rate):
        super(Ranged, self).__init__(name, value, damage, element, role, material)
        self.ammo_type = ammo_type
        self.weapon_range = weapon_range
        self.fire_rate = fire_rate


class Throwables(Ranged):
    def __init__(self, name, value, damage, material, weapon_range, fire_rate):
        super(Throwables, self).__init__(name, value, damage, None, None, material, None, weapon_range, fire_rate)


class Bow(Ranged):
    def __init__(self, name, value, damage, element, role, material, ammo_type, weapon_range, fire_rate):
        super(Bow, self).__init__(name, value, damage, element, role, material, ammo_type, weapon_range, fire_rate)


class Gun(Ranged):
    def __init__(self, name, value, damage, element, role, material, ammo_type, weapon_range, magazine, fire_rate):
        super(Gun, self).__init__(name, value, damage, element, role, material, ammo_type, weapon_range, fire_rate)
        self.magazine = magazine


class RocketLauncher(Ranged):
    def __init__(self, name, value, damage, element, role, material, ammo_type, weapon_range, explosion_range,
                 fire_rate):
        super(RocketLauncher, self).__init__(name, value, damage, element, role, material, ammo_type,
                                             weapon_range, fire_rate)
        self.explosion_range = explosion_range


class Magic(Ranged):
    def __init__(self, name, value, damage, element, role, material, weapon_range, fire_rate, mana, projectile):
        super(Magic, self).__init__(name, value, damage, element, role, material, None, weapon_range, fire_rate)
        self.mana_cost = mana
        self.projectile = projectile
