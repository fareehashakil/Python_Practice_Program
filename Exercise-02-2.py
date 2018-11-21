name, age = input("Enter name and age: ").split(" ")
namee = name.lower()
pos = namee.find("a")
if  pos == 0 and int(age) > 10:
    print("You can watch coco movie..")
else:
    print("Sorry, You cannot watch coco movie!!")