def separate_even_odd(input_list):
    even_list = []
    odd_list = []

    for number in input_list:
        if number % 2 == 0:
            even_list.append(number)
        else:
            odd_list.append(number)

    return even_list, odd_list

# Input: List of numbers
input_numbers = [int(x) for x in input("Enter a list of numbers separated by space: ").split()]

# Separating even and odd elements
even_elements, odd_elements = separate_even_odd(input_numbers)

# Displaying the results
print("Even elements:", even_elements)
print("Odd elements:", odd_elements)
