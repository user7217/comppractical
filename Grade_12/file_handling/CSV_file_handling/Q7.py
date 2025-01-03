import csv

def update_unsafe_price(src="medicines.csv", dest="Updated.csv"):
    try:
        with open(src, 'r') as infile, open(dest, 'w', newline='') as outfile:
            reader = csv.reader(infile)
            writer = csv.writer(outfile)
            writer.writerow(next(reader))  # Write header row
            
            for row in reader:
                if row[0] == "unsafe":  # Check if the type is "unsafe"
                    row[2] = str(round(float(row[2]) * 1.2, 2))  # Increase price by 20%
                writer.writerow(row)
        
        print(f"Prices updated and saved to '{dest}'.")
    except FileNotFoundError:
        print(f"The file '{src}' does not exist.")
    except Exception as e:
        print(f"Error: {e}")

update_unsafe_price()
