Object:
    To chek whether the entered string is a palindrome or not.
    
    
    Palindrome:
        Palindrome is a word which spell same in forward as well as reverse order.
        E.g. madam, afifa etc. 

    
    
    
Sourcce Code:
def Palindrome(str):
    name = str[::-1]
    if name == str:
        return True
    return False

print(Palindrome(input("Enter name: ")))
