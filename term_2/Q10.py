def find_longest_word(word_list):
    if not word_list:
        return None, 0

    longest_word = max(word_list, key=len)
    length_of_longest_word = len(longest_word)

    return longest_word, length_of_longest_word

# Input: List of words
word_list = input("Enter a list of words separated by space: ").split()

# Finding the longest word and its length
longest_word, length_of_longest_word = find_longest_word(word_list)

# Displaying the result
if longest_word:
    print("Longest word:", longest_word)
    print("Length of the longest word:", length_of_longest_word)
else:
    print("No words entered.")
