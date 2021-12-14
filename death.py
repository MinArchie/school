# a text-based adventure game set in a hospital

import time

# values: (keys)-> direction, (value)-> room
rooms = {
    "Corridor": {"West": "Bathroom", "or East": "Cafeteria"},
    "Bathroom": {"Explore": "Red or Blue", "or East": "Corridor"},
    "Cafeteria": {"East": "Staircase", "or West": "Corridor"},
    "Staircase": {"Back to Cafeteria (Type 'Back')": "Cafeteria", "or Up": "Terrace", "or Down": "Waiting_Area"},
    "Terrace": {"Jump": "Death", "or South": "Staircase"},
    "Waiting_Area": {"North": "Staircase", "or South": "Exit", "or East": "Morgue", "or West": "Operating_Room"},
    "Operating_Room": {"East": "Waiting_Area"},
    "Morgue": {"West": "Waiting_Area"},
    "Exit": {"North": "Waiting_Area", "Try": "Finish"}
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
    time.sleep(1)
    print("You hear knocking coming from the last stall.")
    time.sleep(2)
    print("*knock*")
    time.sleep(1)
    print("*knock*.... *knock*")
    time.sleep(1)
    print("\nWhat do you do? Explore the knocking or Head East (go back to corridor) \n")

    possible_moves = rooms[location].keys()
    print("Possible moves: ", *possible_moves)

    direction = input("Decision? \n> ").strip().lower()
    print("You entered: ", direction)

    if direction == "east":
        print()
        corridor()
    if direction == "explore":
        print()
        print("You see a girl holding two papers; one Red, one Blue. Her eyes are completely black")
        time.sleep(2)
        answer = input("Which do you choose? \n> Red \n> Blue \n>> ").lower().strip()
        if answer == "red":
            time.sleep(1)
            print()
            print("The girl pulls out a knife and stabs you.")
            print("Looks Like Curiosity Killed the Cat. Should have retreated when you had the chance. Better luck next time!")
            restart_seq()
        elif answer == "blue":
            time.sleep(1)
            print()
            print("The girl gives you a creepy smiles and strangles you.")
            print("Looks Like Curiosity Killed the Cat. Should have retreated when you had the chance. Better luck next time!")
            restart_seq()


def cafeteria():
    location = "Cafeteria"
    direction = ""

    print("You are in the ", location)

    print("It seems to be connected to the stairway.")
    time.sleep(2)
    print("Suddenly, you smell something weird, like rotten meat.")
    print("You cautiously look at the food there, and discover that they all look like organs.")
    time.sleep(2)
    print("Human organs...")
    time.sleep(1)
    answer1 = input("What do you do? \n>Run to the staircase! \n>Eat the organs! \n(Type Run or Eat) \n>> ").lower().strip()
    if answer1 == "run":
        print()
        print("The sight of the 'food' still makes you uncomfortable")
        print("Perhaps you could go up for some fresh air or go down.")
        staircase()


    elif answer1 == "eat":
        print()
        print("You try to eat the organs, but quickly realize that they were infected. You died.")
        print("Perhaps cannibalism isn't the option.")
        restart_seq()


    possible_moves = rooms[location].keys()
    print("Possible moves: ", *possible_moves)

    direction = input("Move which direction? \n>> ").strip().lower()
    print("You entered: ", direction)

    if direction == "east":
        print("The sight of the 'food' still makes you uncomfortable")
        print("Perhaps you could go up for some fresh air or go down.")
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

    direction = input("Move which direction? \n>> ").strip().lower()
    print("You entered: ", direction)

    if direction == "up":
        print()
        terrace()
    elif direction == "down":
        print()
        waiting_area()
    elif direction == "back":
        print()
        cafeteria()


def terrace():
    location = "Terrace"
    direction = ""

    print("You are in the, ", location)

    possible_moves = rooms[location].keys()
    print("Possible moves: ", *possible_moves)

    direction = input("Move which direction? \n>> ").strip().lower()
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

        direction = input("Move which direction? \n>> ").strip().lower()
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
            password()


def password():
    location = "Exit"
    direction = ""

    while direction != "exit":
        print("You are at the ", location)

        print("There's a four digit code that you need to enter to get out.")
        print("Do you wish to try? Remember, you have a limited amount of attempts")
        print("")

        possible_moves = rooms[location].keys()
        print("possible moves: ", *possible_moves)

        direction = input("Move which direction? \n>> ").strip().lower()
        print("You entered: ", direction)

        if direction == "north":
            print()
            waiting_area()
        elif direction == "try":
            word = "echo"
            guess = input("Guess the 4-letter word (You have only 2 tries): ")
            tries = 1

            if guess != word:
                print("Wrong answer. Try again, and get it right if you wish to live.")
                tries += 1
                guess = input("Guess the 4-letter word: ")
            if guess != word and tries == 2:
                print("You failed to guess the word. ")
                print("You watch as the hospital goes into lockdown, sealing you inside for eternity.")
                print("With these monsters.")
                print("You died.\n")
                restart_seq()

            print("Well done you guessed correctly! The word was ECHO.")
            restart_seq()



def operation_room():
    location = "Operating_Room"
    direction = ""

    print("You are in the, ", location)

    possible_moves = rooms[location].keys()
    print("Possible moves: ", *possible_moves)

    direction = input("Move which direction? \n>> ").strip().lower()
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

    direction = input("Move which direction? \n>> ").strip().lower()
    print("You entered: ", direction)

    if direction == "west":
        print()
        waiting_area()


def restart_seq():
    answer1 = input("Restart Game? (Yes/No) \n>> ").strip().lower()
    if answer1 == "yes":
        print(""*5)
        print("RESTARTING...")
        time.sleep(2)
        print()
        print()
        print("You wake up groggy and unsure. It's dark, so you turn on the light.")
        print("You realize you're in a hospital. You decide to get out and explore.")
        corridor()

    elif answer1 == "no":
        print("Thank you for playing :)")
        quit()


# call stuff

print()
print()
print()
print("*********************")
print("*       TITLE       *")
print("*********************")
print()
print()
print()
time.sleep(2)
print("Welcome!")
print("The rules of the game are simple. Find a way to escape.")
time.sleep(2)
print("GAME LOADING...")
time.sleep(1)
print("HINT: use lowercases only")
time.sleep(1)
print("LOADING...")
print()
print()
print()
time.sleep(3)
print("You wake up groggy and unsure. It's dark, so you turn on the light.")
print("You realize you're in a hospital. You decide to get out and explore.")
print()
corridor()
