def count_file_content(file_path):
    uppercase, digits = 0, 0
    with open(file_path, 'r') as file:
        for line in file:
            uppercase += sum(1 for c in line if c.isupper())
            digits += sum(1 for c in line if c.isdigit())
    return uppercase, digits

def make_copy(original_path, copy_path):
    with open(original_path, 'r') as original_file:
        with open(copy_path, 'w') as copy_file:
            copy_file.write(original_file.read())

def main():
    file_path = 'word.txt'
    copy_file_path = 'word2.txt'

    while True:
        print("\nMenu:")
        print("1. Add fresh contents to file")
        print("2. Make a Copy of the file")
        print("3. Display (contents of original file, copied file & counters)")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            with open(file_path, 'a') as file:
                print("Enter text to add (type 'done' to stop):")
                while True:
                    line = input()
                    if line.lower() == 'done': break
                    file.write(line + '\n')

        elif choice == '2':
            make_copy(file_path, copy_file_path)
            print(f"File copied to {copy_file_path}")

        elif choice == '3':
            try:
                with open(file_path, 'r') as original, open(copy_file_path, 'r') as copy:
                    print("\nContents of original file:")
                    print(original.read())
                    print("\nContents of copied file:")
                    print(copy.read())

                uppercase, digits = count_file_content(file_path)
                print(f"\nUppercase letters: {uppercase}")
                print(f"Digits: {digits}")
            except FileNotFoundError:
                print("File not found.")

        elif choice == '4':
            break

if __name__ == "__main__":
    main()
