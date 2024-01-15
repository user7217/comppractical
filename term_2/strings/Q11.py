def main():
    user_input = input("Enter a string: ")
    
    filtered_words = [word for word in user_input.split() if word.startswith('a') and word.endswith('e')]
    
    if filtered_words:
        print("Words starting with 'a' and ending with 'e':", *filtered_words)
    else:
        print("No matching words found.")

if __name__ == "__main__":
    main()
