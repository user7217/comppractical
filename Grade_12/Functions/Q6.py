def calculate_sum_and_average(numbers):
    return sum(numbers), sum(numbers) / len(numbers)

# Function call statement
my_numbers = [1, 2, 3, 4, 5]
sum_result, average_result = calculate_sum_and_average(my_numbers)

# Print the result
print(f"Sum of the numbers: {sum_result}")
print(f"Average of the numbers: {average_result}")
