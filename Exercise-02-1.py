# Object:
#   Take 3 input in a single line then calculate the average of them and print it using formatting 3.6.



# Source Code:
val1, val2, val3 = input("Enter 3 values for taking average : ").split(" ")
val = (int(val1) + int(val2) + int(val3) ) // 3
print(f"The average of {val1} , {val2} and {val3} is {val}")
