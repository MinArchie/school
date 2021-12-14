# a text-based adventure game set in a hospital

#values: (keys)-> direction, (value)-> room
rooms = {
    "Corridor": {"West": "Bathroom", "East": "Cafeteria"},
    "Bathroom": {"East": "Corridor"},
    "Cafeteria": {"East": "Staircase"},
    "Staircase": {"North": "Terrace", "South": "Waiting_Area"},
    "Terrace": {"South": "Staircase"},
    "Waiting_Area": {"West": "Operating_Room", "East": "Morgue", "South": "Exit"},
    "Operating_Room": {"East": "Waiting_Area"},
    "Morgue": {"West": "Waiting_Area"}
}
"""
location = "Corridor"
direction = ""

while direction != "exit":
    print("You are in the ", location)

    possible_moves = rooms[location].keys()
    print("possible moves: ", *possible_moves)

    direction = input("Move which direction? ").strip().lower()
    print("You entered: ", direction)

    if direction == "west":
        location = "Bathroom"
        direction = ""

        print("You are in the ", location)

        possible_moves = rooms[location].keys()
        print("Possible moves: ", *possible_moves)

        direction = input("Move which direction? ").strip().lower()
        print("You entered: ", direction)

        if direction == "east":
            location = "Corridor"
            direction = ""
            print("You are in the ", location)

            possible_moves = rooms[location].keys()
            print("possible moves: ", *possible_moves)

            direction = input("Move which direction? ").strip().lower()
            print("You entered: ", direction)

    elif direction == "east":
        location = "Cafeteria"
        direction = ""

        print("You are in the ", location)

        possible_moves = rooms[location].keys()
        print("Possible moves: ", *possible_moves)

        direction = input("Move which direction? ").strip().lower()
        print("You entered: ", direction)



print("Values (i.e possible directions to connecting rooms): ")
#iterate through each room, show directions to connecting rooms:
#for key in rooms.keys():
    #print(key, "-->", rooms[key].keys())

    #for k in rooms[key].keys():
        #print(key, "-->", k)

for key in rooms.keys():
    #print(key, "-->", rooms[key].values())
    for v in rooms[key].values():
        print(key, "-->", v)
"""


def corridor():
    location = "Corridor"
    direction = ""

    while direction != "exit":
        print("You are in the ", location)

        possible_moves = rooms[location].keys()
        print("possible moves: ", *possible_moves)

        direction = input("Move which direction? ").strip().lower()
        print("You entered: ", direction)

        if direction == "west":
            bathroom()
        elif direction == "east":
            cafeteria()


def bathroom():
    location = "Bathroom"
    direction = ""

    print("You are in the ", location)

    possible_moves = rooms[location].keys()
    print("Possible moves: ", *possible_moves)

    direction = input("Move which direction? ").strip().lower()
    print("You entered: ", direction)

    if direction == "east":
        corridor()


def cafeteria():
    location = "Cafeteria"
    direction = ""

    print("You are in the ", location)

    possible_moves = rooms[location].keys()
    print("Possible moves: ", *possible_moves)

    direction = input("Move which direction? ").strip().lower()
    print("You entered: ", direction)

    if direction == "east":
        staircase()


def staircase():
    location = "Staircase"
    direction = ""

    print("You are in the, ", location)

    possible_moves = rooms[location].keys()
    print("Possible moves: ", *possible_moves)

    direction = input("Move which direction? ").strip().lower()
    print("You entered: ", direction)

    if direction == "north":
        terrace()
    elif direction == "south":
        waiting_area()


def terrace():
    location = "Terrace"
    direction = ""

    print("You are in the, ", location)

    possible_moves = rooms[location].keys()
    print("Possible moves: ", *possible_moves)

    direction = input("Move which direction? ").strip().lower()
    print("You entered: ", direction)

    if direction == "south":
        staircase()


def waiting_area():
    location = "Waiting_Area"
    direction = ""

    while direction != "exit":
        print("You are in the ", location)

        possible_moves = rooms[location].keys()
        print("possible moves: ", *possible_moves)

        direction = input("Move which direction? ").strip().lower()
        print("You entered: ", direction)

        if direction == "west":
            operation_room()
        elif direction == "east":
            morgue()
        elif direction == "south":
            print ("You won")
        exit()


def operation_room():
    location = "Operating_Room"
    direction = ""

    print("You are in the, ", location)

    possible_moves = rooms[location].keys()
    print("Possible moves: ", *possible_moves)

    direction = input("Move which direction? ").strip().lower()
    print("You entered: ", direction)

    if direction == "east":
        waiting_area()


def morgue():
    location = "Morgue"
    direction = ""

    print("You are in the, ", location)

    possible_moves = rooms[location].keys()
    print("Possible moves: ", *possible_moves)

    direction = input("Move which direction? ").strip().lower()
    print("You entered: ", direction)

    if direction == "west":
        waiting_area()




corridor()
