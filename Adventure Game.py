# Adventure Game
# A family project to save the dragon prince!

print("A HERO'S QUEST")
print("You set forth on a journey to save the dragon prince, as you come to a fork in the road on your trusted steed, Buttercup.")

# FIRST CHOICE added prints for line breaks for easier reading
print()
print("You could take the fork on the RIGHT? It has a weird-looking symbol in the color of black on the sign.")
print("You could take the fork on the LEFT? It has a weird-looking symbol in the color of blue on the sign.")

first_choice = input("Which route do you choose to go? (RIGHT or LEFT): ").lower()

if first_choice == "right":
    print()
    print("You take the fork on the RIGHT.")

    #  SECOND CHOICE (RIGHT PATH) or (BLACK SIGN)
    second_choice = input("As you ride your way on the right fork, you decide you should: PULL OUT YOUR SWORD or RIDE FASTER? ").lower()

    if second_choice == "pull out your sword":
        print()
        print(f"As you {second_choice}, you yell a perfectly pitched battle cry.")
        
        # THIRD CHOICE (SWORD PATH)
        third_choice = input("I AM SO AWESOME, I AM COMING YOUNG DRAGON, or I WANT MY MOMMY? ").lower()

        if third_choice == "i am so awesome":
            print()
            print("In your moment of self-praise, you don't see the orc in the trees. An arrow to the knee ends your journey. Game Over.")

        elif third_choice == "i want my mommy":
            print()
            print("You ride home as fast as you can to cry to your mummy about how your journey never even began... Game Over.")

        elif third_choice == "i am coming young dragon":
            print()
            print("You are powered by the knights of old and ride to save the young dragon, who hasn't even had a chance to begin his journey.")

            # FOURTH CHOICE (CASTLE APPROACH)
            fourth_choice = input("Ahead, you see a ruined tower guarded by shadow wolves. Do you: CHARGE, SNEAK, or CAST A SPELL? ").lower()

            if fourth_choice == "charge":
                print()
                print("Your boldness inspires fear in the wolves. They scatter, and you ascend the tower to find the dragon prince. Victory!")

            elif fourth_choice == "sneak":
                print()
                print("You try to sneak past, but a twig snaps underfoot. The wolves attack. Game Over.")

            elif fourth_choice == "cast a spell":
                print()
                print("You summon a glowing barrier. The wolves cower, and you safely reach the top. The dragon prince is saved!")

            else:
                print()
                print("You hesitate and are overwhelmed by the wolves. Game Over.")
        else:
            print()
            print("That was not a valid option. The moment of confusion is your undoing. Game Over.")

    elif second_choice == "ride faster":
        print()
        print(f"You {second_choice} and see the trees blur past you as you find yourself deep into the night sky in a desert-sanded Arabian night.")
        third_choice = input("As you travel, you start to see the ground moving... Do you: RIDE HARDER, STOP, or THROW MAGIC STONE? ").lower()

        if third_choice == "ride harder":
            print()
            print("Your horse becomes lightning! You burst through a hidden barrier and find the dragon prince asleep in a dream realm. Victory!")
        elif third_choice == "stop":
            print()
            print("Stopping was a mistake. Quicksand engulfs you. Game Over.")
        elif third_choice == "throw magic stone":
            print()
            print("The ground explodes into light, revealing a path straight to the tower. The dragon prince is saved!")
        else:
            print()
            print("You hesitate, and the desert consumes your fate. Game Over.")
    else:
        print()
        print("Your indecision leads to doom. A shadow knight ends your tale. Game Over.")

elif first_choice == "left":
    print()
    print("You take the fork on the LEFT.")

    # SECOND CHOICE (LEFT PATH) or (BLUE SIGN)
    second_choice = input("As you ride your way on the left fork, you decide you should: PULL OUT A BOW or RIDE FASTER? ").lower()

    if second_choice == "pull out a bow":
        print()
        print(f"As you {second_choice}, you ready your aim for danger ahead.")
        third_choice = input("Do you SHOOT ARROWS INTO THE AIR, AIM AT A BUSH, or HOLD YOUR FIRE? ").lower()

        if third_choice == "shoot arrows into the air":
            print()
            print("Your arrows signal a hidden ally, who joins your quest. You ride on with a companion and find the dragon prince!")
        elif third_choice == "aim at a bush":
            print()
            print("A goblin was hiding! You take it out and earn safe passage. Onward to the prince!")
        elif third_choice == "hold your fire":
            print()
            print("A hidden enemy ambushes you. Without your bow ready, you're captured. Game Over.")
        else:
            print()
            print("Confused hesitation leads to chaos. You fall off Buttercup. Game Over.")

    elif second_choice == "ride faster":
        print()
        print("You gallop forward recklessly and reach a shimmering lake.")
        third_choice = input("Do you DRINK the water, LOOK INTO the lake, or TURN BACK? ").lower()

        if third_choice == "drink":
            print()
            print("The water was cursed! You fall asleep for 100 years. Game Over.")
        elif third_choice == "look into":
            print()
            print("A vision shows you the dragon prince's location. You race toward it with hope!")
        elif third_choice == "turn back":
            print()
            print("You flee from destiny. The dragon prince remains lost. Game Over.")
        else:
            print()
            print("You lose your way in indecision. Buttercup sighs. Game Over.")
    else:
        print()
        print("Your choices lacked conviction. A blue mist carries you into a dreamless sleep. Game Over.")

else:
    print()
    print("You didn't select any path. You don't save the dragon prince. Game Over... this ending seems to be not the heroic adventure you wanted.")
