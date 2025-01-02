import pickle

def display_emp_file(filename):
    try:
        # Check if file exists
        with open(filename, 'rb') as file:
            # Read and display the contents
            data = pickle.load(file)
            if not data:
                print("No records found in the file.")
            else:
                print("Employee Records:")
                for record in data:
                    print(record)
    except FileNotFoundError:
        print(f"The file '{filename}' does not exist.")
    except Exception as e:
        print(f"Error reading the file: {e}")

# Call the function with "Emp.dat"
display_emp_file("Emp.dat")
