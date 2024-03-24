# Accepting a sentence or paragraph from the user
input_text = input("Enter a sentence or paragraph: ")

# Removing punctuation and converting to lowercase
import string
input_text = input_text.translate(str.maketrans("", "", string.punctuation)).lower()

# Splitting the text into words
words = input_text.split()

# Creating a dictionary to store word frequencies
word_frequency = {}
print(word_frequency)
# Counting the frequency of each word
for word in words:
    if word in word_frequency:
        word_frequency[word] += 1
    else:
        word_frequency[word] = 1

# Displaying the result
print("\nWord Frequency Dictionary:")
for word, frequency in word_frequency.items():
    print(f"{word}: {frequency}")
