world_map = {
    'MAIN_DRIVEWAY': {
        'NAME': 'Kerry' + "'s" + " Driveway",
        'DESCRIPTION': "This the classroom that you are in right"
                       " now. It has two exits to the north side.",
        'PATHS': {
            'NORTH': "PARKING_LOT"

        }
    },
    'HOUSE_GARAGE': {
        'NAME': "The Edison Parking Lot",
        'DECSCRIPTION': "These are cars parked here. To "
                        "the south is Mr. Wiebe's room",
        'PATHS': {
            'SOUTH': 'MAIN_DRIVEWAY'
        }

    }
}

# Other Variables

current_node = world_map['MAIN_DRIVEWAY']
directions = ["NORTH", "SOUTH", "EAST", "WEST", "UP", "DOWN", ]
playing = True

# Controller
while playing:
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
        print("Command Not Recognized.  ")


print(world_map['MAIN_DRIVEWAY']['DESCRIPTION'])
