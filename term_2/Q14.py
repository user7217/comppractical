# Accepting details of five employees into a tuple
employee_details = []

for _ in range(5):
    employee_id = input("Enter employee ID: ")
    employee_name = input("Enter employee name: ")
    employee_age = input("Enter employee age: ")
    employee_dob = input("Enter employee DOB: ")
    employee_salary = input("Enter employee salary: ")

    employee = (employee_id, employee_name, employee_age, employee_dob, employee_salary)
    employee_details.append(employee)

# Unpacking details of the first employee
first_employee_id, first_employee_name, first_employee_age, first_employee_dob, first_employee_salary = employee_details[0]

# Displaying the details of the first employee
print("\nDetails of the first employee:")
print("Employee ID:", first_employee_id)
print("Employee Name:", first_employee_name)
print("Employee Age:", first_employee_age)
print("Employee DOB:", first_employee_dob)
print("Employee Salary:", first_employee_salary)
