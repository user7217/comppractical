#menu driven program to print pattern based on users choice using nested loop
def display_pattern(num_rows):
    for i in range(1, num_rows + 1):
        for j in range(1, i + 1):
            print("*", end=" ")
        print()

def menu():
    print("Pattern Options:")
    print("1. Right Triangle")
    print("2. Inverted Right Triangle")
    print("3. Pyramid")
    print("4. Inverted Pyramid")
    print("5. Exit")
  
    choice = int(input("Enter your choice (1-5): "))
  
    if choice == 1:
        rows = int(input("Enter the number of rows: "))
        display_pattern(rows)
    elif choice == 2:
        rows = int(input("Enter the number of rows: "))
        for i in range(rows, 0, -1):
            for j in range(1, i + 1):
                print("*", end=" ")
            print()
    elif choice == 3:
        rows = int(input("Enter the number of rows: "))
        for i in range(1, rows + 1):
            print(" " * (rows - i) + "* " * i)
    elif choice == 4:
        rows = int(input("Enter the number of rows: "))
        for i in range(rows, 0, -1):
            print(" " * (rows - i) + "* " * i)
    elif choice == 5:
        print("Exiting the program...")
        return
    else:
        print("Invalid choice! Please enter a valid option.")
  
    menu()

# Calling the menu function to start the program
menu()