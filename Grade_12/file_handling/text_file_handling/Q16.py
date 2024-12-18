#program to display contents of file capitalized 
with open("poem.txt") as f:
    data = f.read()
    print(data.upper())

