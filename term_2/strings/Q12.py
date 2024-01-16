def main():
    user_input = input("Enter a string: ")
    
    words_with_vowels = [word for word in user_input.split() if any(char in "aeiouAEIOU" for char in word)]
    
    print("Words with vowels:", *words_with_vowels) if words_with_vowels else print("No words with vowels found.")

if __name__ == "__main__":
    main()

    
