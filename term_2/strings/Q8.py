def print_alternate_words_starting_with_digit(input_string):
    words = input_string.split()
    selected_words = [word for i, word in enumerate(words) if i % 2 == 0 and word[0].isdigit()]
    print("Alternate words starting with a digit:", ', '.join(selected_words))

# Get input from the user
user_input = input("Enter a string: ")

# Call the function to print alternate words starting with a digit
print_alternate_words_starting_with_digit(user_input)

#print("Alternate words starting with a digit:", ', '.join([word for i, word in enumerate(input("Enter a string: ").split()) if i % 2 == 0 and word[0].isdigit()]))
