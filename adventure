# a text-based adventure game set in a hospital

import time

# values: (keys)-> direction, (value)-> room
rooms = {
    "Corridor": {"Left": "Bathroom", "or Right": "Cafeteria"},
    "Bathroom": {"Investigate": "Red or Blue", "or Back": "Corridor"},
    "Cafeteria": {"Right": "Staircase", "or Left": "Corridor"},
    "Staircase": {"Back to Cafeteria (Type 'Back')": "Cafeteria", "or Up": "Terrace", "or Down": "Waiting_Area"},
    "Terrace": {"Jump": "Death", "or Back": "Staircase"},
    "Waiting_Area": {"Up": "Staircase", "or Exit": "Exit", "or Right": "Morgue", "or Left": "Operating_Room", "or Inspect": "Find pepper Spray"},
    "Operating_Room": {"Back": "Waiting_Area"},
    "Morgue": {"Body": "Unlock a letter", "or Buzzing": "Death", "or Back": "Waiting_Area"},
    "Exit": {"Back": "Waiting_Area", "or Try": "Finish"}
}

inventory = []


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

    print()
    print()

    possible_moves = rooms[location].keys()
    print("Possible moves: ", *possible_moves)

    direction = input("Decision? \n> ").strip().lower()
    print("You entered: ", direction)

    if direction == "back":
        print()

        corridor()
    elif direction == "investigate":
        print()

        bathroom_ex()
    else:
        print()
        print("Invalid move! \nOnly Enter Valid Statements.")
        print()
        print()
        print()

        bathroom()


def take_crowbar():
    while 'crowbar' not in inventory:
        print()
        print()
        print()
        print("On the way up the stairs, something catches your eye.")

        print("It's a Crowbar! ")
        print("Should you take it? ")
        print("But what could you possibly use it for?")
        print()

        print("Pick it up?")
        take_the_crowbar = input("Yes/No: \n>> ").lower().strip()

        if take_the_crowbar == "yes":
                add_to_inventory("crowbar")
                print("CROWBAR added to inventory")
                print("Inventory:")
                print(inventory)

                terrace()

        elif take_the_crowbar == "no":
            print("You leave the Crowbar in the Terrace.")

            terrace()

        else:
            print()
            print("Invalid move! \nOnly Enter Valid Statements.")

            print()
            print()
            print()
            take_crowbar()
    terrace()


def bathroom_ex():
    location = "Bathroom Stall"
    direction = ""

    print()
    print()
    print()
    print("You are in the ", location)
    print()

    print("You see a girl holding out two cards; one Red, one Blue. Her eyes are Black, and hair is also completely Black.")

    answer = input("Which color do you choose? \n>> ").lower().strip()

    if answer == "red":
        print()
        print("The red card materializes into a knife. The girl's Black eyes twinkle as her arm extends to stab you.")
        print("You died.")
        print()
        print("Wrong Decision.")
        print("Perhaps next time, you could try picking a color you see on her.")
        print()
        print("------------------")
        print("|    GAME OVER   |")
        print("------------------")
        print()
        restart_seq()

    elif answer == "blue":
        print()
        print("The girl gives you a creepy smile as her head tilts down, her Black hair completely covering her face.")
        print("Her arms quickly extend unnaturally, reaching towards your neck to strangle you.")
        print("You died.")
        print()
        print("Perhaps next time, you could try picking a color you see on her.")
        print()
        print("------------------")
        print("|    GAME OVER   |")
        print("------------------")
        print()
        restart_seq()

    elif answer == "black":
        print()
        print()

        print("You let your eyes focus on the back of her head, and notice the letter 'H' written on it")
        print()

        print("You get a feeling that this is important.")

        corridor()

    else:
        print()
        print("Invalid move! \nOnly Enter Valid Statements.")
        print()
        print()
        print()

        bathroom_ex()


def cafeteria():
    location = "Cafeteria"
    direction = ""

    print("You are in the ", location)

    print("It seems to be connected to the stairway.")

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

        corridor()
    else:
        print()
        print("Invalid move! \nOnly Enter Valid Statements.")

        print()
        print()
        print()
        cafeteria()

    possible_moves = rooms[location].keys()
    print("Possible moves: ", *possible_moves)

    direction = input("Move which direction? \n>> ").strip().lower()
    print("You entered: ", direction)

    if direction == "right":
        print()
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
        take_crowbar()
    elif direction == "down":
        print()
        waiting_area()
    elif direction == "back":
        print()
        cafeteria()
    else:
        print()
        print("Invalid move! \nOnly Enter Valid Statements.")

        print()
        print()
        staircase()


def terrace():
    location = "Terrace"
    direction = ""

    print()
    print()
    print("* ,   . +   `. *` . . +,   *  ` . + ,  . `  .")
    print("  .  *  ` . + ,  . `  .   . +   `. *` . . + `")

    print("You are in the", location)

    print("The stars look pretty tonight.")

    possible_moves = rooms[location].keys()
    print("Possible moves:", *possible_moves)

    direction = input("Decision? \n>> ").strip().lower()
    print("You entered:", direction)

    if direction == "back":
        print()
        print("As tempting as a trip to the stars sounds like, you decide to keep fighting.")
        print("You could come back here anytime, anyway.")
        print()
        staircase()

    # secret ending

    elif direction == "jump":
        print()
        print("The stars looked pretty, so you decided to join them.")
        print("You didn't really want to fight anymore.")
        print("This place looks like it isn't worth it anyway.")
        print("You died.")

        print("LOADING...")


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
        terrace()


def waiting_area():
    location = "Waiting_Area"
    direction = ""

    while direction != "exit":

        print()
        print("You are in the ", location)

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
        elif direction == "inspect":
            if 'pepper spray' not in inventory:
                print("You navigate your way through the chairs.")
                print("You see a door that leads to the cleaning closet.")
                print("In there you find a bottle of pepper spray")
                print("Pick it up?")
                take_spray()
            elif 'pepper spray' in inventory:
                print()
                print("You've already searched the area")


        else:
            print()
            print("Invalid move! \nOnly Enter Valid Statements.")

            print()
            print()
            print()
            waiting_area()


def take_spray():
    take_the_spray = input("Yes/No: \n>> ").lower().strip()

    if take_the_spray == "yes":
        if "pepper spray" in inventory:
            print("You already have this item!")
            print("Inventory:")
            print(inventory)
        elif "pepper spray" not in inventory:
            add_to_inventory("pepper spray")
            print("PEPPER SPRAY added to inventory")
            print("Inventory:")
            print(inventory)
            print("You head back to the waiting_area")

            waiting_area()
        else:
            print()
            print("Invalid move! \nOnly Enter Valid Statements.")

            print()
            print()
            print()
            take_the_spray = input("Take Spray? (Yes/No): \n>> ")
            if "pepper spray" in inventory:
                print("You already have this item!")
                print("Inventory:")
                print(inventory)
                waiting_area()
            elif "pepper spray" not in inventory:
                add_to_inventory("pepper spray")
                print("PEPPER SPRAY added to inventory")
                print("Inventory:")
                print(inventory)
                print("You head back to the waiting_area")

                waiting_area()

    elif take_the_spray == "no":
        print("You leave the Pepper Spray in the cabinet.")
        print("You head back to the waiting_area")

        waiting_area()

    else:
        print()
        print("Invalid move! \nOnly Enter Valid Statements.")

        print()
        print()
        print()
        take_the_spray = input("Take Spray? (Yes/No): \n>> ")
        if "pepper spray" in inventory:
            print("You already have this item!")
            print("Inventory:")
            print(inventory)
            waiting_area()
        elif "pepper spray" not in inventory:
            add_to_inventory("pepper spray")
            print("PEPPER SPRAY added to inventory")
            print("Inventory:")
            print(inventory)
            print("You head back to the waiting_area")

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

                print("INCORRECT PASSWORD")

                print("ACCESS DENIED")

                print("INITIATING LOCKDOWN...")

                print("You watch as the hospital goes into lockdown, sealing you inside for eternity.")

                print("With these monsters.")
                print("You died.\n")
                print()

                print("------------------")
                print("|    GAME OVER   |")
                print("------------------")
                print()

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

        print()
        print()
        print()
        operation_room()


def morgue():
    location = "Morgue"
    direction = ""

    print("You are in the ", location)

    print()

    possible_moves = rooms[location].keys()
    print("Possible moves: ", *possible_moves)

    direction = input("Decision? \n>> ").strip().lower()
    print("You entered: ", direction)

    if direction == "back":
        print()
        waiting_area()
    elif direction == "body":
        print()
        print("You see the letter 'C' written on it.")
        print("Suddenly, the body sits up.")

    else:
        print()
        print("Invalid move! \nOnly Enter Valid Statements.")

        print()
        print()
        print()
        morgue()


def add_to_inventory(item):
    inventory.append(item)


def delete_from_inventory(item):
    inventory.remove(item)


def restart_seq():
    answer1 = input("Replay Game? (Yes/No) \n>> ").strip().lower()
    if answer1 == "yes":
        print(""*5)
        print("RESTARTING...")

        print()
        print()
        corridor()

    elif answer1 == "no":
        print("Thank you for playing :)")
        quit()
    else:
        print()
        print("Sorry, I don't understand. English please!")

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
time.sleep(1)
print("Welcome!")
print("The rules of the game are simple. Type the command from given options. Find a way to escape.")
time.sleep(1)
print("GAME LOADING...")
time.sleep(2)
print("TIP: use lower-case characters only")
time.sleep(1)
print("You may use items from your inventory, but they might not always work for the situation.")
time.sleep(1)
print("LOADING...")
print()
print()
print()
time.sleep(2)
print()

corridor()
