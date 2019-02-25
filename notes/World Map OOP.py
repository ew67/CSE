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

# Option 1
# Add dependent rooms after


R19A = Room("R19A")
parking_lot = Room('The Parking Lot', None, R19A)

R19A.north = parking_lot

# Option 2
# Put them in quotes

R19A = Room("R19A", 'parking_lot')
parking_lot = Room('The Parking Lot', None, 'R19A')


MAIN_DRIVEWAY = Room("Main Driveway", 'HOUSE_GARAGE', None, None, None, None, None,
                     "You're outside. There are cars in front of you. The garage is slightly opened.")
HOUSE_GARAGE = Room("Garage", 'WASHING_ROOM', MAIN_DRIVEWAY, None, None, None, None, "The garage is empty.")
WASHING_ROOM = Room("Washing Room", 'DOWNSTAIRS_HALLWAY', HOUSE_GARAGE, None, None, None, None,
                    "There's a dryer and washing machine. Nearby a cabinent is open.")
DOWNSTAIRS_HALLWAY = Room("Downstairs Hallway", 'MONIQUE_ROOM', WASHING_ROOM, 'DOWNSTAIRS_HALLWAY_CONT',
                          'KENDRICK_ROOM', None, None, "You're in a hallway. There's an old painting on the wall. "
                                                       "There's a door to your left. The hallway continues West.")
KENDRICK_ROOM = Room("Kendrick's Room", None, None, DOWNSTAIRS_HALLWAY, None, None, None, "The room looks normal, but "
                                                                                          "the wooden floors creak.")
MONIQUE_ROOM = Room("Monique's Room", None, 'DOWNSTAIRS_HALLWAY_CONT', None, None, None, None,
                    "You came through the wall. There'" + 's' + "and old keycard with 2581 printed on it.")
DOWNSTAIRS_HALLWAY_CONT = Room("Downstairs Hallway", MONIQUE_ROOM, 'DOWNSTAIRS_BATHROOM', 'DOWNSTAIRS_LIVING_ROOM',
                               DOWNSTAIRS_HALLWAY, None, None,
                               "You're still in the hallway. There is a room in front and behind you.")
DOWNSTAIRS_BATHROOM = Room("Downstairs Bathroom", DOWNSTAIRS_HALLWAY_CONT, None, None, None, None, None,
                           "It smells really bad.")
DOWNSTAIRS_LIVING_ROOM = Room("Downstairs Living Room", None, 'STAIRWELL', 'DINING_ROOM', DOWNSTAIRS_HALLWAY_CONT, None,
                              None, "You're in a Living Room.")
DINING_ROOM = Room("Dining Room", None, 'KITCHEN', None, DOWNSTAIRS_LIVING_ROOM, None, None, "There's fresh food "
                                                                                             "lying on the table!")
KITCHEN = Room("Kitchen", DINING_ROOM, None, None, None, None, None, "Here lies more food. A few fruits and raw fish. "
                                                                     "There's a knife. ")
DOWNSTAIRS_STAIRWELL = Room("Downstairs Stairwell", DOWNSTAIRS_LIVING_ROOM, None, None, None, 'UPSTAIRS_STAIRWELL')
UPSTAIRS_STAIRWELL = Room("Upstairs Stairwell", 'UPSTAIRS_HALLWAY', None, None, None, None, DOWNSTAIRS_STAIRWELL)
UPSTAIRS_HALLWAY = Room("Main Upstairs Hallway", 'MASTER_BED_ROOM', UPSTAIRS_STAIRWELL,
                        'UPSTAIRS_HALLWAY_CONT', 'UPSTAIRS_LIVING_ROOM')
UPSTAIRS_LIVING_ROOM = Room("Upstairs Living Room", None, None, UPSTAIRS_HALLWAY)
MASTER_BED_ROOM = Room("Master Bedroom", 'MASTER_BALCONY', UPSTAIRS_HALLWAY, None, 'MASTER_HALLWAY')
MASTER_BALCONY = Room("Upstairs Balcony", None, MASTER_BED_ROOM)
MASTER_HALLWAY = Room("Master Hallway", 'MASTER_NORTH_CLOSET', 'MASTER_SOUTH_CLOSET', None, 'MASTER_BATHROOM')
MASTER_NORTH_CLOSET = Room("North Closet", None, MASTER_HALLWAY)
MASTER_SOUTH_CLOSET = Room("South Closet", MASTER_NORTH_CLOSET)
MASTER_BATHROOM = Room("Master Bathroom", None, None, MASTER_HALLWAY)
UPSTAIRS_HALLWAY_CONT = Room("East Upstairs Hallway", 'UPSTAIRS_HALLWAY_NORTH', None, None, UPSTAIRS_HALLWAY)
UPSTAIRS_HALLWAY_NORTH = Room("North Upstairs Hallway", 'LILIE_ROOM', UPSTAIRS_HALLWAY_CONT, 'UPSTAIRS_BATHROOM')
LILIE_ROOM = Room("Lilie's Room", None, UPSTAIRS_HALLWAY_NORTH)
