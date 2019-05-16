import random


class Room(object):
    def __init__(self, name, north=None, south=None, east=None, west=None, up=None, down=None, description="",
                 characters=None, items=None):
        if items is None:
            items = []
        if characters is None:
            characters = []
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.up = up
        self.down = down
        self.description = description
        self.character = characters
        self.items = items
        self.escape = False


class Item(object):
    def __init__(self, name, value):
        self.name = name
        self.value = value


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
    def __init__(self, name, value, durability, buff, heal_amount):
        super(Food, self).__init__(name, value, durability)
        self.buff = buff
        self.heal_amount = heal_amount


class Weapon(Item):
    def __init__(self, name, damage, element, role, material, value):
        super(Weapon, self).__init__(name, value)
        self.damage = damage
        self.element = element
        self.role = role
        self.material = material


class Melee(Weapon):
    def __init__(self, name, value, damage, element, role, material, handedness):
        super(Melee, self).__init__(name, damage, element, role, material, value)
        self.handedness = handedness


class Shield(Melee):
    def __init__(self, name, damage, element, role, material, value, damage_block):
        super(Shield, self).__init__(name, damage, element, role, material, value, 1)
        self.damage_negation = damage_block


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


class Ranged(Weapon):
    def __init__(self, name, value, damage, element, role, material, ammo_type, weapon_range, fire_rate):
        super(Ranged, self).__init__(name, value, damage, element, role, material)
        self.ammo_type = ammo_type
        self.weapon_range = weapon_range
        self.fire_rate = fire_rate


class Throwable(Ranged):
    def __init__(self, name, value, damage, material, weapon_range, fire_rate):
        super(Throwable, self).__init__(name, value, damage, None, None, material, None, weapon_range, fire_rate)


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


class Character(object):
    def __init__(self, name, health, weapon, starting_location, helmet, chestplate, pants, boots):
        self.name = name
        self.health = health
        self.weapon = weapon
        self.inventory = []
        self.current_location = starting_location
        self.helmet = helmet
        self.chestplate = chestplate
        self.pants = pants
        self.boots = boots

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0

    def attack(self, target):
        print("%s attacks %s for %d damage" % (self.name, target.name, self.weapon.damage))
        target.take_damage(self.weapon.damage)
        print("%s has %d health left" % (target.name, target.health))

    def move(self, new_location):
        """This method moves a character to a new location

        :param new_location: The variable containing a room object
        """
        self.current_location = new_location

    def status_check(self):
        try:
            print("HP: %d " % self.health)
            print("Weapon: %s " % self.weapon.name)
            print(self.inventory_check())
            print("Helmet: %s" % self.helmet.name)
            print("Chestplate: %s" % self.chestplate.name)
            print("Pants: %s" % self.pants.name)
            print("Boots: %s" % self.boots.name)
        except AttributeError:
            print("%s" % 'None')

    def inventory_check(self):
        try:
            if len(self.inventory) == 0:
                raise IndexError
            elif len(self.inventory) > 1:
                print("Inventory: [", end="")
            else:
                print("Inventory: [", end="")
            for item_index in range(len(self.inventory) - 1):
                print(self.inventory[item_index].name, end=", ")
            print(self.inventory[len(self.inventory) - 1].name + "]")
        except IndexError:
            print("You have nothing in your inventory.")


# Items
# ======================================================================================================================
Meteor_Rod = Magic("Meteor Rod", 1000, 24, "Earth", "Mage", "Moon_Rock", 3, 2, 5, "Meteor")

RPG = RocketLauncher("RPG", 1000, 50, "Fire", "Demo", "Iron", "Rockets", 3, 2, .5)
Zeus = Gun("Zeus", 50, 12, "Electricity", "Ranged", "Iron", "Electric_Bullet", 5, 30, 5)
V_Power = Bow("rewoP_V", 3000, 67, None, "Ranged", "Wood", "Arrows", 6, 1)
Caltrops = Throwable("Spikes", 50, 5, "Iron", 1, 5)
Karyst = Dagger("Karyst", 0, 34, "Toxin", "Assassin", "Moon_Rock", 35)
Matterbul = Whip("Materbul", 1700, 43, None, None, "Leather", 8)
Maciella = Mace("Maciella", 2500, 70, None, None, "Cobalt", 2)
Repulsor = Sword("Repulsor", 5000, 167, None, "Knight", "Dark Steel", "Longsword", 1)
Stanford = Shield("Stanford", 15, None, "Knight", "Tin", 500, 10)
Health_Potion = Potions("Health Pot", 50, "1", 50, 10)
Cake = Food("Cake", 100, 5, "Well Fed", 15)
Wood_Helmet = Helmet("Wood Helmet", 250, 25, "Wood")
Iron_Chest = ChestPlate("Iron_Chest", 600, 100, "Iron")
Gold_Leggings = Leggings("Gold Leggings", 500, 75, "Gold")
Diamond_Slides = Boots("Diamond Slides", 1500, 1500, "Diamond")
Generic_Sword = Sword("Iron Sword", 500, 12, None, None, None, 'Longsword', '2')
Death_Food = Food("Food", 0, 1, None, -100)


# Characters
# ======================================================================================================================
Big_Scary_Man = Character("Big Scary Man", 100, Generic_Sword, None, None, None, None, None)
Kyle = Character("Kyle", 100, Generic_Sword, None, None, None, None, None)

# Rooms
# ======================================================================================================================
MAIN_DRIVEWAY = Room("Main Driveway", 'HOUSE_GARAGE', None, None, None, None, None,
                     "You're outside. To the North is a slightly opened Garage.", [],
                     [RPG])
HOUSE_GARAGE = Room("Garage", 'WASHING_ROOM', 'MAIN_DRIVEWAY', None, None, None, None, "North of you is a door."
                    "The first thing you notice in the Garage is the keys.")
WASHING_ROOM = Room("Washing Room", 'DOWNSTAIRS_HALLWAY', 'HOUSE_GARAGE', None, None, None, None,
                    "There's a dryer and washing machine. Nearby a cabinet is open.", [Big_Scary_Man, Kyle], [])
DOWNSTAIRS_HALLWAY = Room("Downstairs Hallway", 'MONIQUE_ROOM', 'WASHING_ROOM', 'DOWNSTAIRS_HALLWAY_CONT',
                          'KENDRICK_ROOM', None, None, "You're in a hallway. There's an old painting on the wall. "
                                                       "There's a door to your left. The hallway continues West.")
KENDRICK_ROOM = Room("Kendrick's Room", None, None, 'DOWNSTAIRS_HALLWAY', None, None, None,
                     "The room looks normal, but the wooden floors creak.")
MONIQUE_ROOM = Room("Monique's Room", None, 'DOWNSTAIRS_HALLWAY_CONT', None, None, None, None,
                    "You came through the wall. There'" + 's' + "and old keycard with 2581 printed on it.")
DOWNSTAIRS_HALLWAY_CONT = Room("Downstairs Hallway", 'MONIQUE_ROOM', 'DOWNSTAIRS_BATHROOM', 'DOWNSTAIRS_LIVING_ROOM',
                               'DOWNSTAIRS_HALLWAY', None, None,
                               "You're still in the hallway. There is a room in front and behind you.")
DOWNSTAIRS_BATHROOM = Room("Downstairs Bathroom", 'DOWNSTAIRS_HALLWAY_CONT', None, None, None, None, None,
                           "It smells really bad.")
DOWNSTAIRS_LIVING_ROOM = Room("Downstairs Living Room", None, 'DOWNSTAIRS_STAIRWELL', 'DINING_ROOM',
                              'DOWNSTAIRS_HALLWAY_CONT', None, None, "You're in a Living Room.")
DINING_ROOM = Room("Dining Room", None, 'KITCHEN', None, 'DOWNSTAIRS_LIVING_ROOM', None, None,
                   "There's fresh food lying on the table!", [], [Death_Food])
KITCHEN = Room("Kitchen", 'DINING_ROOM', None, None, None, None, None,
               "Here lies more food. A few fruits and raw fish. There's a knife.", [], [])
DOWNSTAIRS_STAIRWELL = Room("Downstairs Stairwell", 'DOWNSTAIRS_LIVING_ROOM', None, None, None, 'UPSTAIRS_STAIRWELL',
                            None, "The stairwell leads up.")
UPSTAIRS_STAIRWELL = Room("Upstairs Stairwell", 'UPSTAIRS_HALLWAY', None, None, None, None, 'DOWNSTAIRS_STAIRWELL',
                          )
UPSTAIRS_HALLWAY = Room("Main Upstairs Hallway", 'MASTER_BED_ROOM', 'UPSTAIRS_STAIRWELL',
                        'UPSTAIRS_HALLWAY_CONT', 'UPSTAIRS_LIVING_ROOM', None, None,
                        "To the East is a Living Room. Two double doors present themselves "
                        "in the North. The hallway continues East.")
UPSTAIRS_LIVING_ROOM = Room("Upstairs Living Room", None, None, 'UPSTAIRS_HALLWAY', None, None, None,
                            "There's 2 monitors and a computer on the desk. It is off.")
MASTER_BED_ROOM = Room("Master Bedroom", 'MASTER_BALCONY', 'UPSTAIRS_HALLWAY', None, 'MASTER_HALLWAY',
                       "The room is quite large. The room is thoroughly decorated with pictures. North is a door."
                       " East is a hallway.")
MASTER_BALCONY = Room("Balcony", None, 'MASTER_BED_ROOM', None, None, None, None,
                      "You get a better view of the surroundings from up here.", [])
MASTER_HALLWAY = Room("Master Hallway", 'MASTER_NORTH_CLOSET', 'MASTER_SOUTH_CLOSET', None,
                      'MASTER_BATHROOM', "North is a door, to the South is another door. The East door is open.")
MASTER_NORTH_CLOSET = Room("North Closet", None, 'MASTER_HALLWAY', None, None, None, None,
                           "You're in a closet. It has clothes hung up.")
MASTER_SOUTH_CLOSET = Room("South Closet", 'MASTER_NORTH_CLOSET', None, None, None, None, None,
                           "There's a box with blinking lights in the room.")
MASTER_BATHROOM = Room("Master Bathroom", None, None, 'MASTER_HALLWAY', None, None, None,
                       "A shower and bath is visible. The water is running.")
UPSTAIRS_HALLWAY_CONT = Room("Eastern Upstairs Hallway", 'UPSTAIRS_HALLWAY_NORTH', None, 'KENNY_ROOM',
                             'UPSTAIRS_HALLWAY', None, None, "East lies an unopened door. North continues the hallway.")
UPSTAIRS_HALLWAY_NORTH = Room("North Upstairs Hallway", 'LILIE_ROOM', 'UPSTAIRS_HALLWAY_CONT', 'UPSTAIRS_BATHROOM',
                              None, None, None, "There's a doors leading to the North and East.")
UPSTAIRS_BATHROOM = Room("Upstairs Bathroom", None, None, None, 'UPSTAIRS_HALLWAY_NORTH', None, None,
                         "The water to the sink and bath is turned on.")
LILIE_ROOM = Room("Lilie's Room", None, 'UPSTAIRS_HALLWAY_NORTH', None, None, None, None, "A barren room with a bed.")
KENNY_ROOM = Room("Kenny's Room", None, None, 'UPSTAIRS_HALLWAY_CONT', None, None, None, "The room has a foul stench.",
                  [], [RPG])
# Player ===============================================================================================================
Player = Character('Paper', 100, Karyst, MAIN_DRIVEWAY, None, None, None, None)
# Controller ===========================================================================================================

command_list = ['north', 'south', 'east', 'west', 'up', 'down']
short_directions = ['n', 's', 'e', 'w', 'u', 'd']
playing = True
tutorial_state = False
while playing:
    # Tutorial Check ===================================================================================================

    while tutorial_state is False:
        player_command = input("Do you want a tutorial?")
        if 'yes' in player_command.lower():
            tutorial_state = True
            print("This is a text-based adventure game.")
            print("To move around, you can type in the 4 cardinal directions: North, South, East, and West. \n"
                  "You're able to shorten the movement to the first letter of the directions.")
            print("Typing in 'status' in the commandline will present you all your statistics.")
        else:
            tutorial_state = True
            print("You may play the game.")
    # Location Check ===================================================================================================
    print()
    print(Player.current_location.name)
    print(Player.current_location.description)
    # Item Check =======================================================================================================
    if len(Player.current_location.items) > 0:
        items_index = 0

        while items_index < len(Player.current_location.items):
            print()
            print("There is a %s in this room." % Player.current_location.items[items_index].name)
            print()
            choice = input("Do you want to pick this item up?")
            if choice.lower() in "yes":
                print()
                print("You've picked up the %s." % Player.current_location.items[items_index].name)
                Player.inventory.append(Player.current_location.items[items_index])
                Player.current_location.items.remove(Player.current_location.items[items_index])
                Player.inventory_check()
                if Death_Food in Player.inventory:
                    print("You've died from eating the poisoned food.")
                    Player.health = 0
                    playing = False
            else:
                print()
                print("You decide to not pick the item up.")
                print()
                print(Player.current_location.name)
                print(Player.current_location.description)
                items_index += 1

    # Combat Check =====================================================================================================
    if len(Player.current_location.character) > 0:
        for character in Player.current_location.character:
            while (character.health > 0 or Player.health == 0) and not Player.current_location.escape:
                print()
                choice = input("There's a monster here! Do you wish to fight it or run? Yes or No?")
                print()
                if choice in command_list:
                    print("There's still a Monster in the room!")
                elif choice.lower() in ['yes']:
                    print("You've decided to fight the monster!")
                    print()
                    for x in Player.current_location.character:
                        Player.attack(x)
                        print()
                        x.attack(Player)
                        if x.health == 0:
                            print("You've successfully slain this monster!")
                            print()
                            print(Player.current_location.name)
                            print(Player.current_location.description)
                        if Player.health == 0:
                            print("You've died.")
                elif choice.lower() in ['no']:
                    chance = random.randint(0, 1)
                    if chance == 0:
                        print("You tried to run, but it blocked the door!")
                        print()
                        print("You now have to fight it!")
                        for x in Player.current_location.character:
                            Player.attack(x)
                            print()
                            x.attack(Player)
                            if character.health == 0:
                                print("You've successfully slain all the monsters!")
                            if Player.health == 0:
                                print("You've died.")
                    else:
                        print("You successfully escape")
                        Player.current_location.escape = True
                        print()
                        print(Player.current_location.name)
                        print(Player.current_location.description)
    # Movement & Command Input =========================================================================================
    player_command = input(">_")
    if player_command.lower() in short_directions:
        pos = short_directions.index(player_command.lower())
        player_command = command_list[pos]
    elif 'use' in player_command.lower():
        key_str = player_command[6:]
        item = None
        for thing in Player.inventory:
            if thing.name.lower() == key_str.lower():
                item = thing
            if isinstance(item, Potions):
                Player.health = item.heal_amount + Player.health
                if Player.health > 100:
                    Player.health = 100
    elif 'status' in player_command.lower():
        Player.status_check()
    elif 'drop' in player_command.lower():
        key_str = player_command[5:]
        Player.inventory_check()
        Player.current_location.items.append(player_command)
        Player.inventory.remove(player_command)
    elif 'equip' in player_command.lower():
        key_str = player_command[6:]
        item = None
        for thing in Player.inventory:
            if thing.name.lower() == key_str.lower():
                item = thing
        if isinstance(item, Weapon):
            Player.weapon = item
            print("Equipped %s" % Player.weapon.name)
        if isinstance(item, Helmet):
            Player.helmet = item
            print("Equipped %s" % Player.helmet.name)
        if isinstance(item, ChestPlate):
            Player.chestplate = item
            print("Equipped %s" % Player.chestplate.name)
        if isinstance(item, Leggings):
            Player.pants = item
            print("Equipped %s" % Player.pants.name)
        if isinstance(item, Boots):
            Player.boots = item
            print("Equipped %s" % Player.boots.name)
    elif player_command.lower() in ['inventory', 'check inventory']:
        Player.inventory_check()
    elif player_command.lower() in ['q', 'quit', 'exit']:
        playing = False
    elif player_command.lower() in command_list:
        try:
            room_name = getattr(Player.current_location, player_command)
            room_object = globals()[room_name]
            Player.move(room_object)
        except AttributeError:
            print("I can't go that way.")
        except KeyError:
            print("This key does not exist.")
    else:
        print("Command Not Recognized.")
