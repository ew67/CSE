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
                       "There's a door to your left. The hallway continues west.",
        'PATHS': {
            'WEST': "KENDRICK_ROOM",
            'EAST': 'DOWNSTAIRS_HALLWAY_CONT',

        }
    },
    'DOWNSTAIRS_HALLWAY_CONT': {
        'NAME': "Hallway",
        'DESCRIPTION': "You're still in the hallway. There is a room on your left and right.",
        'PATHS': {
            'NORTH': "Monique's Room",
            'SOUTH': "Downstair's Bathroom",
            'EAST': 'Living Room',

        }

    },
    "KENDRICK'S ROOM": {
        'NAME': "Kendrick's Room",
        'DESCRIPTION': "The room looks normal, but the wooden floors creak.",
        'PATHS': {
            'EAST': 'DOWNSTAIRS_HALLWAY',
            'DOWN': 'BASEMENT'
        }

    },
    "MONIQUE'S ROOM": {
        'NAME': "Monique's Room",
        'DESCRIPTION': 'You came through the wall. There' + 's' + "and old keycard with 2581 printed on them.",
        'PATHS': {

}
    },
    'DOWNSTAIRS_LIVING_ROOM': {

    },
    'DINING_ROOM': {

    },
    'KITCHEN': {

    },
    'STAIRWELL': {

    },
    'UPSTAIRS_STAIRWELL': {

    },
    'UPSTAIRS_MAIN_HALLWAY': {

    },
    'UPSTAIRS_LIVING_ROOM': {

    },
    'MASTER_BED_ROOM': {

    },
    'MASTER_HALLWAY': {

    },
    'MASTER_NORTH_CLOSET': {

    },
    'MASTER_SOUTH_CLOSET': {

    },
    'MASTER_BATHROOM': {

    },
    'UPSTAIRS_HALLWAY_EAST': {

    },
    'UPSTAIRS_BATHROOM': {

    },
    'UPSTAIRS_KENNY_ROOM': {

    },
    'UPSTAIRS_LILIE_ROOM': {

    }
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