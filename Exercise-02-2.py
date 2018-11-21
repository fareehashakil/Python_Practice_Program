# Object:
#     To take user's name and age input and allow user to watch movie 
#     if the first alphabet of user's name is 'A' or 'a' 
#     and age is greater than 10 by using If and Else statements.


name, age = input("Enter name and age: ").split(" ")
namee = name.lower()
pos = namee.find("a")
if  pos == 0 and int(age) > 10:
    print("You can watch coco movie..")
else:
    print("Sorry, You cannot watch coco movie!!")
