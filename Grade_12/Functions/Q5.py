def LINEARSEARCH(lst, k):
    return [i for i, x in enumerate(lst) if x == k] or None

# Function call statement
my_list = [3, 7, 2, 8, 2, 5, 2]
key = 2
result = LINEARSEARCH(my_list, key)

# Print the result
print(f"The key {key} is found at indexes: {result}") if result else print(f"The key {key} is not found in the list.")