import csv
import os

# a) Function to insert a record into "Product.csv"
def Write_info():
    filename = "Product.csv"
    # Check if the file exists to avoid writing the header multiple times
    file_exists = os.path.exists(filename)
    
    # Input record details
    prod_id = input("Enter Product ID: ")
    prod_name = input("Enter Product Name: ")
    prod_price = float(input("Enter Product Price: "))
    prod_qty = int(input("Enter Product Quantity: "))
    
    # Write to the CSV file
    with open(filename, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        if not file_exists:
            # Write header row only once
            writer.writerow(["prod_id", "prod_name", "prod_price", "prod_qty"])
        writer.writerow([prod_id, prod_name, prod_price, prod_qty])
    
    print("Record inserted successfully.")

# b) Function to read and display all records from the CSV file
def Read_info():
    filename = "Product.csv"
    try:
        if not os.path.exists(filename):
            print("File does not exist.")
            return
        with open(filename, 'r') as csvfile:
            reader = csv.reader(csvfile, delimiter=';')
            records = list(reader)
            if len(records) <= 1:  # No data rows after the header
                print("No records found in the file.")
            else:
                print("Product Records:")
                for row in records:
                    print("; ".join(row))  # Print rows separated by semicolons
    except Exception as e:
        print(f"Error reading the file: {e}")

# Menu to execute the tasks
def menu():
    while True:
        print("\nMENU:")
        print("1. Insert a New Record (Retain previous data)")
        print("2. View all Records")
        print("3. Exit")
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            Write_info()
        elif choice == 2:
            Read_info()
        elif choice == 3:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the menu
menu()
