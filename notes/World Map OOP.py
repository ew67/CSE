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


MAIN_DRIVEWAY = Room("Main Driveway", 'HOUSE_GARAGE')
HOUSE_GARAGE = Room("Garage", 'WASHING_ROOM', MAIN_DRIVEWAY)
WASHING_ROOM = Room("Washing Room", 'DOWNSTAIRS_HALLWAY', HOUSE_GARAGE)
DOWNSTAIRS_HALLWAY = Room("Downstairs Hallway", 'MONIQUE_ROOM', WASHING_ROOM, 'DOWNSTAIRS_HALLWAY_CONT',
                          'KENDRICK_ROOM')
KENDRICK_ROOM = Room("Kendrick's Room", None, None, DOWNSTAIRS_HALLWAY)
MONIQUE_ROOM = Room("Monique's Room", None, 'DOWNSTAIRS_HALLWAY_CONT')
DOWNSTAIRS_HALLWAY_CONT = Room("Downstairs Hallway", MONIQUE_ROOM, 'DOWNSTAIRS_BATHROOM', 'DOWNSTAIRS_LIVING_ROOM',
                               DOWNSTAIRS_HALLWAY)
DOWNSTAIRS_BATHROOM = Room("Downstairs Bathroom", DOWNSTAIRS_HALLWAY_CONT)
DOWNSTAIRS_LIVING_ROOM = Room("Downstairs Living Room", None, 'STAIRWELL', 'DINING_ROOM', DOWNSTAIRS_HALLWAY_CONT)
DINING_ROOM = Room("Dining Room", None, 'KITCHEN', None, DOWNSTAIRS_LIVING_ROOM)
DOWNSTAIRS_STAIRWELL = Room("Downstairs Stairwell", DOWNSTAIRS_LIVING_ROOM, None, None, None, 'UPSTAIRS_STAIRWELL')
UPSTAIRS_STAIRWELL = Room("Upstairs Stairwell", 'UPSTAIRS_HALLWAY', None, None, None, None, DOWNSTAIRS_STAIRWELL)
UPSTAIRS_HALLWAY = Room("Main Upstairs Hallway", 'MASTER_BED_ROOM', UPSTAIRS_STAIRWELL,
                        'UPSTAIRS_HALLWAY_CONT', 'UPSTAIRS_LIVING_ROOM')
UPSTAIRS_LIVING_ROOM = Room("Upstairs Living Room", None, None, UPSTAIRS_HALLWAY)
MASTER_BED_ROOM = Room("Master Bedroom", 'MASTER_BALCONY', UPSTAIRS_HALLWAY, None, 'MASTER_HALLWAY')
MASTER_HALLWAY = Room("Master Hallway", 'North Closet' )
UPSTAIRS_HALLWAY_CONT