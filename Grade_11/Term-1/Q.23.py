def count_elements(string): # Function to count the elements
    char_count = len(string) # Counting the characters
    space_count = string.count(' ') # Counting the spaces
    letter_count = sum(c.isalpha() for c in string) # Counting the letters
    digit_count = sum(c.isdigit() for c in string) # Counting the digits
    uppercase_count = sum(c.isupper() for c in string) # Counting the uppercase letters
    lowercase_count = sum(c.islower() for c in string) # Counting the lowercase letters
    special_count = char_count - letter_count - space_count - digit_count # Counting the special characters
    word_count = len(string.split())

    print("No. of Characters:", char_count)
    print("No. of Spaces:", space_count)
    print("No. of Letters (Alphabet):", letter_count)
    print("No. of Digits:", digit_count)
    print("No. of Upper-Case Letters:", uppercase_count)
    print("No. of Lower-Case Letters:", lowercase_count)
    print("No. of Special Characters:", special_count)
    print("No. of Words:", word_count)


# Accepting input from the user
input_string = input("Enter a string: ") 

# Counting and printing the elements
count_elements(input_string)