# Function to replace elements greater than 10 with 100
def replace_greater_than_10(num_list):
    for i in range(len(num_list)):
        if num_list[i] > 10:
            num_list[i] = 100

# Accepting a list of numbers from the user
num_list = []
n = int(input("Enter the number of elements in the list (between 1-15): "))

if n < 1 or n > 15:
    print("Invalid input! Number of elements should be between 1 and 15.")
else:
    print("Enter the elements of the list:")
    for i in range(n):
        num = float(input())
        num_list.append(num)

    # Replace elements greater than 10 with 100
    replace_greater_than_10(num_list)

    print("List after replacing elements greater than 10 with 100:")
    print(num_list)

