#read file line by line and store it in a list
with open("poem.txt") as f:
    data = f.readlines()
    print( lines for lines in data)