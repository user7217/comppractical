input_tuple = tuple(input("Enter a tuple of elements separated by space: ").split())
element_indices = {element: index for index, element in enumerate(input_tuple)}
print("Element indices:", {element: index for index, element in enumerate(input_tuple)})
