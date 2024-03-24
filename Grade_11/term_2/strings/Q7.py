def print_words_starting_with_vowel(input_string):
    words = input_string.split()
    vowel_words = [word for word in words if word[0].lower() in 'aeiou']
    print("Words starting with a vowel:", ', '.join(vowel_words))

# Get input from the user
user_input = input("Enter a string: ")

# Call the function to print words starting with a vowel
print_words_starting_with_vowel(user_input)

