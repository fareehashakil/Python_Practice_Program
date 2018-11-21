winning_no = 12
no = int(input("Enter any number for guessing game: "))
if no == winning_no:
    print("You win!!!")
else:
    if no < winning_no:
        print("Low!!!")
    else:
        print("High!!!")