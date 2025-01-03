import csv

def filter_safe_records(src="medicines.csv", dest="Filtered.csv"):
    try:
        with open(src, 'r') as infile, open(dest, 'w', newline='') as outfile:
            reader = csv.reader(infile)
            writer = csv.writer(outfile)
            writer.writerow(next(reader))  # Write the header row
            writer.writerows(row for row in reader if row[0] != "safe")  # Skip rows with type "safe"
        print(f"Filtered records written to '{dest}'.")
    except FileNotFoundError:
        print(f"'{src}' not found.")

filter_safe_records()
