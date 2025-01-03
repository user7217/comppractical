import csv

#a) write a nested list with medicine details to a csv file named 'medicines.csv'
def write_medicines():
    medicine_data = [
        ["safe", "Paracetamol", 25],
        ["unsafe", "Ibuprofen", 40],
        ["safe", "Cetirizine", 15]
    ]
    #write the code to csv file 
    with open('medicines.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        #write header row
        writer.writerow(["M_type", "M_name", "M_price"])
        #write the records 
        writer.writerow(medicine_data)

        print("Medicine records written to 'medicines.csv' successfully.")

#b) read and display all records from the csv file 'medicines.csv'
def read_medicine():
    try:
        #open the file
        with open('medicines.csv', 'r') as file:
            reader = csv.reader(file)
            records = list(reader)

            if not records:
                print("No records found in the file.")
                return
            print("Medicine Records:")
            for row in records:
                print(", ".join(row))
    except FileNotFoundError:
        print("The file 'medicines.csv' does not exist.")
    except Exception as e:
        print(f"Error reading the file: {e}")


#call the function
write_medicines()
read_medicine()
