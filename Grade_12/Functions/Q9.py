def Unit_Seven(*n):
    return [x for x in n if str(x)[-1] == '7']

# Function call
L = Unit_Seven(127, 200, 400, 207, 17, -127)

# Display the result
print(L)
