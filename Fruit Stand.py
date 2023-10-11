dFruit = {
    1: {"name": "Apple", "price": 1.25},
    2: {"name": "Orange", "price": 1.15},
    3: {"name": "Banana", "price": 2.25}
}


def removeFruit():
    global dFruit
    listFruit()
    print("What would you like to remove?")
    intRem = int(input("Enter ID here: "))
    dFruit.pop(intRem)
    print("The Fruit has been removed.")


def addFruit():
    global dFruit
    print("Please enter the fruit you would like to add.")
    intId = int(input("What is the ID? "))
    strName = input("What's the name? ")
    flPrice = float(input("What is the price? "))
    dItem = {"name": strName, "price": flPrice}
    dFruit[intId] = dItem
    print(f"{strName} has been added.")


def listFruit():
    for intKey in dFruit:
        print(intKey, dFruit[intKey]["name"], dFruit[intKey]["price"])


print("Welcome to the fruit stand!")
while True:
    listFruit()
    print("What would you like to do?")
    intMenu = int(input("1 for Add Fruit. 2 for Remove Fruit: "))
    if (intMenu == 1):
        addFruit()
    elif (intMenu == 2):
        removeFruit()
    else:
        print("Sorry that's not an option")

    strMore = input("Would you like to do more? y/n: ")
    if (strMore == "n"):
        break
