# Function for linear search
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index if the element is found
    return -1  # Return -1 if the element is not found

# Accepting values into a list
num_list = []
n = int(input("Enter the number of elements in the list: "))

print("Enter the elements of the list:")
for i in range(n):
    num = int(input())
    num_list.append(num)

# Accept the element to search
element_to_find = int(input("Enter the element to search: "))

# Perform linear search
result = linear_search(num_list, element_to_find)

if result != -1:
    print(f"Element {element_to_find} found at index {result}.")
else:
    print(f"Element {element_to_find} not found in the list.")

