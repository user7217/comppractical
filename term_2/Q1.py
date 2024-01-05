import random

# Function to create a new list
def create_list():
    global my_list
    my_list = []
    print("New list created.")

# Function to append a random 4-digit integer to the list
def append_random():
    random_num = random.randint(1000, 9999)
    my_list.append(random_num)
    print(f"Random 4-digit number {random_num} appended to the list.")

# Function to extend the list
def extend_list():
    extension = input("Enter elements to extend the list (comma-separated): ").split(',')
    extension = [int(elem.strip()) for elem in extension]
    my_list.extend(extension)
    print("List extended.")

# Function to insert an element at a particular position in the list
def insert_element():
    pos = int(input("Enter position to insert the element: "))
    elem = int(input("Enter the element to insert: "))
    my_list.insert(pos, elem)
    print(f"Element {elem} inserted at position {pos}.")

# Function to remove elements from the list
def remove_element():
    print("Select an option to remove an element:")
    print("1. Remove last element")
    print("2. Remove element at a particular position")
    print("3. Remove the first occurrence of an element")
    choice = input("Enter your choice: ")

    if choice == '1':
        if len(my_list) > 0:
            removed_element = my_list.pop()
            print(f"Removed last element: {removed_element}")
        else:
            print("List is empty.")
    elif choice == '2':
        pos = int(input("Enter position to remove the element: "))
        if 0 <= pos < len(my_list):
            removed_element = my_list.pop(pos)
            print(f"Removed element at position {pos}: {removed_element}")
        else:
            print("Invalid position.")
    elif choice == '3':
        elem = int(input("Enter the element to remove: "))
        if elem in my_list:
            my_list.remove(elem)
            print(f"Removed first occurrence of element {elem}.")
        else:
            print("Element not found in the list.")
    else:
        print("Invalid choice.")

# Function to print largest and smallest elements in the list
def print_largest_smallest():
    if len(my_list) > 0:
        print(f"Largest element: {max(my_list)}")
        print(f"Smallest element: {min(my_list)}")
    else:
        print("List is empty.")

# Function to find second largest and second smallest elements in the list
def find_second_largest_smallest():
    if len(my_list) > 1:
        sorted_list = sorted(set(my_list))
        if len(sorted_list) > 1:
            print(f"Second largest element: {sorted_list[-2]}")
            print(f"Second smallest element: {sorted_list[1]}")
        else:
            print("Not enough elements in the list.")
    else:
        print("Not enough elements in the list.")

# Function to sort the list in ascending or descending order
def sort_list():
    print("Select sorting order:")
    print("1. Sort in ascending order")
    print("2. Sort in descending order")
    choice = input("Enter your choice: ")

    if choice == '1':
        sorted_asc = sorted(my_list)
        print(f"Sorted list in ascending order: {sorted_asc}")
    elif choice == '2':
        sorted_desc = sorted(my_list, reverse=True)
        print(f"Sorted list in descending order: {sorted_desc}")
    else:
        print("Invalid choice.")

# Function to reverse the elements of the list
def reverse_list():
    reversed_list = my_list[::-1]
    print(f"Reversed list: {reversed_list}")

# Function to clear the list
def clear_list():
    global my_list
    my_list = []
    print("List cleared.")

# Main program
my_list = []

while True:
    print("\nMenu:")
    print("a. Create a List")
    print("b. Append a random 4 digit integer into the list")
    print("c. Extend the list")
    print("d. Insert an element into a list at a particular position")
    print("e. Remove an element from the list")
    print("f. Print the largest element and smallest element in the list")
    print("g. Find the second largest and second smallest element in the list")
    print("h. Sort the list in ascending or descending order")
    print("i. Reverse the elements of a list")
    print("j. Clear the list")
    print("k. Exit")

    choice = input("Enter your choice: ").lower()

    if choice == 'a':
        create_list()
    elif choice == 'b':
        append_random()
    elif choice == 'c':
        extend_list()
    elif choice == 'd':
        insert_element()
    elif choice == 'e':
        remove_element()
    elif choice == 'f':
        print_largest_smallest()
    elif choice == 'g':
        find_second_largest_smallest()
    elif choice == 'h':
        sort_list()
    elif choice == 'i':
        reverse_list()
    elif choice == 'j':
        clear_list()
    elif choice == 'k':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a valid option.")
