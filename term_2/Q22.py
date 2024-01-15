# Sample dictionaries
D1 = {'a': 1, 'b': 2, 'c': 3}
D2 = {'b': 4, 'c': 5, 'd': 6}

# Find overlapping keys
overlapping_keys = set(D1.keys()).intersection(D2.keys())

# Display the result
print("Overlapping Keys:", list(overlapping_keys))
