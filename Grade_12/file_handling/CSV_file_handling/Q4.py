import csv

def copy_with_different_delimiter(src="medicine.csv", dest="Temp.csv", delim="|"):
    try:
        with open(src, 'r') as infile, open(dest, 'w', newline='') as outfile:
            writer = csv.writer(outfile, delimiter=delim)
            writer.writerows(csv.reader(infile))
        print(f"Copied contents of '{src}' to '{dest}' with '{delim}' delimiter.")
    except FileNotFoundError:
        print(f"'{src}' not found.")

copy_with_different_delimiter()
