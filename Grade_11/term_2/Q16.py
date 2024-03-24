# Accepting five strings into a tuple
string_tuple = tuple(input("Enter five strings separated by space: ").split())

# Finding the length of the shortest string
shortest_length = min(len(s) for s in string_tuple)

# Displaying the result
print("Strings:", string_tuple)
print("Length of the shortest string:", shortest_length)
