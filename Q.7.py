#check if letter digit space or special character
char = input("Enter a character: ")
if char.isalpha(): #if the character is a letter 
    print("Letter")
elif char.isdigit(): #if the character is a digit
    print("Digit")
elif char.isspace(): #if the character is a space
    print("Space")
else: #if the character is a special character
    print("Special character")