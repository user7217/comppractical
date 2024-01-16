str1 = input("Enter a string (STR1): ")
str2 = ' '.join(word for word in str1.split() if not word[0].islower())
print(f"STR2 after removing words starting with lowercase: {str2}")

