class Room(object):
    def __init__(self, name, north=None, south=None, east=None, west=None, up=None, down=None, description=""):
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.up = up
        self.down = down
        self.description = description
        self.character = []


class Monster(object):
    def __init__(self, starting_location):
        self.health = 100
        self.current_location = starting_location


class Player(object):
    def __init__(self, starting_location):
        self.health = 100
        self.current_location = starting_location
        self.inventory = []

    def move(self, new_location):
        """This method moves a character to a new location

        :param new_location: The variable containing a room object
        """
        self.current_location = new_location


# Option 1
# Add dependent rooms after


R19A = Room("R19A")
parking_lot = Room('The Parking Lot', None, R19A)

R19A.north = parking_lot

# Option 2
# Put them in quotes

R19A = Room("R19A", 'parking_lot')
parking_lot = Room('The Parking Lot', None, 'R19A')
playing = True

MAIN_DRIVEWAY = Room("Main Driveway", 'HOUSE_GARAGE', None, None, None, None, None,
                     "You're outside. There are cars in front of you. The garage is slightly opened.")
HOUSE_GARAGE = Room("Garage", 'WASHING_ROOM', 'MAIN_DRIVEWAY', None, None, None, None, "The garage is empty.")
WASHING_ROOM = Room("Washing Room", 'DOWNSTAIRS_HALLWAY', 'HOUSE_GARAGE', None, None, None, None,
                    "There's a dryer and washing machine. Nearby a cabinet is open.")
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
                   "There's fresh food lying on the table!")
KITCHEN = Room("Kitchen", 'DINING_ROOM', None, None, None, None, None,
               "Here lies more food. A few fruits and raw fish. There's a knife.")
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
MASTER_BALCONY = Room("Upstairs Balcony", None, 'MASTER_BED_ROOM', None, None, None, None,
                      "You get a better view of the surroundings from up here.")
MASTER_HALLWAY = Room("Master Hallway", 'MASTER_NORTH_CLOSET', 'MASTER_SOUTH_CLOSET', None,
                      'MASTER_BATHROOM', "North is a door, to the South is another door. The East door is open.")
MASTER_NORTH_CLOSET = Room("North Closet", None, 'MASTER_HALLWAY', None, None, None, None,
                           "You're in a closet. It has clothes hung up.")
MASTER_SOUTH_CLOSET = Room("South Closet", 'MASTER_NORTH_CLOSET', None, None, None, None, None,
                           "There's a box with blinking lights in the room.")
MASTER_BATHROOM = Room("Master Bathroom", None, None, 'MASTER_HALLWAY', None, None, None,
                       "A shower and bath is visible. The water is running.")
UPSTAIRS_HALLWAY_CONT = Room("Eastern Upstairs Hallway", 'UPSTAIRS_HALLWAY_NORTH', None, None, 'UPSTAIRS_HALLWAY',
                             None, None, "East lies an unopened door. North continues the hallway.")
UPSTAIRS_HALLWAY_NORTH = Room("North Upstairs Hallway", 'LILIE_ROOM', 'UPSTAIRS_HALLWAY_CONT', 'UPSTAIRS_BATHROOM',
                              None, None, None, "There's a doors leading to the North and East.")
UPSTAIRS_BATHROOM = Room("Upstairs Bathroom", None, None, None, 'UPSTAIRS_HALLWAY_NORTH', None, None,
                         "The water to the sink and bath is turned on.")
LILIE_ROOM = Room("Lilie's Room", None, 'UPSTAIRS_HALLWAY_NORTH', None, None, None, None, "A barren room with a bed.")
KENNY_ROOM = Room("Kenny's Room", None, None, 'UPSTAIRS_HALLWAY_CONT', None, None, None, "The room has a foul stench.")

player = Player(MAIN_DRIVEWAY)
Big_Scary_Man = Monster(DOWNSTAIRS_STAIRWELL)

directions = ['north', 'south', 'east', 'west', 'up', 'down']

while playing:
    print()
    print(player.current_location.name)
    print(player.current_location.description)
    command = input(">_")
    if command.lower() in ['q', 'quit', 'exit']:
        playing = False
    elif command.lower() in directions:
        try:
            # command = 'north'
            room_name = getattr(player.current_location, command)
            room_object = globals()[room_name]
            player.move(room_object)
        except AttributeError:
            print("I can't go that way.")
        except KeyError:
            print("This key does not exist.")
    else:
        print("Command Not Recognized.")
