def count_file_content(file_path):
    spaces, digits, words, lines = 0, 0, 0, 0
    with open(file_path, 'r') as file:
        for line in file:
            lines += 1
            words_in_line = line.split()
            words += len(words_in_line)
            spaces += line.count(' ')
            digits += sum(c.isdigit() for c in line)
    return spaces, digits, words, lines

def main():
    file_path = r'D:\Exam\word.txt'
    while True:
        print("\n1. Add contents\n2. Display contents\n3. Exit")
        choice = input("Choose an option: ")
        
        if choice == '1':
            with open(file_path, 'a') as file:
                while True:
                    line = input("Enter text (type 'done' to stop): ")
                    if line.lower() == 'done': break
                    file.write(line + '\n')
        elif choice == '2':
            try:
                with open(file_path, 'r') as file:
                    print("\nFile contents:\n" + file.read())
                spaces, digits, words, lines = count_file_content(file_path)
                print(f"\nSpaces: {spaces}, Digits: {digits}, Words: {words}, Lines: {lines}")
            except FileNotFoundError:
                print("File not found.")
        elif choice == '3':
            break

if __name__ == "__main__":
    main()
