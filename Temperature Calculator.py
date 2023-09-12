#(°F − 32) × 5/9 = °C
#(°C × 9/5) + 32 = °F

# Show the UI
print("#" * 80)
print("#" * 9, " " * 60, "#"*9)
print("#" * 9, "Advanced Calculator".center(60), "#" * 9)
print("#" * 9, " " * 60, "#"*9)
print("#" * 80)

# Welcome the user
print("#" * 9, "Welcome User!".center(60), "#" * 9)
print("#" * 9, "(1) Celsius --> Fahrenheit".center(60), "#" * 9)
print("#" * 9, "(2) Fahrenheit --> Celsius".center(60), "#" * 9)
print("#" * 80, "\n")

select = input("Please select what you would like to calculate: ")

# Get input from the user.
# if the user chooses 1, do C to F
# ask for degrees in C
# do the calculation
if(select == "1"):
   cDegrees = int(input("Enter degrees in C: "))
   resultC = (cDegrees * 9/5 + 32)
   print(round(resultC))

# if the user chooses 2, do F to C
elif(select == "2"):
   fDegrees = int(input("Enter degrees in F: "))
   resultF = ((fDegrees - 32) * 5/9)
   print(round(resultF))

# if the user enters anything else, give an error message
else: print("! Please choose an option from the menu !")

