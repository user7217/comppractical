def is_palindrome(word):
    return word == "".join(reversed(word))

def print_palindrome_words(input_string):
    words = input_string.split()
    palindrome_words = [word for word in words if is_palindrome(word)]
    print("Palindrome words:", ', '.join(palindrome_words))

# Get input from the user
user_input = input("Enter a string: ")

# Call the function to print palindrome words
print_palindrome_words(user_input)
