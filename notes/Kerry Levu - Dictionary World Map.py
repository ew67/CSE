world_map = {
    'MAIN_DRIVEWAY': {
        'NAME': 'Kerry' + "'s" + " Driveway",
        'DESCRIPTION': "This the classroom that you are in right"
                       " now. It has two exits to the north side.",
        'PATHS': {
            'NORTH': "HOUSE_GARAGE"

        }
    },
    'HOUSE_GARAGE': {
        'NAME': "Kerry's Garage",
        'DESCRIPTION': "These are cars parked here. To the south is Mr. Wiebe's room",
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
        'DESCRIPTION': "You're in a hallway. There's an old painting on the wall.",
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