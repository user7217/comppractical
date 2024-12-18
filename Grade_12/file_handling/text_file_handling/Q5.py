#program to count number of lines in file
with open("sample.txt") as f:
    data = f.readlines()
    print(len(data))
