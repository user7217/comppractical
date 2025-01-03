import csv

def display_alternate_records(filename="medicines.csv"):
    try:
        with open(filename, 'r') as csvfile:
            reader = csv.reader(csvfile)
            records = list(reader)
            if len(records) == 0:
                print("No records found in the file.")
                return
            
            print("Alternate Records:")
            for i, row in enumerate(records):
                if i % 2 == 0:  # Display alternate rows (0, 2, 4,...)
                    print(", ".join(row))
    except FileNotFoundError:
        print(f"The file '{filename}' does not exist.")
    except Exception as e:
        print(f"Error: {e}")

display_alternate_records()
