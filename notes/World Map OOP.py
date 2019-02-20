class Room(object):
    def __init__(self, name, north=None, south=None, east=None, west=None, description=""):
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.west = west
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
DOWNSTAIRS_HALLWAY = Room("Downstairs Hallway", 'MONIQUE_ROOM', WASHING_ROOM, 'DOWNSTAIRS_HALLWAY_CONT', 'KENDRICK_ROOM')
KENDRICK_ROOM = Room("Kendrick's Room", None, None, DOWNSTAIRS_HALLWAY)