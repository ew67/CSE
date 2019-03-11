world_map = {
    'MAIN_DRIVEWAY': {
        'NAME': 'Kerry' + "'s" + " Driveway",
        'DESCRIPTION': "You're outside. There are cars in front of you. The garage is slightly opened.",
        'PATHS': {
            'NORTH': "HOUSE_GARAGE"

        }
    },
    'HOUSE_GARAGE': {
        'NAME': "Kerry's Garage",
        'DESCRIPTION': "The garage is empty.",
        'PATHS': {
            'SOUTH': 'MAIN_DRIVEWAY',
            'NORTH': 'WASHING_ROOM'
        }

    },
    'WASHING_ROOM': {
        'NAME': "Kerry's Washing Room",
        'DESCRIPTION': "There's a dryer and washing machine. Nearby a cabinet is open.",
        'PATHS': {
            'SOUTH': 'HOUSE_GARAGE',
            'NORTH': 'DOWNSTAIRS_HALLWAY'
        }
    },
    'DOWNSTAIRS_HALLWAY': {
        'NAME': 'Hallway',
        'DESCRIPTION': "You're in a hallway. There's an old painting on the wall."
                       " There's a door to your left. The hallway continues west.",
        'PATHS': {
            'WEST': "KENDRICK'S_ROOM",
            'EAST': 'DOWNSTAIRS_HALLWAY_CONT',
            'SOUTH': 'WASHING_ROOM',

        }
    },
    'DOWNSTAIRS_HALLWAY_CONT': {
        'NAME': "Hallway",
        'DESCRIPTION': "You're still in the hallway. There is a room in front and behind you.",
        'PATHS': {
            'NORTH': "MONIQUE'S_ROOM",
            'SOUTH': "DOWNSTAIRS_BATHROOM",
            'EAST': 'DOWNSTAIRS_LIVING_ROOM',

        }

    },
    "KENDRICK'S_ROOM": {
        'NAME': "Kendrick's Room",
        'DESCRIPTION': "The room looks normal, but the wooden floors creak.",
        'PATHS': {
            'EAST': 'DOWNSTAIRS_HALLWAY',
            'DOWN': 'BASEMENT'
        }

    },
    "MONIQUE'S_ROOM": {
        'NAME': "Monique's Room",
        'DESCRIPTION': 'You came through the wall. There' + 's' + "and old keycard with 2581 printed on it.",
        'PATHS': {
            'SOUTH': 'DOWNSTAIRS_HALLWAY_CONT',
            'WEST': 'DOWNSTAIRS_HALLWAY'
        }
    },
    'DOWNSTAIRS_BATHROOM': {
        'NAME': 'Downstairs Bathroom',
        'DESCRIPTION': "It smells really bad. ",
        'PATHS': {
            'NORTH': 'DOWNSTAIRS_HALLWAY_CONT',

        }
    },
    'DOWNSTAIRS_LIVING_ROOM': {
        'NAME': 'Living Room',
        'DESCRIPTION': "You're in a Living Room.",
        'PATHS': {
            'WEST': "DOWNSTAIRS_HALLWAY_CONT",
            'SOUTH': 'DOWNSTAIRS_STAIRWELL',
            'EAST': 'DINING_ROOM'


        }

    },
    'DINING_ROOM': {
        'NAME': 'Dining Room',
        'DESCRIPTION': "There's fresh food lying on the table!",
        'PATHS': {
            'SOUTH': 'KITCHEN',
            'WEST': 'DOWNSTAIRS_LIVING_ROOM',
        }

    },
    'KITCHEN': {
        'NAME': 'Kitchen',
        'DESCRIPTION': "Here lies more food. A few fruits and raw fish. There's a knife.",
        'PATHS': {
            'NORTH': 'DINING_ROOM',
        }

    },
    'DOWNSTAIRS_STAIRWELL': {
        'NAME': 'Downstairs Stairwell',
        'DESCRIPTION': "The stairwell leads up.",
        'PATHS': {
            'UP': 'UPSTAIRS_STAIRWELL',
        }

    },
    'UPSTAIRS_STAIRWELL': {
        'NAME': 'Upstairs Stairwell',
        'DESCRIPTION': 'You reach the top of the stairwell.',
        'PATHS': {
            'NORTH': 'UPSTAIRS_MAIN_HALLWAY',
            'DOWN': 'DOWNSTAIRS_STAIRWELL',

        }

    },
    'UPSTAIRS_MAIN_HALLWAY': {
        'NAME': "Upstairs Hallway",
        'DESCRIPTION': "To the East is a Living Room. Two double doors present themselves in the North."
                       "The hallway continues East.",
        'PATHS': {
            'NORTH': 'MASTER_BED_ROOM',
            'WEST': 'UPSTAIRS_LIVING_ROOM',
            'EAST': 'UPSTAIRS_HALLWAY_CONT',
            'SOUTH': 'UPSTAIRS_STAIRWELL',
        }

    },
    'UPSTAIRS_LIVING_ROOM': {
        'NAME': "Upstairs Living Room",
        'DESCRIPTION': "There's 2 monitors and a computer on the desk. It is off.",
        'PATHS': {
            'EAST': 'UPSTAIRS_MAIN_HALLWAY'
        }
    },
    'MASTER_BED_ROOM': {
        'NAME': 'Master Bedroom',
        'DESCRIPTION': "The room is quite large. The room is thoroughly decorated with pictures. North is a door."
                       " East is a hallway.",
        'PATHS': {
            'NORTH': 'MASTER_BALCONY',
            'WEST': "MASTER_HALLWAY",
            'SOUTH': 'UPSTAIRS_MAIN_HALLWAY'
        }

    },
    'MASTER_BALCONY': {
        'NAME': 'Master Balcony',
        'DESCRIPTION': 'You get a better view of the surroundings from up here.',
        'PATHS': {
            'SOUTH': 'MASTER_BED_ROOM'
        }

    },

    'UPSTAIRS_HALLWAY_CONT': {
        'NAME': "Eastern Upstairs Hallway",
        'DESCRIPTION': "East lies an unopened door. North continues the hallway.",
        'PATHS': {
            'WEST': 'UPSTAIRS_MAIN_HALLWAY',
            'EAST': 'UPSTAIRS_KENNY_ROOM',
            'NORTH': 'UPSTAIRS_HALLWAY_NORTH',
        }

    },
    'MASTER_HALLWAY': {
        'NAME': 'Master Hallway',
        'DESCRIPTION': 'North is a door, to the South is another door. The East door is open.',
        'PATHS': {
            'NORTH': 'MASTER_NORTH_CLOSET',
            'EAST': 'MASTER_BED_ROOM',
            'WEST': 'MASTER_BATHROOM',
            'SOUTH': 'MASTER_SOUTH_CLOSET',
        }

    },
    'MASTER_NORTH_CLOSET': {
        'NAME': 'Master North Closet',
        'DESCRIPTION': "You're in a closet. It has clothes hung up.",
        'PATHS': {
            'SOUTH': "MASTER_HALLWAY"
        }

    },
    'MASTER_SOUTH_CLOSET': {
        'NAME': 'Master South Closet',
        'DESCRIPTION': "There's a box with blinking lights in the room.",
        'PATHS': {
            'NORTH': 'MASTER_HALLWAY'
        }

    },
    'MASTER_BATHROOM': {
        'NAME': 'Master Bathroom',
        'DESCRIPTION': 'The water to the sink and bath is turned on.',
        'PATHS': {
            "EAST": 'MASTER_HALLWAY'
        }

    },
    'UPSTAIRS_HALLWAY_NORTH': {
        'NAME': 'Northern Upstairs Hallway',
        'DESCRIPTION': "There's a doors leading to the North and East.",
        'PATHS': {
            'NORTH': 'UPSTAIRS_LILIE_ROOM',
            'SOUTH': 'UPSTAIRS_HALLWAY_CONT',
            'EAST': 'UPSTAIRS_BATHROOM',
        }

    },
    'UPSTAIRS_BATHROOM': {
        'NAME': "Upstairs Bathroom",
        'DESCRIPTION': "The water to the sink and bath is turned on.",
        'PATHS': {
            'WEST': 'UPSTAIRS_HALLWAY_NORTH'

        }
    },
    'UPSTAIRS_KENNY_ROOM': {
        'NAME': "Kenny's Room",
        'DESCRIPTION': "The room has a foul stench.",
        'PATHS': {
            'WEST': 'UPSTAIRS_HALLWAY_CONT'
        }

    },
    'UPSTAIRS_LILIE_ROOM': {
        'NAME': "Lilie's Room",
        'DESCRIPTION': 'A barren room with a bed.',
        'PATHS': {
            'SOUTH': 'UPSTAIRS_HALLWAY_NORTH'
        }

    },
}


# Other Variables

current_node = world_map['MAIN_DRIVEWAY']
directions = ["NORTH", "SOUTH", "EAST", "WEST", "UP", "DOWN", "N", ]
playing = True

# Controller
while playing:
    print()
    print(current_node["NAME"])
    print(current_node['DESCRIPTION'])
    command = input(">_")
    if command.lower() in ['q', 'quit', 'exit']:
        playing = False
    elif command.upper() in directions:
        try:
            room_name = current_node['PATHS'][command.upper()]
            current_node = world_map[room_name]
        except KeyError:
            print("I can't go that way.")
    else:
        print("Command Not Recognized.")
