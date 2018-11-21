name= input("Enter your name: ")
l = len(name)
i = 0
temp = ""
while i < l:
    if name[i] in temp:
        pass
    else:
        print(f"{name[i]} : {name.count(name[i])}")
        temp += name[i]
    i += 1