import random
num = random.randint(1,100)
user = int(input("Enter number: "))
count = 1 
while user != num:
    count += 1
    if user < num:
        print("too low!!!")
    else:
        print("too high!!!")
    user = int(input("guess again: "))
print(f"you win, and you guessed this number in {count} times")