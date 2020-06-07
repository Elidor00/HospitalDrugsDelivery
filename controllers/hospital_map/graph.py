# coordinate for target points
MAP_POINTS = {
    "Warehouse": [-10.26, 0.22],
    "ExitWareHouse": [-10.26, -9.64],
    "Hallway0": [-3.67, -9.64],

    "EntryR0": [-3.67, -3.1],
    "NearR0B0": [-1.09, -3.1],
    "R0Bed0": [-1.09, -3.99],
    "BetweenR0B0B3": [1.33, -3.1],
    "NearR0B3": [3.74, -3.1],
    "R0Bed3": [3.74, -3.99],
    "BetweenR0B1B2": [1.33, -8],
    "R0Bed2": [3.74, -8],
    "R0Bed1": [-1.09, -8],

    "EntryR1": [-3.67, 5.78],
    "NearR1B0": [-1.09, 5.78],
    "R1Bed0": [-1.09, 4.63],
    "BetweenR1B0B3": [1.33, 5.78],
    "NearR1B3": [3.74, 5.78],
    "R1Bed3": [3.74, 4.63],
    "BetweenR1B1B2": [1.33, -0.8],
    "R1Bed2": [3.74, -0.8],
    "R1Bed1": [-1.09, -0.8],

    "EntryR4": [-3.67, 31.06],
    "NearR4B0": [-1.09, 31.06],
    "R4Bed3": [-1.09, 32.45],
    "BetweenR4B0B3": [1.33, 31.06],
    "NearR4B3": [3.74, 31.06],
    "R4Bed0": [3.74, 32.45],
    "BetweenR4B1B2": [1.33, 36.0],
    "R4Bed1": [3.74, 36.0],
    "R4Bed2": [-1.09, 36.0],

    "EntryR3": [-3.67, 23.30],
    "EntryR2": [-3.67, 15.08]

}

Edges = [
    ("Warehouse", "ExitWareHouse"),
    ("ExitWareHouse", "Hallway0"),
    ("Hallway0", "EntryR0"),

    ("EntryR0", "NearR0B0"),
    ("NearR0B0", "BetweenR0B0B3"),
    ("NearR0B0", "R0Bed0"),
    ("BetweenR0B0B3", "NearR0B3"),
    ("NearR0B3", "R0Bed3"),
    ("BetweenR0B0B3", "BetweenR0B1B2"),
    ("BetweenR0B1B2", "R0Bed2"),
    ("BetweenR0B1B2", "R0Bed1"),

    ("EntryR0", "EntryR1"),
    ("EntryR1", "NearR1B0"),
    ("NearR1B0", "BetweenR1B0B3"),
    ("NearR1B0", "R1Bed0"),
    ("BetweenR1B0B3", "NearR1B3"),
    ("NearR1B3", "R1Bed3"),
    ("BetweenR1B0B3", "BetweenR1B1B2"),
    ("BetweenR1B1B2", "R1Bed2"),
    ("BetweenR1B1B2", "R1Bed1"),

    ("EntryR3", "EntryR4"),
    ("EntryR4", "NearR4B0"),
    ("NearR4B0", "BetweenR4B0B3"),
    ("NearR4B0", "R4Bed0"),
    ("BetweenR4B0B3", "NearR4B3"),
    ("NearR4B3", "R4Bed3"),
    ("BetweenR4B0B3", "BetweenR4B1B2"),
    ("BetweenR4B1B2", "R4Bed2"),
    ("BetweenR4B1B2", "R4Bed1"),

]

