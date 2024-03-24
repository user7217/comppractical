# Function to rotate the elements of a list
def rotate_list_elements(my_list):
    if len(my_list) <= 1:
        return my_list  # Return the list as it is if it has 0 or 1 element

    last_element = my_list[-1]  # Store the last element before rotation
    for i in range(len(my_list) - 1, 0, -1):
        my_list[i] = my_list[i - 1]  # Shift elements to the right

    my_list[0] = last_element  # Place the last element at the first index
    return my_list

# Accepting a list of elements from the user
num_list = []
n = int(input("Enter the number of elements in the list: "))

print("Enter the elements of the list:")
for i in range(n):
    num = int(input())
    num_list.append(num)

# Rotate the elements of the list
rotated_list = rotate_list_elements(num_list)

print(f"The list after rotating its elements: {rotated_list}")
