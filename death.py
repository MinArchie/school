# a text-based adventure game set in a hospital

import time

# values: (keys)-> direction, (value)-> room
rooms = {
    "Corridor": {"Left": "Bathroom", "or Right": "Cafeteria"},
    "Bathroom": {"Explore": "Red or Blue", "or Back": "Corridor"},
    "Cafeteria": {"Right": "Staircase", "or Left": "Corridor"},
    "Staircase": {"Back to Cafeteria (Type 'Back')": "Cafeteria", "or Up": "Terrace", "or Down": "Waiting_Area"},
    "Terrace": {"Jump": "Death", "or Back": "Staircase"},
    "Waiting_Area": {"Up": "Staircase", "or Exit": "Exit", "or Right": "Morgue", "or Left": "Operating_Room"},
    "Operating_Room": {"Back": "Waiting_Area"},
    "Morgue": {"Back": "Waiting_Area"},
    "Exit": {"Back": "Waiting_Area", "or Try": "Finish"}
}


# functions


def corridor():
    location = "Corridor"
    direction = ""

    while direction != "exit":
        print()
        print()
        print("_______________________")
        print("_______________________")
        print("You are in the ", location)

        possible_moves = rooms[location].keys()
        print("possible moves: ", *possible_moves)

        direction = input("\nMove which direction? \n> ").strip().lower()
        print("You entered: ", direction)

        if direction == "left":
            print()
            bathroom()
        elif direction == "right":
            print()
            cafeteria()
        else:
            print()
            print("Invalid move! \nOnly Enter Valid Statements.")
            print()
            print()
            print()
            corridor()


def bathroom():
    location = "Bathroom"
    direction = ""

    print()
    print()
    print()
    print("You are in the ", location)

    print("You head inside to wash your face.")
    time.sleep(1)
    print("You hear knocking coming from the last stall.")
    time.sleep(2)
    print("*knock*")
    time.sleep(1)
    print("*knock*.... *knock*")
    time.sleep(1)
    print("\nWhat do you do? Explore the knocking or Head Back (go back to corridor) \n")

    possible_moves = rooms[location].keys()
    print("Possible moves: ", *possible_moves)

    direction = input("Decision? \n> ").strip().lower()
    print("You entered: ", direction)

    if direction == "back":
        print()
        time.sleep(1)
        corridor()
    elif direction == "explore":
        print()
        time.sleep(1)
        bathroom_ex()
    else:
        print()
        print("Invalid move! \nOnly Enter Valid Statements.")
        print()
        print()
        print()
        time.sleep(1)
        bathroom()


def bathroom_ex():
    location = "Bathroom"
    direction = ""

    print("You see a girl holding two papers; one Red, one Blue. Her eyes are completely black")
    time.sleep(2)
    answer = input("Which do you choose? \n> Red \n> Blue \n>> ").lower().strip()

    if answer == "red":
        print()
        print("The girl pulls out a knife and stabs you.")
        print("Looks Like Curiosity Killed the Cat. Should have retreated when you had the chance. Better luck next time!")
        print()
        print("------------------")
        print("|    GAME OVER   |")
        print("------------------")
        print()
        restart_seq()

    elif answer == "blue":
        print()
        print("The girl gives you a creepy smiles and strangles you.")
        print("Looks Like Curiosity Killed the Cat. Should have retreated when you had the chance. Better luck next time!")
        print()
        print("------------------")
        print("|    GAME OVER   |")
        print("------------------")
        print()
        restart_seq()

    else:
        print()
        print("Invalid move! \nOnly Enter Valid Statements.")
        print()
        print()
        print()
        time.sleep(1)
        bathroom_ex()


def cafeteria():
    location = "Cafeteria"
    direction = ""

    print("You are in the ", location)

    print("It seems to be connected to the stairway.")
    time.sleep(1)
    print("Suddenly, you smell something weird, like rotten meat.")
    print("You cautiously look at the food there, and discover that they all look like organs.")
    time.sleep(2)
    print("Human organs...")
    time.sleep(2)
    answer1 = input("What do you do? \n>Run to the staircase! \n>Eat the organs! \n>Go Back to Corridor! \n(Type Run or Eat or Back) \n>> ").lower().strip()
    if answer1 == "run":
        print()
        print("The sight of the 'food' still makes you uncomfortable")
        print("Perhaps you could go up for some fresh air or go down.")
        staircase()

    elif answer1 == "eat":
        print()
        print("You try to eat the organs, but quickly realize that they were infected. You died.")
        print("Perhaps cannibalism isn't the option.")
        print()
        print("------------------")
        print("|    GAME OVER   |")
        print("------------------")
        print()
        restart_seq()
    elif answer1 == "back":
        print()
        time.sleep(1)
        corridor()
    else:
        print()
        print("Invalid move! \nOnly Enter Valid Statements.")
        time.sleep(1)
        print()
        print()
        print()
        cafeteria()


    possible_moves = rooms[location].keys()
    print("Possible moves: ", *possible_moves)

    direction = input("Move which direction? \n>> ").strip().lower()
    print("You entered: ", direction)

    if direction == "right":
        print("The sight of the 'food' still makes you uncomfortable")
        print("Perhaps you could go up for some fresh air or go down.")
        staircase()

    elif direction == "left":
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
    else:
        print()
        print("Invalid move! \nOnly Enter Valid Statements.")
        time.sleep(1)
        print()
        print()
        staircase()


def terrace():
    location = "Terrace"
    direction = ""

    print()
    print()
    print()
    print("* ,   . *   `. *` . . *,")
    print("  .  *  ` . * ,  . `  . ")

    print("You are in the, ", location)

    print("The stars look pretty tonight.")
    print("You wonder what exactly you're doing here.")
    print("You're not sure what exactly you want to do either.")
    print("Would you like to go back downstairs or...")

    possible_moves = rooms[location].keys()
    print("Possible moves: ", *possible_moves)

    direction = input("Decision? \n>> ").strip().lower()
    print("You entered: ", direction)

    if direction == "back":
        print()
        print("As tempting as a trip to the stars sounds like, you decide to keep fighting.")
        print("You could come back here anytime, anyway.")
        staircase()

    #secret ending

    elif direction == "jump":
        print()
        print("The stars looked pretty, so you decided to join them.")
        print("You didn't really want to fight anymore.")
        print("This place looks like it isn't worth it anyway.")
        print("You died.")
        time.sleep(6)
        print("LOADING...")
        time.sleep(2)
        print("You wake up.")
        time.sleep(1)
        print("In a white room.")
        time.sleep(1)
        print("You get a sense of deja-vu.")
        time.sleep(1)
        print("You see the door opening")
        time.sleep(2)
        print("A nurse walks in, the one that you recognize. You remember that he checks in on you frequently.")
        print('"It is time for your pills again," he says. "I hope you weren\'t hallucinating again."')
        print("Ah well, that explains a lot.")
        time.sleep(3)
        print()
        print()
        print("UNLOCKED SECRET ENDING")
        time.sleep(2)

        print()
        print("------------------")
        print("|    GAME OVER   |")
        print("------------------")
        print()

        restart_seq()
    else:
        print()
        print("Invalid move! \nOnly Enter Valid Statements.")
        time.sleep(1)
        print()
        print()
        print()
        terrace()


def waiting_area():
    location = "Waiting_Area"
    direction = ""

    while direction != "exit":

        print()
        print("You are in the ", location)

        print("You feel sick to the stomach, the sight of human organs still plaguing your thoughts.")
        print("Never the less, you carry on.")
        print("")
        print("The Waiting_Area is connected to two other rooms and the Exit.")
        print("You may also go back up the staircase. (Type 'up')")
        print()

        possible_moves = rooms[location].keys()
        print("possible moves: ", *possible_moves)

        direction = input("Move which direction? \n>> ").strip().lower()
        print("You entered: ", direction)

        if direction == "left":
            print()
            operation_room()
        elif direction == "up":
            print()
            staircase()
        elif direction == "right":
            print()
            morgue()
        elif direction == "exit":
            print()
            password()
        else:
            print()
            print("Invalid move! \nOnly Enter Valid Statements.")
            time.sleep(1)
            print()
            print()
            print()
            waiting_area()


def password():
    location = "Exit"
    direction = ""

    while direction != "exit":
        print("You are at the ", location)

        print("There's a four digit code that you need to enter to get out.")
        print("Do you wish to try? Remember, you have a limited amount of attempts")
        print("Head Back if you think you aren't ready.")
        print("")

        possible_moves = rooms[location].keys()
        print("possible moves: ", *possible_moves)

        direction = input("Move which direction? \n>> ").strip().lower()
        print("You entered: ", direction)

        if direction == "back":
            print()
            waiting_area()

        elif direction == "try":
            word = "echo"
            guess = input("Guess the 4-letter word (You have only 2 tries): ")
            tries = 1

            if guess != word:
                print()
                print("INCORRECT PASSWORD.")
                print("Try again, and get it right if you wish to live.")
                tries += 1
                guess = input("Guess the 4-letter word: ")
            if guess != word and tries == 2:
                time.sleep(1)
                print("INCORRECT PASSWORD")
                time.sleep(1)
                print("ACCESS DENIED")
                time.sleep(1)
                print("INITIATING LOCKDOWN...")
                time.sleep(1)
                print("You watch as the hospital goes into lockdown, sealing you inside for eternity.")
                time.sleep(1.5)
                print("With these monsters.")
                print("You died.\n")
                print()
                time.sleep(1)
                print("------------------")
                print("|    GAME OVER   |")
                print("------------------")
                print()
                time.sleep(1)
                restart_seq()

            print()
            print("CORRECT PASSWORD")
            print("You made it out alive.")
            print()
            print("------------------")
            print("|     YOU WON    |")
            print("------------------")
            print()
            restart_seq()
        else:
            print()
            print("Invalid move! \nOnly Enter Valid Statements.")
            time.sleep(1)
            print()
            print()
            print()
            password()


def operation_room():
    location = "Operating_Room"
    direction = ""

    print("You are in the ", location)

    print()
    print("You can go Back to the Waiting_Area")
    possible_moves = rooms[location].keys()
    print("Possible moves: ", *possible_moves)

    direction = input("Move which direction? \n>> ").strip().lower()
    print("You entered: ", direction)

    if direction == "back":
        print()
        waiting_area()
    else:
        print()
        print("Invalid move! \nOnly Enter Valid Statements.")
        time.sleep(1)
        print()
        print()
        print()
        operation_room()


def morgue():
    location = "Morgue"
    direction = ""

    print("You are in the ", location)

    print()
    print("You can go back to the Waiting_Area")
    possible_moves = rooms[location].keys()
    print("Possible moves: ", *possible_moves)

    direction = input("Move which direction? \n>> ").strip().lower()
    print("You entered: ", direction)

    if direction == "back":
        print()
        waiting_area()
    else:
        print()
        print("Invalid move! \nOnly Enter Valid Statements.")
        time.sleep(1)
        print()
        print()
        print()
        morgue()


def restart_seq():
    answer1 = input("Replay Game? (Yes/No) \n>> ").strip().lower()
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
    else:
        print()
        print("Sorry, I don't understand. English please!")
        time.sleep(1)
        print()
        print()
        restart_seq()


# call stuff

print()
print()
print()
print("********************")
print("*   LUCID DREAMS   *")
print("********************")
print()
print()
print()
time.sleep(2)
print("Welcome!")
print("The rules of the game are simple. Type the command from given options. Find a way to escape.")
time.sleep(2)
print("GAME LOADING...")
time.sleep(1)
print("TIP: use lower-case characters only")
time.sleep(1)
print("LOADING...")
print()
print()
print()
time.sleep(3)
print("You wake up groggy and unsure. It's dark, so you turn on the light.")
print("You realize you're in a hospital. You decide to get out and explore.")
print()
time.sleep(2)
corridor()


