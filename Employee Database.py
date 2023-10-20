Employees = {
    1: {"name": "Jort", "job": "Manager"},
    2: {"name": "Steve", "job": "Janitor"},
    3: {"name": "Marc", "job": "Owner"}
}


def fireEmployees():
    global Employees
    listEmployees()
    print("What would you like to remove?")
    intRem = int(input("Enter ID here: "))
    Employees.pop(intRem)
    print("They have been fired.")


def hireEmployees():
    global Employees
    print("Please enter who you would like to hire.")
    intId = int(input("What is their ID?: "))
    strName = input("What is their name?: ")
    strJob = (input("What is their job?: "))
    dHire = {"name": strName, "job": strJob}
    Employees[intId] = dHire
    print(f"{strName} has been added.")


def listEmployees():
    for intKey in Employees:
        print(intKey, Employees[intKey]["name"], Employees[intKey]["job"])


print("Welcome to Indeed.com!")
while True:
    listEmployees()
    print("What would you like to do?")
    intMenu = int(input("1 for Hire. 2 for Fire: "))
    if (intMenu == 1):
        hireEmployees()
    elif (intMenu == 2):
        fireEmployees()
    else:
        print("Sorry that's not an option")

    strMore = input("Would you like to do more? y/n: ")
    if (strMore == "n"):
        break
