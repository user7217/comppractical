def print_alternate_characters(input_string):
    result = ""
    for i in range(0, len(input_string), 2): 
        result += input_string[i] # Add the character at index i to the result string
    print("Alternate characters:", result)

# Get input from the user
user_input = input("Enter a string: ")

# Call the function to print alternate characters
print_alternate_characters(user_input)
