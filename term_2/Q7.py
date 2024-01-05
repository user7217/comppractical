# Function to form a list with the sum of corresponding elements from two lists
def sum_corresponding_elements(list1, list2):
    if len(list1) != len(list2):
        return None  # If lists are not of the same size, return None

    result_list = [list1[i] + list2[i] for i in range(len(list1))]
    return result_list

# Accepting the first list from the user
list1 = []
n = int(input("Enter the number of elements in the lists: "))

print("Enter the elements of the first list:")
for i in range(n):
    elem = int(input())
    list1.append(elem)

# Accepting the second list from the user
list2 = []
print("Enter the elements of the second list:")
for i in range(n):
    elem = int(input())
    list2.append(elem)

# Forming the list with the sum of corresponding elements
result = sum_corresponding_elements(list1, list2)

if result is None:
    print("Lists are not of the same size.")
else:
    print(f"The resulting list with the sum of corresponding elements is: {result}")
