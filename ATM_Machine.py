# Marc A Felicidario
# 09 / 20 / 2023
# COMP B10

# A simple ATM Machine program.

# start with some $$
checking = 3345.68
savings = 10000.00

# Welcome UI Message
print("#"*80)
print("Welcome to the ATM")
print("#"*80)

# create a loop for the program; contiuously run the program
while (True):

    #Show the menu options
    print("Choose an option: \n1 - Deposit   2 - Withdraw   3 - View Balance\n")
    # Ask the user for their choice
    menu = input("What would you like to do? -> ")

    if (menu == "1"):
        print("You want to make a deposit.")
        # ask for account
        accType = input("c. Checking OR s. Savings -> ")

        # ask for amount
        if (accType == "c"):          
            chkDep = float(input("How much would you like deposit?: $"))
            #total = chkDep + checking
            #print(round(total, 2))
            checking += chkDep      #append user deposit amount to checking
            newChkBal = round(checking, 2)
            print(f"Checking Balance: ${newChkBal}")
        elif (accType == "s"):
            savDep = float(input("How much would you like deposit?: $"))
            savings += savDep      #append user deposit amount to savings
            newSavBal = round(savings, 2)
            print(f"Savings Balance: ${newSavBal}")
        else:
            print("Please Enter c. Checking OR s. Savings")
            continue

    elif (menu == "2"):
        print("You want to make a withdrawal.")
        accType = input("c. Checking OR s. Savings -> ")
        if (accType == "c"):          
            chkWit = float(input("How much would you like to withdrawal?: $"))
            checking -= chkWit      #pop user withdrawal amount to checking
            newChkWit = round(checking, 2)
            print(f"Checking Balance: ${newChkWit}")
        elif (accType == "s"):
            savWit = float(input("How much would you like withdrawal?: $"))
            savings -= savWit      #pop user withdrawal amount to savings
            newSavWit = round(savings, 2)
            print(f"Savings Balance: ${newSavWit}")
        else:
            print("Please Enter c. Checking OR s. Savings")
            continue
    
    elif (menu == "3"):
        print("You want to check a balance.")
        accType =  input("c. Checking OR s. Savings -> ")
        if (accType == "c"):
            newChkBal = round(checking, 2)
            print(f"Checking Balance: ${newChkBal}")
        elif (accType == "s"):
            newSavBal = round(savings, 2)
            print(f"Savings Balance: ${newSavBal}")
        else:
            print("Please Enter c. Checking OR s. Savings")
            continue


    else:
        print ("Sorry - that's not a valid choice")

    print("")
    strMore = input("Would you like to perform another transaction? ")

    if (strMore != "y"):
        break
