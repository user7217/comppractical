def ReplaceAll(content, oldword, newword):
    # Replace all occurrences of oldword with newword in the content
    return content.replace(oldword, newword)

def main():
    # Step 1: Get file path from the user
    file_path = input("Enter the file path: ")
    
    try:
        # Open the file and display its contents
        with open(file_path, 'r') as file:
            content = file.read()
            print("\nOriginal Content of the File:")
            print(content)
        
        # Step 2: Get the oldword and newword from the user
        oldword = input("\nEnter the word to replace: ")
        newword = input("Enter the new word: ")

        # Call the ReplaceAll function
        changed_content = ReplaceAll(content, oldword, newword)

        # Step 3: Display the changed content
        print("\nChanged Content:")
        print(changed_content)

    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")

if __name__ == "__main__":
    main()
