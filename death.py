# a text-based adventure game set in a hospital

# values: (keys)-> direction, (value)-> room
rooms = {
    "Corridor": {"West": "Bathroom", "or East": "Cafeteria"},
    "Bathroom": {"Explore": "Red or Blue", "or East": "Corridor"},
    "Cafeteria": {"East": "Staircase", "or West": "Corridor"},
    "Staircase": {"West": "Cafeteria", "or North": "Terrace", "or South": "Waiting_Area"},
    "Terrace": {"Jump": "Death", "or South": "Staircase"},
    "Waiting_Area": {"North": "Staircase", "or South": "Exit", "or East": "Morgue", "or West": "Operating_Room"},
    "Operating_Room": {"East": "Waiting_Area"},
    "Morgue": {"West": "Waiting_Area"}
}


# functions


def corridor():
    location = "Corridor"
    direction = ""

    while direction != "exit":
        print("You are in the ", location)

        possible_moves = rooms[location].keys()
        print("possible moves: ", *possible_moves)

        direction = input("\nMove which direction? \n> ").strip().lower()
        print("You entered: ", direction)

        if direction == "west":
            print()
            bathroom()
        elif direction == "east":
            print()
            cafeteria()


def bathroom():
    location = "Bathroom"
    direction = ""

    print("You are in the ", location)

    print("You head inside to wash your face.")
    print("You hear knocking coming from the last stall.")
    print("\nWhat do you do? Explore the knocking or Head East (go back to corridor) \n")

    possible_moves = rooms[location].keys()
    print("Possible moves: ", *possible_moves)

    direction = input("Move which direction? \n> ").strip().lower()
    print("You entered: ", direction)

    if direction == "east":
        print()
        corridor()
    if direction == "explore":
        print()
        print("You see a girl holding two papers; one Red, one Blue.")
        answer = input("Which do you choose? \n> Red \n> Blue \n>> ").lower().strip()
        if answer == "red":
            print()
            print("The girl pulls out a knife and stabs you.")
            print("Looks Like Curiosity Killed the Cat. Should have retreated when you had the chance. Better luck next time!")
            restart_seq()
        elif answer == "blue":
            print()
            print("The girl smiles and strangles you.")
            print("Looks Like Curiosity Killed the Cat. Should have retreated when you had the chance. Better luck next time!")
            restart_seq()


def cafeteria():
    location = "Cafeteria"
    direction = ""

    print("You are in the ", location)

    print("It seems to be connected to the stairway.")
    print("Suddenly, you smell something weird, like rotten meat.")
    print("You cautiously look at the food there, and discover that they all look like organs.")
    print("Human organs...")
    answer1 = input("What do you do? \n>Run to the staircase! \n>Grab the thing (Type Run or Grab)")


    possible_moves = rooms[location].keys()
    print("Possible moves: ", *possible_moves)

    direction = input("Move which direction? \n> ").strip().lower()
    print("You entered: ", direction)

    if direction == "east":
        print()
        staircase()
    elif direction == "west":
        print()
        corridor()


def staircase():
    location = "Staircase"
    direction = ""

    print("You are in the ", location)

    possible_moves = rooms[location].keys()
    print("Possible moves: ", *possible_moves)

    direction = input("Move which direction? \n> ").strip().lower()
    print("You entered: ", direction)

    if direction == "north":
        print()
        terrace()
    elif direction == "south":
        print()
        waiting_area()
    elif direction == "west":
        print()
        cafeteria()


def terrace():
    location = "Terrace"
    direction = ""

    print("You are in the, ", location)

    possible_moves = rooms[location].keys()
    print("Possible moves: ", *possible_moves)

    direction = input("Move which direction? \n> ").strip().lower()
    print("You entered: ", direction)

    if direction == "south":
        print()
        staircase()
    elif direction == "jump":
        print()
        print("You died")
        restart_seq()


def waiting_area():
    location = "Waiting_Area"
    direction = ""

    while direction != "exit":
        print("You are in the ", location)

        print("You feel sick to the stomach, the sight of human organs still plaguing your thoughts.")
        print("Never the less, you carry on.")
        print("")

        possible_moves = rooms[location].keys()
        print("possible moves: ", *possible_moves)

        direction = input("Move which direction? \n> ").strip().lower()
        print("You entered: ", direction)

        if direction == "west":
            print()
            operation_room()
        elif direction == "north":
            print()
            staircase()
        elif direction == "east":
            print()
            morgue()
        elif direction == "south":
            print()
            print("You are now at the exit, but you need a 4-letter word to get through.")
            print("Time is running out, the monsters won't wait for you.")
            password()


def password():
    word = "echo"
    guess = input("Guess the 4-letter word:")
    tries = 1

    if guess != word:
        print("Wrong answer. Try again if you have the nerve.")
        tries += 1
        guess = input("Guess the 4-letter word:")
    if guess != word and tries == 2:
        print("You failed to guess the word was it that hard?\n")
        restart_seq()

    print("Well done you guessed correctly! The word was ECHO.")
    restart_seq()


def operation_room():
    location = "Operating_Room"
    direction = ""

    print("You are in the, ", location)

    possible_moves = rooms[location].keys()
    print("Possible moves: ", *possible_moves)

    direction = input("Move which direction? \n> ").strip().lower()
    print("You entered: ", direction)

    if direction == "east":
        print()
        waiting_area()


def morgue():
    location = "Morgue"
    direction = ""

    print("You are in the, ", location)

    possible_moves = rooms[location].keys()
    print("Possible moves: ", *possible_moves)

    direction = input("Move which direction? \n> ").strip().lower()
    print("You entered: ", direction)

    if direction == "west":
        print()
        waiting_area()


def restart_seq():
    answer1 = input("Restart Game? (Yes/No) \n> ").strip().lower()
    if answer1 == "yes":
        print(""*5)
        print("RESTARTING...")
        print("You wake up groggy and unsure. It's dark, so you turn on the light.")
        print("You realize you're in a hospital. You decide to get out and explore.")
        corridor()

    elif answer1 == "no":
        print("Thank you for playing :)")
        quit()


# call stuff

print()
print()
print("You wake up groggy and unsure. It's dark, so you turn on the light.")
print("You realize you're in a hospital. You decide to get out and explore.")
print()
corridor()
