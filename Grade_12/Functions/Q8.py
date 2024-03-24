def part_reverse(lst, start, end):
    lst[start:end+1] = lst[start:end+1][::-1]

# Sample Input Data
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Function Call
part_reverse(my_list, 3, 6)

# Output
print(my_list)
