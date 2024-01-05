# Function to calculate sum and average of a list of numbers
def calculate_sum_average(num_list):
    list_sum = sum(num_list)
    list_average = list_sum / len(num_list)
    return list_sum, list_average

# Accepting a list of numbers from the user
num_list = []
n = int(input("Enter the number of elements in the list: "))

print("Enter the elements of the list:")
for i in range(n):
    num = float(input())
    num_list.append(num)

# Calculate sum and average
sum_of_list, average_of_list = calculate_sum_average(num_list)

print(f"The sum of the numbers in the list is: {sum_of_list}")
print(f"The average of the numbers in the list is: {average_of_list:.2f}")
