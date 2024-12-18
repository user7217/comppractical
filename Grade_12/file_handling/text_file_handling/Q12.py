#print line with max length in file
with open("poem.txt") as f:
    data = f.readlines()
    print(max(data, key=len))
    