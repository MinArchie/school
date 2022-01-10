# a text-based adventure game set in a hospital

import time

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
        "or Buzzing": "Death",
        "or Back": "Waiting_Area"
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

    inventory.clear()
    print()
    print("A white room. A single bed. One window. ")
    print("There is a door that leads to the corridor")
    print()
    print()

    possible_moves = rooms[location].keys()
    print("possible moves:", *possible_moves)

    direction = input("\nWhat will you do? \n> ").lower().strip()
    print("You entered:", direction)

    if direction == "door":
        print()
        corridor()
    elif direction == "inspect":
        print("It’s plain, clean, and impersonal.")
        quitting()
        print("You can’t jump out of the window; it’s grilled shut.")
        print("The walls are clean, immaculate. The floor— pristine. The bed is always made. ")
        print("No matter how much you destroy the place, it reverts back to its original state.")
        print()
        print()
        white_room()
    elif direction == "quit":
        print("")
        quit("GAME TERMINATING...")
    else:
        print("Please enter valid statements")
        print()
        print()
        white_room()


def corridor():
    location = "Corridor"
    direction = ""

    while direction != "exit":
        print()
        print()
        print("_______________________")
        print("_______________________")
        print("You are in the", location)
        print()
        print()
        quitting()
        print("It is a long, straight hallway. White floors, white walls.")
        print("To the left is the bathroom. To the right, the cafeteria.")
        print()

        possible_moves = rooms[location].keys()
        print("possible moves:", *possible_moves)

        direction = input("\nMove which direction? \n> ").lower().strip()
        print("You entered:", direction)

        if direction == "left":
            print()
            print()
            bathroom()
        elif direction == "right":
            print()
            cafeteria()
        elif direction == "quit":
            print("")
            quit("GAME TERMINATING...")
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
    print("You are in the", location)
    quitting()
    print("A row of toilet stalls. A mirror. Sinks. A ghost that knocks.")
    print()
    print()
    print("...")
    quitting()
    print("*knock*")
    time.sleep(1)
    print("*knock* *knock*")

    quitting()
    print("You never did put a ghost in this bathroom, at least not consciously.")
    print("But it’s always there now. In the last stall. Each time you come in.")
    quitting()

    print("\nWhat do you do? Investigate the knocking or Head Back (go back to corridor) \n")

    possible_moves = rooms[location].keys()
    print("Possible moves:", *possible_moves)

    direction = input("Decision? \n> ").lower().strip()
    print("You entered:", direction)

    if direction == "back":
        print()
        print()
        corridor()
    elif direction == "investigate":
        print()
        print()
        bathroom_ex()
    elif direction == "quit":
        print("")
        quit("GAME TERMINATING...")
    else:
        print()
        print("Invalid move! \nOnly Enter Valid Statements.")
        print()
        print()
        print()
        bathroom()


def bathroom_ex():
    location = "Bathroom Stall"
    direction = ""

    print()
    print()
    print()
    print("You are in the", location)
    print()

    print("A young girl, holding out two cards. One red and One blue.")
    quitting()
    print("Her empty BLACK eyes peak at your soul from the fringes of her BLACK hair. ")
    quitting()

    print("She asks you to choose. But regardless of your choice, you die each time.")
    print()
    quitting()
    print("Maybe you should try something new.")

    answer = input("Which color do you choose? \n>> ").lower().strip()

    if answer == "red":
        print()
        print("You knew it was coming, but still flinched when she stabs you. ")
        print()
        print()
        print("You wake up in the white room.")
        quitting()
        print("Her Black eyes still haunt your memories.")
        print("Maybe Red isn’t the answer.")
        print("(Press Enter to Continue...")
        quitting()
        white_room()

    elif answer == "blue":
        print()
        print("You knew it was coming, but still flinched when she strangles you.")

        print()
        print()
        print("You wake up in the white room.")
        quitting()
        print("Her Black eyes still haunt your memories.")
        print("Maybe Blue isn’t the answer.")
        print("(Press Enter to Continue...)")
        quitting()
        print()
        print()
        white_room()

    elif answer == "black":
        print()
        print("Ah. Interesting. You choose a completely different color.")
        print()

        print("Slowly, she turns her head to the side, not stopping until it did a complete 180 degree turn.")
        print()
        quitting()
        print("You let your eyes focus on the back of her head, and notice the letter 'R' written on it")
        print()

        print("You get a feeling that this is important.")
        print()

        print("Seeing as nothing more happened, you head back to the corridor.")
        quitting()
        print()
        print()
        corridor()

    elif direction == "quit":
        print("")
        quit("GAME TERMINATING...")
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

    print("You are in the", location)

    print("It seems to be connected to the stairway.")
    quitting()
    print("As you enter, you see the menu.")
    print("    —— —— —— —— —— —— —— ")
    print("    |       menu       |")
    print("    | 1)juIce          |")
    print("    | 2)pIzza          |")
    print("    | 3)Ice cream      |")
    print("    | 4)rIce           |")
    print("    | 5)chIcken wIngs  |")
    print("    —— —— —— —— —— —— —— ")
    print("How peculiar... The letter ‘I’ stands out.")
    print()
    quitting()
    print("Behind the counter you see a wide variety of...")
    print("Human organs...")
    print()
    print("You don’t know why. But looking at it makes your stomach hurl each time. ")
    print()

    answer1 = input("What do you do? \n>Run to the staircase! \n>Eat the organs! \n>Go Back to Corridor! \n(Type Run or Eat or Back) \n>> ").lower().strip()
    if answer1 == "run":
        print()
        print("The sight of the 'food' still makes you uncomfortable")
        print("Perhaps you could go up for some fresh air or go down.")
        quitting()
        print()
        print()
        staircase()
    elif answer1 == "eat":
        print()
        print("You don’t understand what compels you to do this.")
        quitting()
        print("But you eat the organs.")
        print()
        print()
        print("You wake up in the white room. The feeling of nausea won’t leave you.")
        quitting()
        print("Maybe cannibalism isn't the answer.")
        print()
        print()
        print("...")
        quitting()
        white_room()
    elif answer1 == "back":
        print()
        print()
        corridor()
    elif direction == "quit":
        print("")
        quit("GAME TERMINATING...")
    else:
        print()
        print("Invalid move! \nOnly Enter Valid Statements.")
        print()
        print()
        print()
        cafeteria()


def staircase():
    location = "Staircase"
    direction = ""

    print("You are in the", location)

    possible_moves = rooms[location].keys()
    print("Possible moves:", *possible_moves)

    direction = input("Move which direction? \n>> ").lower().strip()
    print("You entered:", direction)

    if direction == "up":
        print()
        print()
        take_crowbar()
    elif direction == "down":
        print()
        print()
        waiting_area()
    elif direction == "back":
        print()
        print()
        cafeteria()
    elif direction == "quit":
        print("")
        quit("GAME TERMINATING...")
    else:
        print()
        print("Invalid move! \nOnly Enter Valid Statements.")
        print()
        print()
        staircase()


def take_crowbar():
    while 'crowbar' not in inventory:
        print()
        print()
        print()
        print("On the way up the stairs, something catches your eye.")
        quitting()
        print("It's a Crowbar! ")
        quitting()
        print("Should you take it? ")
        print("But what could you possibly use it for?")
        print()
        print()
        print("Pick it up?")
        take_the_crowbar = input("Yes/No: \n>> ").lower().strip()

        if take_the_crowbar == "yes":
            add_to_inventory("crowbar")
            print("CROWBAR added to inventory")
            print("Inventory:")
            print(inventory)
            print()
            print()
            quitting()
            terrace()
        elif take_the_crowbar == "no":
            print("You leave the Crowbar in the Terrace.")
            print()
            print()
            print("...")
            quitting()
            terrace()
        elif take_the_crowbar == "quit":
            print("")
            quit("GAME TERMINATING...")
        else:
            print()
            print("Invalid move! \nOnly Enter Valid Statements.")
            print()
            print()
            print()
            take_crowbar()
    terrace()


def terrace():
    location = "Terrace"
    direction = ""

    print()
    print()
    print("* ,   . +   `. *` . . +,   *  ` . + ,  . `  .")
    print("  .  *  ` . + ,  . `  .   . +   `. *` . . + `")

    print("You are in the", location)
    quitting()

    print("The stars look pretty tonight.")
    quitting()
    print("You wonder what exactly you're doing here.")
    print("You're not sure what exactly you want to do either.")
    quitting()
    print("Would you like to go back downstairs or...")

    possible_moves = rooms[location].keys()
    print("Possible moves:", *possible_moves)

    direction = input("Decision? \n>> ").lower().strip()
    print("You entered:", direction)

    if direction == "back":
        print()
        print("As tempting as a trip to the stars sounds like, you decide to keep fighting.")
        quitting()
        print("You could come back here anytime, anyway.")
        print()
        print()
        quitting()
        staircase()
    elif direction == "jump":
        print()
        print("Do you really wish to jump? Nothing special would happen. You’ll just die.")
        print("AKA wake up in the white room.")
        quitting()
        print("Maybe it's different this time...")
        quitting()
        print("You brace yourself and fall forward.")
        print()
        print()
        print("... Only to wake up in the White Room.")
        quitting()
        print("God dammit.")
        print("Same thing, again and again.")
        quitting()
        print()
        print()
        white_room()
    elif direction == "quit":
        print("")
        quit("GAME TERMINATING...")
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
        print("You are in the", location)
        print()

        print("The deeper levels always felt strange to you.")
        quitting()
        print("The Waiting Area is nothing much, except for the safe locker.")
        print("To the left is an operating room and to the right... a morgue.")
        quitting()
        print("There’s also a supply closet.")
        print("You may also go back up the staircase. (Type 'up')")
        quitting()
        print()

        possible_moves = rooms[location].keys()
        print("possible moves:", *possible_moves)

        direction = input("Move which direction? \n>> ").lower().strip()
        print("You entered:", direction)

        if direction == "left":
            print()
            print()
            operation_room()
        elif direction == "up":
            print()
            print()
            staircase()
        elif direction == "right":
            print()
            print()
            morgue()
        elif direction == "exit":
            print()
            print()
            password()
        elif direction == "inspect":
            if 'bug spray' not in inventory:
                print()
                print("You navigate your way through the chairs.")
                print("You see a door that leads to the cleaning closet.")
                quitting()
                print("In there you find a bottle of bug spray")
                quitting()
                print("Pick it up?")
                take_spray()
            elif 'bug spray' in inventory:
                print()
                print("There is nothing left to inspect")
                print()
                print()
                waiting_area()
            elif direction == "quit":
                print("")
                quit("GAME TERMINATING...")
        elif direction == "quit":
            print("")
            quit("GAME TERMINATING...")
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
        if "bug spray" in inventory:
            print()
            print("You already have this item!")
            quitting()
            print("Inventory:")
            print(inventory)
        elif "bug spray" not in inventory:
            add_to_inventory("bug spray")
            print()
            print("Bug spray added to inventory")
            quitting()
            print("Inventory:")
            print(inventory)
            print()
            print("You head back to the waiting_area")
            quitting()
            print()
            print()
            waiting_area()
        elif take_the_spray == "quit":
            print("")
            quit("GAME TERMINATING...")
        else:
            print()
            print("Invalid move! \nOnly Enter Valid Statements.")
            print()
            print()
            print()
            take_spray()

    elif take_the_spray == "no":
        print()
        print("You leave the Bug spray in the cabinet.")
        quitting()
        print("You head back to the waiting_area")
        quitting()
        print()
        print()
        waiting_area()
    elif take_the_spray == "quit":
        print("")
        quit("GAME TERMINATING...")
    else:
        print()
        print("Invalid move! \nOnly Enter Valid Statements.")
        print()
        print()
        print()
        take_spray()


def operation_room():
    location = "Operating_Room"
    direction = ""

    print("You are in the", location)
    print()
    quitting()
    print("'The Mad Surgeon', as you’ve come to call him, greets you.")
    print("He wears his scrubs and a face mask and a face shield.")
    quitting()
    print("He asks you if you want to get rid of your depression.")
    print("What a concept. But maybe it’s worth another shot...")
    quitting()
    print("All you know is that you can't kill him, but you can stall for time.")
    quitting()
    print("Every time he 'dies', it only takes him a few minutes to come back to life.")
    quitting()
    print("Looks like he's alive again.")

    print()
    print("You can go Back to the Waiting_Area")
    print("Possible moves: ", "Accept,", "Deny,", " or Back")
    print()

    direction = input("What do you do? \n>> ").lower().strip()
    print("You entered:", direction)

    if direction == "back":
        print()
        print()
        waiting_area()
    elif direction == "accept":
        print("You lay on the bench, telling yourself that maybe this time he can actually cure you.")
        print("...")
        quitting()
        print("You sigh as you hear him laugh. The Mad Surgeon tells you that all he wants from you are your organs.")
        print("He congratulates you for being stupid enough to think anything could cure you.")
        quitting()
        print("You hope you won’t wake up in the White Room again.")
        print()
        print("But of course, you do.")
        quitting()
        print()
        print()
        white_room()
    elif direction == "deny":
        deny()
    elif direction == "quit":
        print("")
        quit("GAME TERMINATING...")
    else:
        print()
        print("Invalid move! \nOnly Enter Valid Statements.")
        print()
        print()
        print()
        operation_room()


def deny():
    print()
    print("The surgeon charges at you with a scalpel.")
    print()
    print("Possible moves: 'Inventory' or 'Run'")
    print()
    decide = input("Quick! What do you do?: \n>>").lower().strip()

    if decide == "inventory":
        print(inventory)
        if not inventory:
            print()
            print("Uh-oh. Looks like you have nothing to defend yourself with.")
            print("Only thing you can do now, is run.")
            quitting()
            print("So you turn around and try to run")
            print("But he catches up with you.")
            print()
            print("You wake up in the white room.")
            print("Maybe next time you should find something to defend yourself with...")
            quitting()
            print()
            print()
            white_room()
        else:
            defend = input("Pick something to defend yourself with. \n>> ").lower().replace(" ","")
            if defend == "crowbar":
                print()
                print("The surgeon tries to stab you with his scalpel.")
                print("You block his attacks.")
                quitting()
                print("You delt him a deadly blow with your crowbar and watch as his body flops to the ground.")
                print()
                quitting()
                print("You notice his ID card.")
                print("It has the letter 'B' written on it.")
                quitting()
                print()
                print("Feeling a little shaky, you return to the Waiting_Area")
                quitting()
                print()
                print()
                waiting_area()
            elif defend == "bugspray":
                print("The surgeon tries to stab you with his scalpel.")
                quitting()
                print("You use the bug spray, but realize how ineffective it is against his surgical mask and face shield")
                print("How stupid! You try to run away, but he catches up to you.")
                quitting()
                print("You were unable to make it out alive.")
                print()
                print()
                print("You wake up in the white room, yet again.")
                quitting()
                print()
                print()
                white_room()
            elif defend == "quit":
                print("")
                quit("GAME TERMINATING...")
            else:
                print()
                print("Invalid move! \nOnly Enter Valid Statements.")
                print()
                print()
                print()
                deny()
    elif decide == "run":
        print()
        print("The surgeon tries to stab you with his scalpel.")
        quitting()
        print("You turn around and try to run,")
        print("But you couldn't make it in time.")
        quitting()
        print()
        print()
        print("You wake up in the white room.")
        quitting()
        print()
        print()
        white_room()
    elif decide == "quit":
        print("")
        quit("GAME TERMINATING...")
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

    print("You are in the", location)

    print()
    print("The Lights Flicker.\n")
    quitting()
    print("This place gives you a bad vibe")
    quitting()
    print("There’s a body on the stretcher. A white sheet covers it.")
    print("The blood seeps through the fabric.")
    quitting()
    print("The foot is uncovered. You can see the toe tag.")
    quitting()
    print("At the same time, you hear a sharp buzzing sound.")
    time.sleep(1)
    print("*Buzzzzzz*")
    print()
    print("It originates from one of the body storage cabinets.")
    print()
    print("What do you do? Inspect the Body or the Buzzing?")
    print("(You may also go back to the Waiting_Area)")

    possible_moves = rooms[location].keys()
    print("Possible moves:", *possible_moves)

    direction = input("Decision? \n>> ").lower().strip()
    print("You entered: ", direction)

    if direction == "back":
        print()
        print()
        waiting_area()
    elif direction == "body":
        print()
        print("You cautiously make your way towards the body.")
        quitting()
        print("Upon closer inspection, you notice that the foot is decomposing.")
        print("The toe tag seems to be covered in mud. How unusual.")
        quitting()
        print()
        print("You reach forward to dust off the mud.")
        quitting()
        print("Suddenly, the body sits up.")
        quitting()
        print("Scared to death, you run back to the waiting room.")
    elif direction == "buzzing":
        buzz()
    elif direction == "quit":
        print("")
        quit("GAME TERMINATING...")
    else:
        print()
        print("Invalid move! \nOnly Enter Valid Statements.")

        print()
        print()
        print()
        morgue()


def buzz():
    print()
    print("You head towards the cabinet wondering what's causing that noise.")
    quitting()
    print("It stops; you don't hear a thing.")
    quitting()
    print("Something's fishy and you know it, but you open the cabinet anyway.")
    quitting()
    print("*Buzzzzzz*")
    print("Before you realize, a swarm of bluebottle flies surround you.")
    print("\"It's just flies,\" you think.")
    quitting()
    print("Something feels off. But what?")
    quitting()
    print("It's your skin.")
    time.sleep(1)
    print("Crap. They are feeding on your skin!")
    print()
    print()
    print("Possible moves: Inventory or run")
    decide = input("What do you do? \n>> ").lower().strip()

    if decide == "inventory":
        print(inventory)
        if not inventory:
            print()
            print("Uh-oh. Looks like you have nothing to defend yourself with.")
            print("Only one thing left to do.")
            quitting()
            print("You turn around and run,")
            print("But you can't get through. It's an impenetrable swarm of flies.")
            quitting()
            print("You try but you get eaten to death by those flies.")
            print()
            print()
            print("You wake up in the white room.")
            print("Maybe next time you should find something to defend yourself with...")
            quitting()
            print()
            print()
            white_room()
        elif decide == "quit":
            print("")
            quit("GAME TERMINATING...")
        else:
            defend = input("Pick something to defend yourself with. \n>> ").lower().replace(" ","")
            if defend == "bugspray":
                print()
                print("The flies won't leave you alone.")
                print("So you use the bugspray to kill 'em.")
                quitting()
                print("You spray it all over the room and watch as they rain down to the ground.")
                quitting()
                print("A simple, but effective solution.")
                print()
                print("Once the last of them die, you notice a piece of paper in the cabinet.")
                quitting()
                print("It has the letter 'D' written on it.")
                quitting()
                print("You get the feeling that this is important. You return to the Waiting Area.")
                print("...")
                quitting()
                print()
                print()
                waiting_area()
            elif defend == "crowbar":
                print()
                print("The swarm of flies dive on to you.")
                time.sleep(0.2)
                print("You use the crowbar, but realize that the flies just escapes your every hit.")
                quitting()
                print("How stupid! You try to run away, but it's of no use")
                time.sleep(0.2)
                print("You get eaten up to death by those flies.")
                print()
                print()
                print("You wake up; again in the white room.")
                quitting()
                print()
                print()
                white_room()
            elif defend == "quit":
                print("")
                quit("GAME TERMINATING...")
            else:
                print()
                print("Invalid move! \nOnly Enter Valid Statements.")
                print()
                print()
                print()
                buzz()
    elif decide == "run":
        print()
        print("The swarm of flies dive on to you.")
        print()
        print("You turn around and try to run")
        quitting()
        print("But you just can't get through it.")
        time.sleep(0.3)
        print("And you get eaten up to death by those flies.")
        print()
        print()
        print("You wake up in the white room.")
        quitting()
        print()
        print()
        white_room()
    elif decide == "quit":
        print("")
        quit("GAME TERMINATING...")
    else:
        print()
        print("Invalid move! \nOnly Enter Valid Statements.")
        print()
        print()
        print()
        buzz()


def password():
    location = "Exit"
    direction = ""

    print()
    print("You are at the", location, ". Or you hope it is.")
    quitting()
    print("There's a safe with a four letter code.")
    quitting()
    print("Do you wish to try? Remember, you have a limited amount of attempts.")
    print("Head Back if you think you aren't ready.")
    quitting()
    print("")

    possible_moves = rooms[location].keys()
    print("possible moves:", *possible_moves)

    direction = input("Your choice? \n>> ").lower().strip()
    print("You entered:", direction)

    if direction == "back":
        print()
        print()
        waiting_area()
    elif direction == "try":
        word = "bird"
        guess = input("Guess the 4-letter word (You have only 2 tries): ").lower().strip()
        tries = 1
        if guess != word:
            print()
            print("INCORRECT PASSWORD.")
            print("Try again, and get it right if you wish to live.")
            tries += 1
            guess = input("Guess the 4-letter word: ")
        if guess != word and tries == 2:
            print()
            print("INCORRECT PASSWORD")
            time.sleep(0.3)
            print("You got it wrong.")
            quitting()
            print("A tiny part of you wished that this meant you would die. For real.")
            quitting()
            print("But reality is often disappointing.")
            print()
            print()
            print("You're back at the White Room again.")
            quitting()
            print("Just like every other time.")
            print("Death just doesn't seem to exist here.")
            quitting()
            print()
            print()
            white_room()
        print()
        print("CORRECT PASSWORD")
        print()
        safe()
    elif direction == "quit":
        print("")
        quit("GAME TERMINATING...")
    else:
        print()
        print("Invalid move! \nOnly Enter Valid Statements.")
        print()
        print()
        print()
        password()


def safe():
    print()
    print("You open the safe, smiling, hoping for something good to happen.")
    quitting()
    print("Inside, you see a locket; it was your mom's. It has a picture of us together.")
    time.sleep(0.3)
    print("It was the only thing that was left of hers.")
    quitting()
    print("//FLASHBACK//")
    print("She used to suffer from nightmares, something similar to yours.")
    print("But she was brave enough to resist. She even managed to overcome it.")
    quitting()
    print("Perhaps you’re just not strong enough...")
    quitting()
    print()
    print("You remember... She used to say:")
    quitting()
    print("        \"My little bird, I hope when you take that leap")
    print("         of faith, you have nothing to fear anymore...\"")
    print("//FLASHBACK END//")
    quitting()
    print()
    print("A leap of faith...")
    print("A leap... a Jump...?!")
    quitting()
    print("Is that what it means?")
    print("Maybe...")
    quitting()
    print("But I’ve tried jumping off the terrace. Maybe more than a hundred times.")
    print("It always ends in the White Room.")
    quitting()
    print("Well. There can’t be any harm in trying once more.")
    print("It might be different.")
    quitting()
    print("You head straight to the terrace.")
    print()
    print()
    quitting()
    terrace_alt()


def terrace_alt():
    location = "Terrace"
    direction = ""

    print()
    print()
    print("* ,   . +   `. *` . . +,   *  ` . + ,  . `  .")
    print("  .  *  ` . + ,  . `  .   . +   `. *` . . + `")

    print("You are in the", location)
    quitting()
    print("This is it.")
    quitting()
    print("You take one last look at the stars.")
    print("You could jump... Or you could head back.")
    quitting()
    print("But you've exhausted every inch of this nightmare.")
    print("There is no point in heading back.")

    print("Possible moves: Stay or Jump")

    direction = input("Decision? \n>> ").lower().strip()
    print("You entered:", direction)

    if direction == "stay":
        print()
        print("Alright. No.")
        print("You don't want to jump. Not right now, at least.")
        print("You could come back here anytime, anyway.")
        quitting()
        print("Right...?")
        print("...")
        quitting()
        print("... It doesn't feel right though...")
        quitting()
        print()
        print("Nevertheless, you leave.")
        quitting()
        print("On the way downstairs, you feel your vision black out.")
        print()
        print()
        print()
        print("You slowly come to yourself.")
        quitting()
        print("You're in a white room. The White Room.")
        quitting()
        print("You squeeze your eyes shut. It shouldn't be happening. No, not after everything— just to come back here—")
        quitting()
        print("But what else did you expect? You did nothing different.")
        print("You were a coward who didn't take the chance to change.")
        quitting()
        print("You’re stuck. You can’t get out.")
        quitting()
        print("It’s a dream. It’s a nightmare.")
        time.sleep(0.4)
        print("It’s a nightmare. You’re stuck.")
        time.sleep(0.4)
        print("You’re stuck.")
        time.sleep(0.3)
        print("You’re stuck. You’re stuck. You’re stuck.")
        time.sleep(0.2)
        print("You’re stuck. You’re stuck. You’re stuck. You’re stuck. You’re stuck. You’re stuck.")
        time.sleep(0.1)
        print("Stuck. Stuck. Stuck. Stu—")
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print("...")
        quitting()
        print("------------------------")
        print("| ENDING 2/2: INSANITY |")
        print("------------------------")
        print()
        print()
        print("You couldn't make it out.")
        print("You stayed, despite knowing there was a way out.")
        quitting()
        print("Your grief and thoughts weigh you down.")
        quitting()
        print("You wonder if you could have done anything differently.")
        quitting()
        print("If you had been brave.")
        quitting()
        print("Maybe things would have been better...")
        quitting()
        print()
        print()
        print()
        print()
        restart_seq()

    elif direction == "jump":
        print()
        print("You brace yourself, and fall forward.")
        print()
        print()
        print()
        print("You slowly come to yourself, waking up in a white room.")
        quitting()
        print("A white room? /The/ white room?")
        quitting()
        print("You squeeze your eyes shut. It couldn’t be happening. No, not after everything— just to come back here—")
        time.sleep(0.5)
        print("*knock*")
        time.sleep(0.2)
        print("*knock*")
        print("Someone walks in through the door— a man— a man that you recognize.")
        print("A man from the hospital— the one you were in before the dream.")
        quitting()
        quitting()
        print("This isn't a part of the dream. It’s not the dream— is it the dream?")
        quitting()
        print("It can’t be. There are in people here. Real people you haven’t seen in your dreams. ")
        print()
        print()
        quitting()
        print("The nurse asks you if you've been sleeping well.")
        print("You nod.")
        print()
        quitting()
        print("You search for your mother's locket on your bedside table.")
        print("It's there. You see two faces smiling at one another.")
        quitting()
        print("You carefully rip the picture until only your mother’s face remains, and place it back into the locket.")
        print("Your mother lives in dreams. You belong here.")
        print()
        print()
        print("You’re not sure when you’re going to be okay... but that’s okay.")
        quitting()
        print("It might take a while, but you will make it out of this hospital.")
        print("With a full recovery.")
        quitting()
        print("You won’t get stuck.")
        quitting()
        print("You look at your mother one last time before you close the locket with a click.")
        quitting()
        print()
        print()
        print()
        print()
        print()
        print()
        print("-----------------------")
        print("| ENDING 1/2: CLOSURE |")
        print("-----------------------")
        print()
        print()
        print("It was the fear of being stuck in a hospital that put you in an endless loop of actually being stuck.")
        print("After coming to terms with yourself, you realize that it might take a while for you to be alright.")
        quitting()
        print("But you know it’ll happen someday.")
        print()
        print()
        quitting()
        print("Congratulations! You made it!")
        print()
        restart_seq()
    elif direction == "quit":
        print("")
        quit("GAME TERMINATING...")
    else:
        print()
        print("Invalid move! \nOnly Enter Valid Statements.")
        print()
        print()
        print()
        terrace_alt()


def add_to_inventory(item):
    inventory.append(item)


def restart_seq():
    answer1 = input("Replay Game? (Yes/No) \n>> ").lower().strip()
    if answer1 == "yes":
        print(""*5)
        print("RESTARTING...")

        print()
        print()
        print("You're back here again.")
        print("You know it's a dream, that’s for sure.")
        print("(Press Enter to Continue...)")
        quitting()
        print("But you're stuck here. Stuck for too long.")
        print("You can't control all of it. It feels like it's the dream that controls you.")
        quitting()
        print("You are trapped in this twisted hospital")
        print("You can't wake up. You can't die. If you die, you wake up back in this room.")
        quitting()
        print("All you want is to be freed.")

        quitting()
        print()
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


def quitting():
    user = input()
    while user != "quit":
        break
    else:
        quit("GAME TERMINATING...")


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
time.sleep(1)
print("The rules of the game are simple. Type the command from given options. Find a way to escape.")
time.sleep(2)
print("GAME LOADING...")
time.sleep(1)
print("TIP: use lower-case characters only")
time.sleep(1.5)
print("LOADING...")
time.sleep(0.4)
print("Type 'quit' to exit game at anytime.")
time.sleep(1.5)
print("STARTING GAME...")
print()
print()
print()
time.sleep(3)
print("You're back here again.")
print("You know it's a dream, that’s for sure.")
print("(Press Enter to Continue...)")
quitting()
print("But you're stuck here. Stuck for too long.")
print("You can't control all of it. It feels like it's the dream that controls you.")
quitting()
print("You are trapped in this twisted hospital")
print("You can't wake up. You can't die. If you die, you wake up back in this room.")
quitting()
print("All you want is to be freed.")

quitting()
print()

white_room()
