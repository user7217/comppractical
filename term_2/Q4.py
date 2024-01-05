# Function to merge two lists and sort the merged list
def merge_and_sort_lists(list1, list2):
    merged_list = list1 + list2
    sorted_list = sorted(merged_list)
    return sorted_list

# Accepting the first list from the user
list1 = []
n1 = int(input("Enter the number of elements in the first list: "))

print("Enter the elements of the first list:")
for i in range(n1):
    elem = int(input())
    list1.append(elem)

# Accepting the second list from the user
list2 = []
n2 = int(input("Enter the number of elements in the second list: "))

print("Enter the elements of the second list:")
for i in range(n2):
    elem = int(input())
    list2.append(elem)

# Merge and sort the lists
sorted_merged_list = merge_and_sort_lists(list1, list2)

print(f"Merged and sorted list: {sorted_merged_list}")
