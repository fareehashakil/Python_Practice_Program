# Object:
#   Lets play a guessing game using nested if statement!
#   Ask the user to enter any number and if its the winning number
#   print You win!!
  
  
# Source Code:
winning_no = 12
no = int(input("Enter any number for guessing game: "))
if no == winning_no:
    print("You win!!!")
else:
    if no < winning_no:
        print("Low!!!")
    else:
        print("High!!!")
