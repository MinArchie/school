# a text-based adventure game set in a hospital

# import time

# values: (keys)-> direction, (value)-> room
rooms = {
    "White_Room": {
        "Door": "Corridor",
        "or Inspect": "Description"
    },
    "Corridor": {
        "Left": "Bathroom",
        "or Right": "Cafeteria"
    },
    "Bathroom": {
        "Investigate": "Red or Blue",
        "or Back": "Corridor"
    },
    "Cafeteria": {
        "Right": "Staircase",
        "or Left": "Corridor"
    },
    "Staircase": {
        "Back to Cafeteria (Type 'Back')": "Cafeteria",
        "or Up": "Terrace",
        "or Down": "Waiting_Area"
    },
    "Terrace": {
        "Jump": "Death",
        "or Back": "Staircase"
    },
    "Waiting_Area": {
        "Up": "Staircase",
        "or Exit": "Exit",
        "or Right": "Morgue",
        "or Left": "Operating_Room",
        "or Inspect": "Find pepper Spray"
    },
    "Operating_Room": {
        "Back": "Waiting_Area",
        "Accept": "Death",
        "Deny": {
            "Crowbar": "No Death",
            "Run": "Death",
            "Bug_Spray": "Death"
        }
    },
    "Morgue": {
        "Body": "Unlock a letter",
        "Buzzing": "Death",
        "Back": "Waiting_Area"
    },
    "Exit": {
        "Back": "Waiting_Area",
        "or Try": "Finish"
    }
}

inventory = []


# functions

def white_room():
    location = "White_Room"
    direction = ""

    print()
    print("A white room. A single bed. One window. ")
    print("There is a door that leads to the corridor")

    possible_moves = rooms[location].keys()
    print("possible moves: ", *possible_moves)

    direction = input("\nWhat will you do? \n> ").strip().lower()
    print("You entered: ", direction)

    if direction == "door":
        print()
        corridor()
    elif direction == "inspect":
        print("It’s plain, clean, and impersonal.")
        print("You can’t jump out of the window; it’s grilled shut.")
        print("The walls are clean, immaculate. The floor— pristine. The bed is always made. ")
        print("No matter how much you destroy the place, it reverts back to its original state.")
        print()
        white_room()
    else:
        print("Please enter valid statements")
        white_room()


def corridor():
    location = "Corridor"
    direction = ""

    while direction != "exit":
        print()
        print()
        print("_______________________")
        print("_______________________")
        print("You are in the ", location)

        print()
        print("It is a long, straight hallway. White floors, white walls.")
        print("To the left is the bathroom. To the right, the cafeteria.")

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

    print("A row of toilet stalls. A mirror. Sinks. A ghost that knocks.")

    print()
    print()

    print("Like clockwork, you hear knocking coming from the last stall.")

    print("*knock*")

    print("*knock*.... *knock*")

    print("You never did put a ghost in this bathroom, at least not consciously.")
    print("But it’s always there now. In the last stall. Each time you come in.")

    print("\nWhat do you do? Investigate the knocking or Head Back (go back to corridor) \n")

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

    print("You remember reading about a story of a ghost that kills you regardless of the color you choose.")

    print("You wonder if your fate here is to die in a similar way.")
    print()

    print("Scared, you try to move out of the stall, only to find your feet stuck to the ground.")

    print("She won't let you go without making a decision.")

    answer = input("Which color do you choose? \n>> ").lower().strip()

    if answer == "red":
        print()
        print("The red card materializes into a knife. The girl's Black eyes twinkle as her arm extends to stab you.")
        print("You died.")
        print()
        print("Wrong Decision.")
        print("Perhaps next time, you could try picking a color you see on her.")
        print()
        print()
        print()
        print("You're back here again.")
        print("Just like every other time.")
        print("Death just doesn't seem to exist here.")
        white_room()

    elif answer == "blue":
        print()
        print("The girl gives you a creepy smile as her head tilts down, her Black hair completely covering her face.")
        print("Her arms quickly extend unnaturally, reaching towards your neck to strangle you.")
        print("You died.")
        print()
        print("Perhaps next time, you could try picking a color you see on her.")
        print()
        print()
        print()
        print("You're back here again.")
        print("Just like every other time.")
        print("Death just doesn't seem to exist here.")
        white_room()

    elif answer == "black":
        print()
        print("Ah. Interesting. You choose a completely different color.")

        print("The Red and Blue papers disappear from the girl's extended arms.")

        print("Slowly, she turns her head to the side, not stopping until it did a complete 180 degree turn.")

        print("She makes no other move.")
        print()

        print("You let your eyes focus on the back of her head, and notice the letter 'H' written on it")
        print()

        print("You get a feeling that this is important.")
        print()

        print("Seeing as nothing more happened, you head back to the corridor.")

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

    print("Suddenly, you smell something weird, like rotten meat.")
    print("You cautiously look at the food there, and discover that they all look like organs.")

    print("Human organs...")

    answer1 = input("What do you do? \n>Run to the staircase! \n>Eat the organs! \n>Go Back to Corridor! \n(Type Run or Eat or Back) \n>> ").lower().strip()
    if answer1 == "run":
        print()
        print("The sight of the 'food' still makes you uncomfortable")
        print("Perhaps you could go up for some fresh air or go down.")
        staircase()

    elif answer1 == "eat":
        print()
        print()
        print()
        print("You're back here again.")
        print("Just like every other time.")
        print("Perhaps cannibalism isn't the answer.")
        white_room()
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
    print("You wonder what exactly you're doing here.")
    print("You're not sure what exactly you want to do either.")
    print("Would you like to go back downstairs or...")

    possible_moves = rooms[location].keys()
    print("Possible moves:", *possible_moves)

    direction = input("Decision? \n>> ").strip().lower()
    print("You entered:", direction)

    if direction == "back":
        print()
        print("As tempting as a trip to the stars sounds like, you decide to keep fighting.")
        print("You could come back here anytime, anyway.")
        staircase()

    # secret ending

    elif direction == "jump":
        print("Still gotta work on this")
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

        print("You feel sick to the stomach, the sight of human organs still plaguing your thoughts.")
        print("Never the less, you carry on.")
        print("")
        print("The Waiting_Area is connected to two other rooms and the Exit.")
        print("You may inspect the area.")
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
        elif direction == "inspect":
            if 'pepper spray' not in inventory:
                print("You navigate your way through the chairs.")
                print("You see a door that leads to the cleaning closet.")
                print("In there you find a bottle of pepper spray")
                print("Pick it up?")
                take_spray()
            elif 'pepper spray' in inventory:
                print()
                print("There is nothing left to inspect")
                waiting_area()

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
            take_spray()

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
        take_spray()
# have to change this part to fit our new script


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

                print()
                print()
                print("You're back here again.")
                print("Just like every other time.")
                print("Death just doesn't seem to exist here.")
                white_room()

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
    print("'The Mad Surgeon', as you’ve come to call him, greets you.")
    print("He wears his scrubs and a face mask and a face shield.")
    print("He asks you if you want to get rid of your depression.")
    print("What a concept. But maybe it’s worth another shot...")
    print("All you know is that you can't kill him, but you can stall for time.")
    print("Every time he 'dies', it only takes him a few minutes to come back to life.")
    print("Looks like he's alive again.")

    print()
    print("You can go Back to the Waiting_Area")
    print("Possible moves: ", "Accept,", "Deny,", " or Back")

    direction = input("What do you do? \n>> ").strip().lower()
    print("You entered: ", direction)

    if direction == "back":
        print()
        waiting_area()
    elif direction == "accept":
        print("You lay on the bench, telling yourself that maybe this time he can actually cure you.")
        print("You sigh as you hear him laugh. The Mad Surgeon tells you that all he wants from you are your organs.")
        print("He congratulates you for being stupid enough to think anything could cure you.")
        print("You hope you won’t wake up in the White Room again.")
        print()
        print("But of course, you do.")
        white_room()
    elif direction == "deny":
        deny()

    else:
        print()
        print("Invalid move! \nOnly Enter Valid Statements.")

        print()
        print()
        print()
        operation_room()


def deny():
    print("The surgeon charges at you with a scalpel.")
    print("Possible moves: 'Inventory' or 'Run'")
    decide = input("What do you do?: \n>>").lower().strip()

    if decide == "inventory":
        print(inventory)
        if not inventory:
            print("Uh-oh. Looks like you have nothing to defend yourself with.")
            print("Only thing you can do now, is run.")
            print("The surgeon tries to stab you with his scalpel.")
            print("You turn around and try to run")
            print("But he catches up with you.")
            print()
            print("You wake up in the white room.")
            print("Maybe next time you should find something to defend yourself with...")
            white_room()
        else:
            defend = input("Pick something to defend yourself with. \n>> ").lower().strip()
            if defend == "crowbar":
                print("The surgeon tries to stab you with his scalpel.")
                print("You block his attacks.")
                print("You delt him a deadly blow with your crowbar and watch as his body flops to the ground.")
                print()
                print("You notice his ID card.")
                print("It has the letter 'B' written on it.")
                print()
                print("Feeling a little shaky, you return to the Waiting_Area")
                print()
                waiting_area()
            elif defend == "bug_spray":
                print("The surgeon tries to stab you with his scalpel.")
                print("You use the bug spray, but realize how ineffective it is against his surgical mask and face shield")
                print(" How stupid! You try to run away, but he catches up to you.")
                print()
                print()
                print("You wake up, again in the white room.")
                white_room()

            else:
                print()
                print("Invalid move! \nOnly Enter Valid Statements.")

                print()
                print()
                print()
                deny()
    elif decide == "run":
        print("The surgeon tries to stab you with his scalpel.")
        print("You turn around and try to run")
        print("But he catches up with you.")
        print()
        print("You wake up in the white room.")
        white_room()
    else:
        print()
        print("Invalid move! \nOnly Enter Valid Statements.")

        print()
        print()
        print()
        deny()


def morgue():
    location = "Morgue"
    direction = ""

    print("You are in the ", location)

    print()
    print("The Lights Flicker.\n")
    print("This place gives you a bad vibe, but it might just be because of the dead body on the stretcher.\n")
    print("A white sheet covers the body. The blood seeps through the fabric.")
    print("The foot is uncovered. You can see the toe tag.")
    print("At the same time, you hear a sharp buzzing sound.")
    print("It originates from one of the body storage cabinets.")
    print("What do you do? Inspect the Body or the Buzzing?")
    print("(You may also go back to the Waiting_Area)")

    possible_moves = rooms[location].keys()
    print("Possible moves: ", *possible_moves)

    direction = input("Decision? \n>> ").strip().lower()
    print("You entered: ", direction)

    if direction == "back":
        print()
        waiting_area()
    elif direction == "body":
        print()
        print("You cautiously make your way towards the body.")
        print("Upon closer inspection, you notice that the foot is decomposing.")
        print("The toe tag seems to be covered in mud. How unusual.")
        print()
        print("You dust off some of the mud. You see the letter 'C' written on it.")
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
        print("You're back here again.")
        print("You know it's a dream. You just know.")
        print("In the beginning, You could manipulate this dream however you liked.")
        print("But now...")
        print("But now you just don't have the strength.")
        print("You've been here too long.")
        print("You can't control it anymore. Now, it's the dream controls you.")
        print("All you see is this constant nightmare.")
        print("You, trapped in this twisted hospital, living and reliving the same thing again and again.")
        print("You can't wake up. You can't die. If you die, you wake up back in this room.")
        print("Last time, you died jumping off the terrace.")
        print("You're not sure if it's going to be any different this time.")
        white_room()

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

print("Welcome!")
print("The rules of the game are simple. Type the command from given options. Find a way to escape.")

print("GAME LOADING...")

print("TIP: use lower-case characters only")

print("You may use items from your inventory, but they might not always work for the situation.")

print("LOADING...")
print()
print()
print()

print("You're back here again.")
print("You know it's a dream. You just know.")
print("In the beginning, You could manipulate this dream however you liked.")
print("But now...")
print("But now you just don't have the strength.")
print("You've been here too long.")
print("You can't control it anymore. Now, it's the dream controls you.")
print("All you see is this constant nightmare.")
print("You, trapped in this twisted hospital, living and reliving the same thing again and again.")
print("You can't wake up. You can't die. If you die, you wake up back in this room.")
print("Last time, you died jumping off the terrace.")
print("You're not sure if it's going to be any different this time.")

print()

white_room()
