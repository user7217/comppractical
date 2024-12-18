def main():
    # Step 1: Accept n names from the user and store them in "nameslist.txt"
    n = int(input("Enter the number of names you want to input: "))
    with open("nameslist.txt", 'w') as file:
        for i in range(n):
            name = input(f"Enter name {i+1}: ")
            file.write(name + '\n')

    # Step 2: Display the contents of the "nameslist.txt"
    with open("nameslist.txt", 'r') as file:
        print("\nContents of 'nameslist.txt':")
        print(file.read())

    # Step 3: Create a new file "lexical_nameslist.txt" that stores the names sorted lexicographically
    with open("nameslist.txt", 'r') as file:
        names = file.readlines()
        names.sort()  # Sort the names lexicographically

    with open("lexical_nameslist.txt", 'w') as file:
        file.writelines(names)

    # Step 4: Display the contents of "lexical_nameslist.txt"
    with open("lexical_nameslist.txt", 'r') as file:
        print("\nContents of 'lexical_nameslist.txt':")
        print(file.read())

if __name__ == "__main__":
    main()
