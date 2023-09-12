# Imported random module.
import random

flag = True
attempts = 0
remainingGuesses = 3
intSecret = random.randint(1, 10)
# Welcomes user, and explains the rules.

print("WELCOME to my number guessing game!".center(80))
print(" Guess my number 1 - 10. *ONLY 3 TRIES* ")

# While loop to continue game.
while(flag == True):
    while (attempts < 3):
        intGuess = int(input(" What is your guess?: "))
        if (intGuess == intSecret):
            # Winner
            remainingGuesses -= 1
            attempts += 1
            print(" You win! :) ")
            print(remainingGuesses, "guess(es) remaining")
            break
        else:
            # Loser
            remainingGuesses -= 1
            attempts += 1
            print(remainingGuesses, "guess(es) remaining")
            print(" You lose! :( ")
# Prompt user to play again.
    playAgain = input("\nWould you like to play again? y/n: ")
    if (playAgain == "y"):
        attempts = 0
        remainingGuesses = 3
        flag = True
    elif (playAgain == "n"):
        print("Thank you for playing!")
        flag = False
    else:
        print("Please enter y/n")
