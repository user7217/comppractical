user_input = input("Enter a string: ")
words = user_input.split()
if words:
    longest = max(words, key=len)
    shortest = min(words, key=len)
    print(f"Longest word: {longest}, shortest word: {shortest}")
else:
    print("No words entered.")


    