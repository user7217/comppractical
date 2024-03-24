def check_password_validity(password):
    return all([
        any(char.islower() for char in password),
        any(char.isupper() for char in password),
        any(char.isdigit() for char in password),
        any(char in '$#@' for char in password),
        5 <= len(password) <= 15
    ])

# Accept password from the user
user_password = input("Enter your password: ")

# Check validity and print the result
if check_password_validity(user_password):
    print("Password is Valid")
else:
    print("Password is Invalid")
