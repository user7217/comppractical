#count frequency of words
user_input = input("Enter a string: ")
words = user_input.split()
word_freq = {}
for word in words:
    word_freq[word] = word_freq.get(word, 0) + 1
print("Word frequency:", word_freq)
word_and_count = word_freq.get("and", 0)
word_is_count = word_freq.get("is", 0)
print(f"Frequency of 'and': {word_and_count}, frequency of 'is': {word_is_count}")