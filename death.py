while True:

    inventory = []
    answer = int(input("You wake up, groggy and unsure. It's dark, so you turn on the light. You realize you're in a hospital. You decide to get out and explore. \nYou're in a long corridor. \n1) Go Left \n2) Go Right \n(Chose 1 or 2) \n"))

    #1: bathroom
    if answer == 1:
        answer = int(input("You walk down the hallway until you reach the bathrooms. You head inside to wash your face. You hear knocking coming from the last stall. \nWhat do you do? \n1) Explore the knocking \n2) Head back \n"))
        #1: stay
        if answer == 1:
            answer = int(input("You open the bathroom stall to find a girl standing, holding out two color papers; one red and one blue. \nWhich one do you choose? \n1) Red \n2) Blue \n"))
            #red
            if answer == 1:
                print("The girl pulls out a knife and stabs you. Should have left the bathroom when you had the chance. Better luck next time!")
                ans = input("Restart Game? (Yes/No)").lower()
                if ans == "yes":
                    print("RESTARTING...")
                    continue
                else:
                    print ("Thanks for playing :)")
                    break
                #blue
            elif answer == 2:
                print("The girl smiles and strangles you. Should have left the bathroom when you had the chance. Better luck next time!")
                ans = input("Restart Game? (Yes/No)").lower()
                if ans == "yes":
                    print("RESTARTING...")
                    continue
                else:
                    print("Thanks for playing :)")
                    break
        #2:leave
        else:
            answer = int(input("\nYou're in a long corridor. \n2) Go Right \n"))
            if answer == 2:
                answer = int(input(
                    "You walk down the hallway until you reach the cafeteria. It is connected to stairway. The cafeteria smells funky. You see that all the food here are just human organs...?! \nWhat do you do? \n1) Run to the stairway \n2) Eat the organs! \n"))
                # 1: stairway
                if answer == 1:
                    answer = int(input("You're in the stairway. \nWhich way do you go? \n1) Up \n2) Down \n"))
                    # 1: terrace
                    if answer == 1:
                        answer = int(input(
                            "You're in the Terrace. The stars look great tonight. There's nothing much here. \nWhat do you do? \n1) Jump off the building \n2)Head back. \n"))
                        if answer == 1:
                            print(
                                    "The stars looked pretty. You wished to join them after all that you've witnessed. You died.")
                            ans = input("Restart Game? (Yes/No)").lower()
                            if ans == "yes":
                                print("RESTARTING...")
                                continue
                            else:
                                print("Thanks for playing :)")
                                break
                        elif answer == 2:
                            answer = int(input("You're in the stairway. \nWhich way do you go? \n2) Down \n"))

                # 2: cannibalism
                elif answer == 2:
                    print(
                        "You try to eat the organs, but quickly realize that they were infected. You died. Perhaps cannibalism isn't the option.")
                    ans = input("Restart Game? (Yes/No)").lower()
                    if ans == "yes":
                        print("RESTARTING...")
                        continue
                    else:
                        print("Thanks for playing :)")
                        break

    #2: cafeteria
    elif answer == 2:
        answer = int(input(
            "You walk down the hallway until you reach the cafeteria. It is connected to stairway. The cafeteria smells funky. You see that all the food here are just human organs...?! \nWhat do you do? \n1) Run to the stairway \n2) Eat the organs!"))
        # 1: stairway
        if answer == 1:
            answer = int(input("You're in the stairway. \nWhich way do you go? \n1) Up \n2) Down \n"))
            # 1: terrace
            if answer == 1:
                answer = int(input("You're in the Terrace. The stars look great tonight. There's nothing much here. \nWhat do you do? \n1) Jump off the building \n2)Head back. \n"))
                if answer == 1:
                    print("The stars looked pretty. You wished to join them after all that you've witnessed. You died.")
                    ans = input("Restart Game? (Yes/No)").lower()
                    if ans == "yes":
                        print("RESTARTING...")
                        continue
                    else:
                        print("Thanks for playing :)")
                        break
            #2: head back

        #2: cannibalism
        elif answer == 2:
            print("You try to eat the organs, but quickly realize that they were infected. You died. Perhaps cannibalism isn't the option.")
            ans = input("Restart Game? (Yes/No)").lower()
            if ans == "yes":
                print("RESTARTING...")
                continue
            else:
                print("Thanks for playing :)")
                break

    elif answer == 2:
        print("idk")

    else:
        print ("Idk what you're saying mate. Type 1 or 2")
