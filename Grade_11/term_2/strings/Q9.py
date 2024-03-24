def print_alternate_words_of_length(input_string, target_length=5):
    words = input_string.split()
    selected_words = [word for i, word in enumerate(words) if i % 2 == 0 and len(word) == target_length]
    print(f"Alternate words of length {target_length}:", ', '.join(selected_words))

# Get input from the user
user_input = input("Enter a string: ")

# Call the function to print alternate words of length 5
print_alternate_words_of_length(user_input, target_length=5)

