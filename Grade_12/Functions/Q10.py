def check_password_validity(password):
    has_lower = False
    has_upper = False
    has_digit = False
    has_special = False

    for char in password:
        if char.islower():
            has_lower = True
        elif char.isupper():
            has_upper = True
        elif char.isdigit():
            has_digit = True
        elif char in '$#@':
            has_special = True

    return has_lower and has_upper and has_digit and has_special and 5 <= len(password) <= 15

user_password = input("Enter your password: ")

if check_password_validity(user_password):
    print("Password is Valid")
else:
    print("Password is Invalid")
