#Program Wordle or word game

#Store a secret word and guess count
secret = "link"
guess_count = 0
guess = -1

print ("Welcome to the word guessing game!")
print()

keep_playing = "yes"
while keep_playing == "yes":
    #Ok here is where I will start the blank hint loop
    initial_hint = "_ " * len(secret)
    print (f"Your hint is:_ _ _ _")

    secret_guess = ""
    while secret_guess != secret:
        secret_guess = input(f"What is your guess? ").lower()

        #check for the correct length this one was rough
        if len(secret_guess) != len(secret):
            print(f"Your guess must be {len(secret)} letters long.")
            continue

        guess_count = guess_count + 1
        
        if secret_guess == secret:
            print ("You Win! ")
        else:
            #My code to attempt to have the hint show based on rules
            hint = ""
            for i in range(len(secret)):   
                    if secret_guess[i] == secret[i]:
                        hint += secret_guess[i].upper() + " "
                    elif secret_guess[i] in secret:
                        hint += secret_guess[i].lower() + " "
                    else:
                         hint += "_ "
            print("Hint:", hint.strip())    #found strip from the python library seemed appropriate to use this to remove any excess spaces.
            print ("Incorrect Try again")

        print (f"It took you {guess_count} guesses")

    keep_playing = input("Would you like to play agian (yes/no)? ")
    if keep_playing == "yes":
         guess_count = 0
         print()
