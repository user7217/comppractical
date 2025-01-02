import pickle  # Importing pickle for binary file operations

# Input the number of employees
n = int(input("Enter the number of employees: "))

# Create a list of employee dictionaries
employees = [{"empNo": input("EmpNo: "), "ename": input("Name: "), "Salary": float(input("Salary: "))} for _ in range(n)]

# Write the list of employees to a binary file
with open('emp.dat', 'wb') as f: 
    pickle.dump(employees, f)

# Confirm data has been saved
print("Employee details saved to 'emp.dat'.")
