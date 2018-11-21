def checknos(no1,no2,no3):
    if no1>no2 and no1>no3:
        return (f"{no1} is greater than {no2} and {no3}")
    elif no2>no3 and no2>no1:
        return (f"{no2} is greater than {no1} and {no3}")
    return (f"{no3} is greater than {no1} and {no2}")

no1 , no2, no3 = input("Enter 2 numbers: ").split(" ")

print(checknos(int(no1),int(no2),int(no3)))