# Object:
#   Take name as an input from user and a character to count how many
#   times it will appear in his or her name.
  
  
# Source Code:
name, char = input("Enter your name and Enter character u want to count: ").split(" ")
cou1 = name.count(char.upper())
cou2 = name.count(char.lower())
print(f"Hi {name}, your name's length is {len(name)} and {char} appears {cou1+cou2} times.")
