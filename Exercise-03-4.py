num = input("Enter number: ")
l = len(num)
i = 0
sum = 0
while i < l:
    sum += int(num[i]) 
    i += 1
print(f"Sum is {sum}")
