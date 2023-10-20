import random


# functions

def welcomeMessage():
    print("#" * 80)
    print("ROCK, PAPER, SCISSORS!")
    print("#" * 80)
    print("\n\n")


def playerChoice():
    while True:
        playerInput = input("(R)ock, (P)aper, (S)cissors: ")
        playerInput = playerInput.lower().strip()
        if playerInput == "r" or playerInput == "rock":
            strReturn = "r"
            break
        elif playerInput == "p" or playerInput == "paper":
            strReturn = "p"
            break
        elif playerInput == "s" or playerInput == "scissors":
            strReturn = "s"
            break
        else:
            strReturn = ("\nInput is invalid. Please enter (R), (P), or (S).")

    return playerInput


def computerChoice():
    lisGuesses = ["r", "p", "s"]
    return random.choice(lisGuesses)


def Winner(strPlayer, strComp):
    print(f"\nYou chose {strPlayer}")
    print(f"Computer chose {strComp}\n")
    if strPlayer == strComp:
        print("It's a tie!")
    else:
        if strPlayer == "r":
            if strComp == "p":
                return "Computer"
            elif strComp == "s":
                return "Player"
        elif strPlayer == "p":
            if strComp == "s":
                return "Computer"
            elif strComp == "r":
                return "Player"
        elif strPlayer == "s":
            if strComp == "r":
                return "Computer"
            elif strComp == "p":
                return "Player"

    return "Tie"