# coordinate for target points
MAP_POINTS = {
    "Warehouse": [-10.26, 0.22],
    "ExitWarehouse": [-10.26, -9.64],
    "Hallway0": [-3.67, -9.64],

    "EntryR0": [-3.67, -3.1],
    "MiddleR0": [1.33, -3.1],
    "NearR0B0": [1.33, -4.12],
    "Room0Patient0": [3.74, -4.12],
    "BetweenR0B1B2": [1.33, -8],
    "Room0Patient1": [3.74, -8],
    "Room0Patient2": [-1.09, -8],

    "EntryR1": [-3.67, 5.78],
    "MiddleR1": [1.33, 5.78],
    "NearR1B0": [1.33, 4.71],
    "Room1Patient0": [3.74, 4.71],
    "BetweenR1B1B2": [1.33, 0.8],
    "Room1Patient1": [3.74, 0.8],
    "Room1Patient2": [-1.09, 0.8],

    "EntryR2": [-3.67, 16.11],
    "MiddleR2": [-1.0, 16.11],
    "Room2Patient0": [0.19, 16.11],
    "Room2Patient1": [-1.0, 20],
    "Room2Patient2": [3.79, 20],
    "EntryR2D1": [3.79, 14.13],

    "Hallway1": [-3.67, 14.13],

    "EntryR3": [14.0, 14.13],
    "MiddleR3": [14.0, 18.37],
    "NearR3B0": [10.29, 18.37],
    "Room3Patient0": [10.29, 20.85],
    "BetweenR3B1B2": [6.39, 18.37],
    "Room3Patient1": [6.39, 20.85],
    "Room3Patient2": [6.39, 16.41],

    "EntryR4": [-3.67, 23.85],
    "MiddleR4": [1.0, 23.85],
    "NearR4B0": [1.0, 24.41],
    "Room4Patient0": [3.67, 24.41],
    "BetweenR4B1B2": [1.0, 27.59],
    "Room4Patient1": [-1.0, 27.59],
    "Room4Patient2": [3.67, 27.59],

    "EntryR5": [-3.67, 31.22],
    "MiddleR5": [1.0, 31.22],
    "NearR5B0": [1.0, 32.0],
    "Room5Patient0": [3.67, 32.0],
    "BetweenR5B1B2": [1.0, 36.0],
    "Room5Patient1": [-1.0, 36.0],
    "Room5Patient2": [3.67, 36.0],

    "EntryR6": [-6.55, 31.22],
    "MiddleR6": [-11.0, 31.22],
    "NearR6B0": [-11.0, 32.0],
    "Room6Patient0": [-13.67, 32.0],
    "BetweenR6B1B2": [-11.0, 36.0],
    "Room6Patient2": [-9.23, 36.0],
    "Room6Patient1": [-13.67, 36.0],

    "MiddleHallway1": [-6.55, 14.13],

    "EntryR7": [-6.55, 20.0],
    "MiddleR7": [-11.0, 20.0],
    "NearR7B0": [-11.0, 19.0],
    "Room7Patient0": [-13.67, 19.0],
    "BetweenR7B1B2": [-11.0, 15.16],
    "Room7Patient1": [-9.23, 15.16],
    "Room7Patient2": [-13.67, 15.16],

    "EntryR8": [-6.55, 11.0],
    "MiddleR8": [-11.0, 11.0],
    "NearR8B0": [-11.0, 10.0],
    "Room8Patient0": [-13.67, 10.0],
    "BetweenR8B1B2": [-11.0, 5.31],
    "Room8Patient1": [-9.23, 5.31],
    "Room8Patient2": [-13.67, 5.31],

    "HallwayEntry": [-6.55, -9.64],

    "HallwaySafePoint": [-3.67, 8.5],

    "EntrySafePoint": [6.57, 8.5],
    "SafePoint": [6.57, 5.41],

    "MiddleRoom2Room3": [6.57, 14.13]
}

EDGES = [
    ("Warehouse", "ExitWarehouse"),
    ("ExitWarehouse", "HallwayEntry"),

    ("HallwayEntry", "Hallway0"),
    ("HallwayEntry", "EntryR8"),
    
    ("Hallway0", "EntryR0"),

    ("EntryR0", "MiddleR0"),
    ("MiddleR0", "NearR0B0"),
    ("NearR0B0", "Room0Patient0"),
    ("NearR0B0", "BetweenR0B1B2"),
    ("BetweenR0B1B2", "Room0Patient2"),
    ("BetweenR0B1B2", "Room0Patient1"),

    ("EntryR0", "EntryR1"),
    ("EntryR1", "MiddleR1"),
    ("MiddleR1", "NearR1B0"),
    ("NearR1B0", "Room1Patient0"),
    ("NearR1B0", "BetweenR1B1B2"),
    ("BetweenR1B1B2", "Room1Patient2"),
    ("BetweenR1B1B2", "Room1Patient1"),

    ("EntryR1", "HallwaySafePoint"),
    ("HallwaySafePoint", "Hallway1"),
    ("EntrySafePoint", "HallwaySafePoint"),
    ("EntrySafePoint", "SafePoint"),

    ("EntrySafePoint", "MiddleRoom2Room3"),

    ("MiddleRoom2Room3", "EntryR2D1"),
    ("MiddleRoom2Room3", "EntryR3"),

    ("Hallway1", "EntryR2"),
    ("Hallway1", "EntryR2D1"),

    ("EntryR2", "MiddleR2"),
    ("MiddleR2", "Room2Patient0"),
    ("MiddleR2", "Room2Patient1"),
    ("Room2Patient1", "Room2Patient2"),

    ("EntryR3", "MiddleR3"),
    ("MiddleR3", "NearR3B0"),
    ("NearR3B0", "Room3Patient0"),
    ("NearR3B0", "BetweenR3B1B2"),
    ("BetweenR3B1B2", "Room3Patient2"),
    ("BetweenR3B1B2", "Room3Patient1"),

    ("EntryR2", "EntryR4"),
    ("EntryR4", "MiddleR4"),
    ("MiddleR4", "NearR4B0"),
    ("NearR4B0", "Room4Patient0"),
    ("NearR4B0", "BetweenR4B1B2"),
    ("BetweenR4B1B2", "Room4Patient2"),
    ("BetweenR4B1B2", "Room4Patient1"),

    ("EntryR4", "EntryR5"),
    ("EntryR5", "MiddleR5"),
    ("MiddleR5", "NearR5B0"),
    ("NearR5B0", "Room5Patient0"),
    ("NearR5B0", "BetweenR5B1B2"),
    ("BetweenR5B1B2", "Room5Patient2"),
    ("BetweenR5B1B2", "Room5Patient1"),

    ("EntryR5", "EntryR6"),
    ("EntryR6", "MiddleR6"),
    ("MiddleR6", "NearR6B0"),
    ("NearR6B0", "Room6Patient0"),
    ("NearR6B0", "BetweenR6B1B2"),
    ("BetweenR6B1B2", "Room6Patient2"),
    ("BetweenR6B1B2", "Room6Patient1"),

    ("MiddleHallway1", "EntryR7"),
    ("MiddleHallway1", "EntryR8"),
    ("MiddleHallway1", "EntryR7"),
    ("MiddleHallway1", "Hallway1"),

    ("EntryR6", "EntryR7"),

    ("EntryR7", "MiddleR7"),
    ("MiddleR7", "NearR7B0"),
    ("NearR7B0", "Room7Patient0"),
    ("NearR7B0", "BetweenR7B1B2"),
    ("BetweenR7B1B2", "Room7Patient2"),
    ("BetweenR7B1B2", "Room7Patient1"),

    ("EntryR7", "EntryR8"),

    ("EntryR8", "MiddleR8"),
    ("MiddleR8", "NearR8B0"),
    ("NearR8B0", "Room8Patient0"),
    ("NearR8B0", "BetweenR8B1B2"),
    ("BetweenR8B1B2", "Room8Patient2"),
    ("BetweenR8B1B2", "Room8Patient1")
]

