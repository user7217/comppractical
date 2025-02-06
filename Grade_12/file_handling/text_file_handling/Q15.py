try:
    with open("poem.txt") as f:
        data = f.read()
        words = data.split()
        word_freq = {}

        for word in words:
            word_freq[word] = word_freq.get(word, 0) + 1  # Use get to avoid KeyError

        # Attempt to access word frequencies for "and" and "is"
        and_count = word_freq.get("and", 0)  # Defaults to 0 if "and" is not found
        is_count = word_freq.get("is", 0)  # Defaults to 0 if "is" is not found

        print(f"'and' appears {and_count} times.")
        print(f"'is' appears {is_count} times.")

except FileNotFoundError:
    print("Error: The file 'poem.txt' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")
