#check if same length
def check_length(a,b):
    return len(str(a)) == len(str(b))

a = str(input("Enter the first string: "))
b = str(input("Enter the second string: "))
result = check_length(a,b)
if result:
    print("The strings are of the same length")
else:
    print("The strings are not of the same length")