world_map = {
    'R19A': {
        'NAME': "Wiebe's Classroom",
        'DESCRIPTION': "This the classroom that you are in right"
                       " now. It has two exits to the north side.",
        'PATHS': {
            'NORTH': "PARKING_LOT"

        }
    },
    'PARKING_lOT': {
        'NAME': "The Edison Parking Lot",
        'DECSCRIPTION': "These are cars parked here. To "
                        "the south is Mr. Wiebe's room",
        'PATHS': {
            'SOUTH': 'R19A'
        }

    }
}



