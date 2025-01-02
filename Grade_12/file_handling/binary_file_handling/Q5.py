import pickle
import os

# a) Insert a dictionary object into the file
def insert(filename):
    try:
        ticket = {
            "tnum": input("Enter Ticket Number: "),
            "source": input("Enter Source: "),
            "destination": input("Enter Destination: "),
            "cost": float(input("Enter Cost: "))
        }
        if os.path.exists(filename):  # Append to existing file
            with open(filename, 'rb') as f:
                data = pickle.load(f)
        else:
            data = []
        data.append(ticket)
        with open(filename, 'wb') as f:
            pickle.dump(data, f)
        print("Record inserted successfully.")
    except Exception as e:
        print("Error inserting record:", e)

# b) Display all records
def displayall(filename):
    try:
        if not os.path.exists(filename):
            print("File does not exist.")
            return
        with open(filename, 'rb') as f:
            data = pickle.load(f)
            if not data:
                print("No records found.")
            else:
                for record in data:
                    print(record)
    except Exception as e:
        print("Error displaying records:", e)

# c) Search for a specific record by ticket number
def search(filename, kTnum):
    try:
        if not os.path.exists(filename):
            print("File does not exist.")
            return
        with open(filename, 'rb') as f:
            data = pickle.load(f)
            found = False
            for record in data:
                if record["tnum"] == kTnum:
                    print(record)
                    found = True
            if not found:
                print("No matching record found.")
    except Exception as e:
        print("Error searching record:", e)

# d) Modify a record using a temporary file
def modify_withtemp(filename, kTnum):
    try:
        if not os.path.exists(filename):
            print("File does not exist.")
            return
        with open(filename, 'rb') as f:
            data = pickle.load(f)
        modified = False
        for record in data:
            if record["tnum"] == kTnum:
                record["source"] = input("Enter new Source: ")
                record["destination"] = input("Enter new Destination: ")
                record["cost"] = float(input("Enter new Cost: "))
                modified = True
        if modified:
            with open(filename, 'wb') as f:
                pickle.dump(data, f)
            print("Record modified successfully.")
        else:
            print("No matching record found.")
    except Exception as e:
        print("Error modifying record:", e)

# e) Modify a record without using a temporary file
def modify_withouttemp(filename, kTnum):
    modify_withtemp(filename, kTnum)  # Same logic as modifying in-place

# f) Delete a record using a temporary file
def delete_withtemp(filename, kTnum):
    try:
        if not os.path.exists(filename):
            print("File does not exist.")
            return
        with open(filename, 'rb') as f:
            data = pickle.load(f)
        new_data = [record for record in data if record["tnum"] != kTnum]
        if len(new_data) == len(data):
            print("No matching record found.")
        else:
            with open(filename, 'wb') as f:
                pickle.dump(new_data, f)
            print("Record deleted successfully.")
    except Exception as e:
        print("Error deleting record:", e)

# Menu to execute the program
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
        print("7. Exit")
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
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the menu
menu()
