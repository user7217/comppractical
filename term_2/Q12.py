def remove_item_from_tuple(input_tuple, item_to_remove):
    # Check if the item is present in the tuple
    if item_to_remove in input_tuple:
        # Create a new tuple excluding the specified item
        new_tuple = tuple(element for element in input_tuple if element != item_to_remove)
        return new_tuple
    else:
        print(f"{item_to_remove} not found in the tuple.")
        return input_tuple

# Input: Tuple of elements
input_tuple = tuple(input("Enter a tuple of elements separated by space: ").split())

# Input: Item to be removed
item_to_remove = input("Enter the item to remove from the tuple: ")

# Remove the item from the tuple
result_tuple = remove_item_from_tuple(input_tuple, item_to_remove)

# Displaying the result
print("Original Tuple:", input_tuple)
print("Tuple after removing", item_to_remove + ":", result_tuple)
