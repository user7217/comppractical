import pickle
import os

# Function to delete all records where Source is "Delhi" and Destination is "Mumbai"
def delete_delhi_mumbai(filename):
    try:
        if not os.path.exists(filename):
            print("File does not exist.")
            return
        with open(filename, 'rb') as f:
            data = pickle.load(f)
        
        original_count = len(data)
        data = [record for record in data if not (record["source"] == "Delhi" and record["destination"] == "Mumbai")]
        
        if len(data) == original_count:
            print("No records with Source='Delhi' and Destination='Mumbai' found.")
        else:
            with open(filename, 'wb') as f:
                pickle.dump(data, f)
            print("Records with Source='Delhi' and Destination='Mumbai' have been deleted.")
    except Exception as e:
        print(f"Error: {e}")

# Function to display the number of records in the file
def count_records(filename):
    try:
        if not os.path.exists(filename):
            print("File does not exist.")
            return
        with open(filename, 'rb') as f:
            data = pickle.load(f)
            print(f"Number of records in the file: {len(data)}")
    except Exception as e:
        print(f"Error: {e}")

# Function to increase the cost of all tickets by 20%
def increase_cost(filename):
    try:
        if not os.path.exists(filename):
            print("File does not exist.")
            return
        with open(filename, 'rb') as f:
            data = pickle.load(f)
        
        if not data:
            print("No records found in the file.")
        else:
            for record in data:
                record["cost"] *= 1.20  # Increase cost by 20%
            with open(filename, 'wb') as f:
                pickle.dump(data, f)
            print("Ticket costs increased by 20%.")
    except Exception as e:
        print(f"Error: {e}")

# Menu to implement the functionalities
def menu():
    filename = "traTicket.dat"
    while True:
        print("\nMENU:")
        print("1. Insert a New Ticket Record")
        print("2. View all Records")
        print("3. Search a particular Ticket")
        print("4. Modify Ticket Details (Using Temporary File)")
        print("5. Modify Ticket Details (Without Using Temporary File)")
        print("6. Delete a record")
        print("7. Delete all records where Source='Delhi' and Destination='Mumbai'")
        print("8. Display the number of records in the file")
        print("9. Increase ticket costs by 20%")
        print("10. Exit")
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            insert(filename)
        elif choice == 2:
            displayall(filename)
        elif choice == 3:
            kTnum = input("Enter Ticket Number to search: ")
            search(filename, kTnum)
        elif choice == 4:
            kTnum = input("Enter Ticket Number to modify: ")
            modify_withtemp(filename, kTnum)
        elif choice == 5:
            kTnum = input("Enter Ticket Number to modify: ")
            modify_withouttemp(filename, kTnum)
        elif choice == 6:
            kTnum = input("Enter Ticket Number to delete: ")
            delete_withtemp(filename, kTnum)
        elif choice == 7:
            delete_delhi_mumbai(filename)
        elif choice == 8:
            count_records(filename)
        elif choice == 9:
            increase_cost(filename)
        elif choice == 10:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the menu
menu()
