import csv 

#a) display records where m_type is unsafe
def display_unsafe(filename='medicines.csv'):
    try:
        with open(filename, 'r') as csvfile:
            reader = csv.reader(csvfile)
            records = list(reader)
            if len(records) <= 1: # only header row exists
                print("No records found in the file.")
                return
            
            print("Unsafe Medicines:")
            found = False
            for row in records[1:]:
                if row[0] == 'unsafe':
                    print(", ".join(row))
                    found = True
            
            if not found:
                print("No unsafe medicines found.")
    except FileNotFoundError:
        print(f"The file '{filename}' does not exist.")
    except Exception as e:
        print(f"Error reading the file: {e}")

#b) display records where m_price is greater than 400
def display_price_above_400(filename='medicines.csv'):
    try:
        with open(filename, 'r') as csvfile:
            reader = csv.reader(csvfile)
            records = list(reader)
            if len(records) <= 1: # only header row exists
                print("No records found in the file.")
                return
            
            print("Mdeicines with price above 400:")
            found = False
            for row in records[1:]:
                if float(row[2]) > 400:
                    print(", ".join(row))
                    found = True
            
            if not found:
                print("No medicines found with price above 400.")
    except FileNotFoundError:
        print(f"The file '{filename}' does not exist.")
    except Exception as e:
        print(f"Error reading the file: {e}")

#display the number of records exluding header row
def count_records(filename='medicines.csv'):
    try:
        with open(filename, 'r') as csvfile:
            reader = csv.reader(csvfile)
            records = list(reader)
            record_count = len(records) - 1
            print(f"Number of records: {record_count}")
    except FileNotFoundError:
        print(f"The file '{filename}' does not exist.")
    except Exception as e:
        print(f"Error reading the file: {e}")

#call the functions
print("\nDisplaying unsafe medicines:")
display_unsafe()

print("\nDisplaying medicines with price above 400:")
display_price_above_400()

print("\nCounting the number of records:")
count_records()