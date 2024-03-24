sample_text = str(input("Enter a string: "))
result = ' '.join(elem.capitalize() for elem in sample_text.split())

print(result)