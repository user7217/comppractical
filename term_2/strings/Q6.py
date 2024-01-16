user_input = input("Enter a string: ")
print("Alternate words:", ', '.join(user_input.split()[::2]))

