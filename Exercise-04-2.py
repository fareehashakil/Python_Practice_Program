def Palindrome(str):
    name = str[::-1]
    if name == str:
        return True
    return False

print(Palindrome(input("Enter name: ")))