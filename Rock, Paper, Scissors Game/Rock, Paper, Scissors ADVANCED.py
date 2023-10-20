import rpsmodule
# Main Program

# Main Loop
while True:
    # Replay until player is done.
    rpsmodule.welcomeMessage()

    # Score count for game
    playerScore = 0
    compScore = 0

    # Game loop
    while True:

        playerInput = rpsmodule.playerChoice()
        compInput = rpsmodule.computerChoice()

        whoWon = rpsmodule.Winner(playerInput, compInput)

        # Points added to player / computer
        if whoWon == "Player":
            playerScore += 1
            print("You won!\n")
        elif whoWon == "Computer":
            compScore += 1
            print("The computer won!\n")
        else:
            print("TIE!\n")

        print(f"The score is computer: {compScore}.")

        # Check for the winner
        if playerScore == 2:
            print("You won!")
            break
        elif compScore == 2:
            print("Computer won!")
            break

    print("Do you want to play again?")
    replay = input("y / n: ")

    if replay == "n":
        break

print("\nThank you for playing!")


