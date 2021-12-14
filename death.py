# a text-based adventure game set in a hospital

# values: (keys)-> direction, (value)-> room

rooms = {
    "Corridor": {"West": "Bathroom", "East": "Cafeteria"},
    "Bathroom": {"Explore": "Red or Blue","East": "Corridor"},
    "Cafeteria": {"East": "Staircase"},
    "Staircase": {"North": "Terrace", "South": "Waiting_Area"},
    "Terrace": {"Jump": "Death", "South": "Staircase"},
    "Waiting_Area": {"West": "Operating_Room", "East": "Morgue", "South": "Exit"},
    "Operating_Room": {"East": "Waiting_Area"},
    "Morgue": {"West": "Waiting_Area"}
}


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
    if direction == "explore":
        print("You see a girl holding two papers; one Red, one Blue.")
        answer = input("Which do you choose? \n1) Red \n2)Blue \n")
        if answer == "1":
            print("You died")
            restart_seq()
        elif answer == "2":
            print("you died")
            restart_seq()


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
    elif direction == "jump":
        print("You died")
        restart_seq()


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
            print("You won")
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


def restart_seq():
    answer1 = input("Restart Game? (Yes/No)").strip().lower()
    if answer1 == "yes":
        print("RESTARTING...")
        corridor()

    elif answer1 == "no":
        print("Thank you for playing :)")
        quit()


corridor()
